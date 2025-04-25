# Development Tools

## Sanity checks before commiting code
### [`pre-commit`](https://pre-commit.com/)

**Description**: The *pre-commit* framework automates tasks like code formatting, linting, and testing before commits. It runs hooks—scripts executed before committing—to enforce coding standards and maintain code quality, reducing manual effort and ensuring consistency across teams.

#### Current hooks applied in this repository:
This is the list of current hooks used in this repository. Those hooks are defined in the `.pre-commit-config.yaml` file.

| *pre-commit* hook       | Status   | Description |
|-------------------------|----------|-------------|
| check-added-large-files | ✅  | Prevents adding large files to the repository. |
| check-yaml              | ✅  | Ensures YAML files are properly formatted. |
| end-of-life-fixer       | ✅  | Fixes deprecated Python syntax and libraries. |
| mixed-line-ending       | ✅  | Fixes mixed line endings (LF/CRLF) in files. |
| trailing-whitespace     | ✅  | Removes trailing whitespace from code. |
| [black]                 | ✅  | Formats Python code to adhere to Black style. |
| [isort]                 | ✅  | Sorts and organizes Python imports. |
| [flake8]                | ✅  | Checks Python code for PEP 8 compliance. |
| [djlint-django]         | ✅  | Lints Django template files for style issues. |
| [ruff]                  | ❌  | Python linter, currently disabled. |



#### Usage:

##### 1. Install the hooks

You need a `.pre-commit-config.yaml` file that specify the hooks to use in the project, normally it is already created by the team and any modification should be discussed with the maintainers.

Run this command to install the hooks:
```bash
pre-commit install
```

##### 2. Run the hooks manually (optional)

*pre-commit* runs the hooks automatically everytime you try to commit the code. However, if you want to run the hooks without trying to commit the code just run the following code:

```bash
pre-commit run --all-files
```

##### 3. Update the hooks
To update the hooks to the last release made by the developers, you just need to run this:
```bash
pre-commit clean
pre-commit autoupdate
pre-commit install
```
#### Typical workflow
1. Make changes to your code.
2. Run `git add .` to stage your changes.
3. Run `git commit -m "<some conventional commit message>"`
4. The *pre-commit* hook will run automatically before the commit is finalized, checking for any issues (like formatting problems or linting errors).
5. If the checks pass, the commit will go through. If there are issues, the commit will be blocked, and you'll be asked to fix them.

#### Adding up/removing/edit a pre-commit hook:
Note: this part of this mini-guide is just only when you need to add an additional check before your commits. Most of the time you do not need to do this unless you talk with your team and discuss this before.

1. Open the `pre-commit-config.yaml` file.
2. TO ADD UP: add the hook at the end of the file.
3. TO REMOVE: instead of deleting the code, just comment the lines that conform the code for the specific hook.
4. TO EDIT: modify the specific hook.
5. Run `pre-commit install` to install the new changes.

### [`isort`](https://pycqa.github.io/isort/)

*isort* is a Python tool that automatically sorts imports to keep them clean and organized. It arranges imports by type (standard, third-party, local), improving readability and maintaining consistent order.

To use *isort*, simply run:
```bash
isort your_file.py
```

For auto-formatting all file in a project:
```bash
isort .
```
It’ll sort imports, making your code more maintainable!

### [`black`](https://black.readthedocs.io/en/stable/)
*black* is an opinionated Python code formatter that automatically formats code to adhere to the [PEP 8 style guide](https://peps.python.org/pep-0008/), ensuring consistent code style.

To use *black*, simply run:
```bash
black your_file.py
```
For formatting all files in a project:
```bash
black .
```
It will reformat your code to be more readable and consistent!

### [`Flake8-pyproject`](https://github.com/john-hen/Flake8-pyproject) [[Flake8](https://flake8.pycqa.org/en/latest/) plugin]
*flake8-pyproject* is a plugin for *flake8* that allows configuration of *flake8* settings via `pyproject.toml`, simplifying configuration management.

To use *flake8* with pyproject.toml`:
```bash
flake8 your_file.py
```
It checks Python code for PEP 8 compliance and other issues, enforcing best practices!


### [`djlint-django`](https://www.djlint.com/docs/languages/django/)
*djlint-django* is a linter for Django template files, ensuring consistent formatting and syntax by catching common mistakes in HTML and template tags.

To use *djlint-django*:
```bash
djlint your_template.html
```
For auto-formatting all templates:
```bash
djlint .
```
It ensures your Django templates are clean and readable!

### [`Ruff`](https://docs.astral.sh/ruff/)
*ruff* is a fast Python linter that performs static analysis, checking for errors, stylistic issues, and enforcing best practices across your Python code.

To use *ruff*:
```bash
ruff your_file.py
```
For checking all files in a project:
```bash
ruff .
```
It quickly detects issues, helping you keep your code in top shape!

## Testing
### [`Pytest`](https://docs.pytest.org/en/stable/)
*pytest* is a powerful testing framework for Python that makes writing simple and scalable test cases straightforward. It automatically discovers tests by looking for functions that start with `test_`.

#### Usage:

##### 1. Writing Tests:

Define a test function like this:
```python
def test_addition():
    assert 1 + 1 == 2
```

##### 2. Running Tests:

- To run all tests in your project, simply execute:
```bash
pytest
```
*pytest* will find all files matching `test_*.py` and run the tests inside them.

- Running a Single Test:

To run a specific test function, specify the file and test function like so:
```bash
pytest test_file.py::test_addition
```

##### Additional Features:
- pytest provides detailed outputs, showing which tests passed or failed.
- Supports fixtures for setup/teardown logic.
- Includes plugins to extend functionality (e.g., for test coverage).

This makes pytest ideal for both simple and complex testing needs!
