# Python project template

This is a template repository for any Python project that comes with the following dev tools:

* black: auto-formats code
* isort: sorts the imports
* flake8: looks for common errors
* pyupgrade: upgrades Python syntax

All of those checks are run as pre-commit hooks using the `pre-commit` library.

It includes `pytest` for testing plus the `pytest-cov` plugin to measure coverage.

The checks and tests are all run using Github actions on every pull request and merge to main.

This repository is setup for Python 3.10. To customize that, change the `VARIANT` argument in `.devcontainer/devcontainer.json`, and change the flag passed into `pyupgrade` in `.precommit-config.yaml` and `.github/workflows/python.yaml`.

## Development instructions

## With devcontainer

This repository comes with a devcontainer (a Dockerized Python environment). If you open it in Codespaces, it should automatically initialize the devcontainer.

Locally, you can open it in VS Code with the Dev Containers extension installed.

## Without devcontainer

If you can't or don't want to use the devcontainer, then you should first create a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

Then install the dev tools and pre-commit hooks:

```
pip3 install --user -r requirements-dev.txt
pre-commit install
```

## Adding code and tests

This repository starts with a very simple `main.py` and a test for it at `tests/main_test.py`.
You'll want to replace that with your own code, and you'll probably want to add additional files
as your code grows in complexity.

When you're ready to run tests, just run:

```
pytest
```

### 🔎 Found an issue or have an idea for improvement?

Help me make this template repository better by letting us know and opening an issue!
