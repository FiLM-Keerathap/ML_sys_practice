# ML_sys_practice

<!-- TOC depthFrom:2 depthTo:3 -->

- [Dependencies](#dependencies)
- [Project: Structured Data](#structured-data) 🔜 in progress
- [Project: Computer Vision](#computer-vision) ⏳ Coming soon
- [Project: NLP](#nlp) ⏳ Coming soon

<!-- /TOC -->

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

- Use [poetry-kernel](https://github.com/pathbird/poetry-kernel) for Jupyter Notebook integration with Python packages follow `pyproject.toml`.

# Projects

## [Structured Data](Structured_Data)

🔜 in progress

## [Computer Vision](Computer_Vision)

⏳ Coming soon

## [NLP](NLP)

⏳ Coming soon

---
