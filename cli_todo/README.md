# Simple CLI Todo List

This is a simple command-line tool for managing a todo list.

## Features

*   **Add Tasks:** Add tasks to the list.
*   **List Tasks:** View all tasks in the list.
*   **Remove Tasks:** Remove tasks from the list by number.

## Usage

1.  **Add a task:**
    ```bash
    python main.py add task_description
    ```

2.  **List tasks:**
    ```bash
    python main.py list
    ```

3.  **Remove a task:**
    ```bash
    python main.py remove task_number
    ```
    Replace `task_number` with the number of the task you want to remove (as displayed when listing tasks).

## Data Storage

Tasks are stored in a JSON file named `todo.json`.

## Testing

Unit tests are included to ensure the functionality of the script.  Run them using:

```bash
python -m unittest test_main.py
```