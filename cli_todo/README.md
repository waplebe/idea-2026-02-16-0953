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

## Improvements

*   **Error Handling:**  The script now includes more robust error handling, specifically for invalid task numbers and invalid JSON in the data file.
*   **Data Validation:**  The `remove_task` function validates the input task number to ensure it's within the valid range of tasks.
*   **JSONDecodeError Handling:** The `load_tasks` function now handles `JSONDecodeError` gracefully, returning an empty list if the JSON file is corrupted.
*   **Comprehensive Testing:** Added a test case `test_load_tasks_invalid_json` to verify the script handles invalid JSON in the data file.
*   **Clearer Error Messages:** Improved error messages to provide more helpful feedback to the user.

## Examples

*   **Add a task:** `python main.py add Buy groceries`
*   **List tasks:** `python main.py list`
*   **Remove task 1:** `python main.py remove 1`

## New Features

*   **JSON Corruption Handling:** The script now gracefully handles corrupted JSON files in `todo.json` by returning an empty list and printing an informative error message. This prevents the program from crashing when encountering invalid data.
*   **Comprehensive JSON Error Handling:** Added a test case `test_load_tasks_corrupted_json` to specifically verify the handling of corrupted JSON files.