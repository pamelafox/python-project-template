import json
import logging
import sys
import os
from src.api_client import WordPressAPIClient
from src.link_optimizer import LinkOptimizer

# Add the project root to the Python path to avoid ModuleNotFoundError
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

def load_config(config_path="config/config.json"):
    """Load configuration from a JSON file."""
    try:
        with open(config_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("Config file not found. Ensure 'config/config.json' exists.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing config file: {e}")
        sys.exit(1)

def process_post(post, link_optimizer, api_client):
    """Analyze and update a single post."""
    post_id = post["id"]
    content = post["content"]["rendered"]

    logging.info(f"Analyzing post {post_id}...")
    updated_content = link_optimizer.optimize_content(content, posts)

    if content != updated_content:  # Only update if changes were made
        logging.info(f"Updating post {post_id}...")
        try:
            api_client.update_post(post_id, updated_content)
            logging.info(f"Post {post_id} updated successfully.")
        except Exception as e:
            logging.error(f"Failed to update post {post_id}: {e}")
    else:
        logging.info(f"No changes for post {post_id}.")

def main():
    # Step 1: Load configuration
    config = load_config()
    base_url = config["base_url"]
    username = config["username"]
    app_password = config["app_password"]
    external_links = config["external_links"]

    # Step 2: Initialize modules
    logging.info("Initializing API client and Link Optimizer...")
    api_client = WordPressAPIClient(base_url, username, app_password)
    link_optimizer = LinkOptimizer(external_links)

    # Step 3: Fetch posts
    logging.info("Fetching posts from WordPress...")
    try:
        posts = api_client.get_posts()
        logging.info(f"Fetched {len(posts)} posts.")
    except Exception as e:
        logging.error(f"Failed to fetch posts: {e}")
        sys.exit(1)

    # Step 4: Analyze and update posts
    for post in posts:
        process_post(post, link_optimizer, api_client)

    logging.info("Processing complete.")

if __name__ == "__main__":
    main()
