"""
Task Tracker CLI Application

This script allows you to add, update, delete, and list tasks stored in a JSON file.
Each task has:
- id
- description
- status (todo, in-progress, done)
- createdAt
- updatedAt
"""

import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file, create new if not exists."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    """Save tasks into the JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


def generate_id(tasks):
    """Generate a unique ID for each task."""
    return max([task["id"] for task in tasks], default=0) + 1


def add_task(description):
    """Add a new task with given description."""
    tasks = load_tasks()
    task = {
        "id": generate_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")


def update_task(task_id, description):
    """Update an existing task's description."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task {task_id} not found")


def delete_task(task_id):
    """Delete a task by ID."""
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task {task_id} not found")
    else:
        save_tasks(new_tasks)
        print(f"Task {task_id} deleted successfully")


def mark_status(task_id, status):
    """Change the status of a task (todo, in-progress, done)."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task {task_id} not found")


def list_tasks(filter_status=None):
    """List all tasks, optionally filtered by status."""
    tasks = load_tasks()
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        print(
            f"[{task['id']}] {task['description']} - {task['status']} "
            f"(Created: {task['createdAt']}, Updated: {task['updatedAt']})"
        )


def handle_command(command, args):
    """Handle CLI commands and arguments."""
    if command == "add" and len(args) >= 1:
        add_task(" ".join(args))
    elif command == "update" and len(args) >= 2:
        update_task(int(args[0]), " ".join(args[1:]))
    elif command == "delete" and len(args) == 1:
        delete_task(int(args[0]))
    elif command == "mark-in-progress" and len(args) == 1:
        mark_status(int(args[0]), "in-progress")
    elif command == "mark-done" and len(args) == 1:
        mark_status(int(args[0]), "done")
    elif command == "list":
        if not args:
            list_tasks()
        elif args[0] in ["todo", "in-progress", "done"]:
            list_tasks(args[0])
        else:
            print("Invalid status filter. Use: todo | in-progress | done")
    else:
        print("Invalid command or arguments")


def main():
    """Main entry point for the CLI."""
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments...]")
        return

    command = sys.argv[1]
    args = sys.argv[2:]
    handle_command(command, args)


if __name__ == "__main__":
    main()
