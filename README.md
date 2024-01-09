# ML_sys_practice

<!-- TOC depthFrom:2 depthTo:3 -->

- [Dependencies](#dependencies)
- [Project: Structured Data](#structured-data) 🔜 in progress
- [Project: Computer Vision](#computer-vision) ⏳ Coming soon
- [Project: NLP](#nlp) ⏳ Coming soon

<!-- /TOC -->
## Enviroment setup

I develop in WSL: Ubuntu

## Dependencies

Using [Poetry](https://python-poetry.org/) for Python Package and Dependency Management

### Basic Steps

0. [Install Poetry](https://python-poetry.org/docs/#installation) if not yet
installed.
1. **Navigate to your project directory:**

    ```sh
    cd <PROJECT_DIR>
    ```

2. **Initialize your project:**

    ```sh
    poetry init -n
    ```

    - This command interactively creates a `pyproject.toml` file in your project directory.

3. **Add dependencies:**
    - Specify them in the `tool.poetry.dependencies` section of `pyproject.toml`:

        ```toml
        [tool.poetry.dependencies]
        numpy = "^1.19"
        ```

    - Use a mapping of package names and version constraints.

4. **Use the `add` command to add dependencies:**

    ```sh
    poetry add numpy
    ```

    - It finds a suitable version constraint and installs the package along with sub-dependencies.

    **NOTE:** If you already have `pyproject.toml`, you can use the `install` command to read the file, resolve dependencies, and install them.

    ```sh
    poetry install
    ```

### Updating Dependencies

- **To update to the latest compatible version:**

    ```sh
    poetry update package
    ```

- **To upgrade to the latest available version:**

    ```sh
    poetry add package@latest
    ```

### Installing Multiple Packages

```sh
$ poetry add pandas numpy
# or
$ poetry add $(cat requirements.txt)
```

### Remove a dependency

The `remove` command removes required packages to your `pyproject.toml`` and installs them.

```bash
poetry remove numpy
```

### Jupyter Notebook Integration

To integrate Poetry with Jupyter Notebook and manage Python packages effectively, consider using [poetry-kernel](https://github.com/pathbird/poetry-kernel). Follow the steps below, and choose the method that suits your workflow.

#### Method 1: Select Another Kernel

When running Jupyter Notebook, you can choose another kernel from `Python environments`.
Use a kernel from the Python environment managed by Poetry
Select the kernel named "<kernel_name>"

#### Method 2: Use Poetry-Managed Kernel

Create and use a new kernel managed by Poetry:

```bash
# Create a new kernel named "<kernel_name>"
$ poetry run python -m ipykernel install --user --name=<kernel_name>
```

#### Method 3: Run Jupyter Notebook Server

Start Jupyter Notebook server and connect using the provided URL:

```bash
# Run Jupyter Notebook server
$ poetry run jupyter notebook
```

# Projects

## [Structured Data](Structured_Data)

🔜 in progress

## [Computer Vision](Computer_Vision)

⏳ Coming soon

## [NLP](NLP)

⏳ Coming soon


credit 
https://github.com/statmike/vertex-ai-mlops/tree/main
---
