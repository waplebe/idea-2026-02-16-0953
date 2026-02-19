import argparse
import json
import os

DATA_FILE = "todo.json"

def load_tasks():
    """Loads tasks from the data file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {DATA_FILE}.  File may be corrupted.  Starting with an empty list.")
            return []
    else:
        return []

def save_tasks(tasks):
    """Saves tasks to the data file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    """Adds a task to the list."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def list_tasks():
    """Lists all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def remove_task(task_number):
    """Removes a task by its number."""
    tasks = load_tasks()
    try:
        index = int(task_number) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid task number. Please enter a number.")


def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("action", choices=["add", "list", "remove"], help="Action to perform.")
    parser.add_argument("task", nargs="*", help="Task(s) to add or number of task to remove.")

    args = parser.parse_args()

    if args.action == "add":
        if not args.task:
            print("Please provide a task to add.")
        else:
            add_task(" ".join(args.task))
    elif args.action == "list":
        list_tasks()
    elif args.action == "remove":
        if not args.task:
            print("Please provide a task number to remove.")
        else:
            remove_task(args.task[0])


if __name__ == "__main__":
    main()