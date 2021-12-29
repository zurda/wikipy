# Wikipy

To install the project, run:

```
poetry install
```

Poetry has now created a virtual environment dedicated to your project, and installed your initial package into it. It has also created a so-called lock file, named `poetry.lock`.

Run a Python session inside the new virtual environment with the command:

```
poetry run wikipy
```

To check code format:

```
poetry run flake8
poetry run black .
```
