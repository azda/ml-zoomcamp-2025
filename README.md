# ML Zoomcamp 2025

This project uses `uv` for managing Python environments and dependencies. Below are the steps to set up the project for the first time.

## Installation

1.  **Install `uv`**:
    You can install `uv` using `pip` or your system's package manager.

    *   **Using `pip`**:
        ```zsh
        pip install uv
        ```

    *   **Using Homebrew (macOS)**:
        ```zsh
        brew install uv
        ```

2.  **Create a Virtual Environment**:
    Create a virtual environment in a `.venv` directory:
    ```zsh
    uv venv
    ```
    This will create a virtual environment that `uv` will automatically use.

3.  **Install Dependencies**:
    To install or update dependencies from `pyproject.toml`, use:
    ```zsh
    uv sync
    ```

## Additional Commands

-   **List Installed Packages**:
    ```zsh
    uv pip list
    ```

-   **Install Additional Packages**:
    ```zsh
    uv pip install <package-name>
    ```

-   **Freeze Dependencies**:
    ```zsh
    uv pip freeze > requirements.txt
    ```