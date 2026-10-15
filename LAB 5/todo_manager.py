
"""A simple command-line todo manager."""

import json
from datetime import datetime

tasks = {}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def add_task(title, priority="medium", labels=None):
    """Add a task and return its ID."""
    if labels is None:
        labels = []

    task_id = max(tasks.keys(), default=0) + 1
    labels = list(labels)
    labels.append(priority)

    tasks[task_id] = {
        "title": title,
        "priority": priority,
        "labels": labels,
        "done": False,
        "created": datetime.now().isoformat(),
    }
    return task_id


def complete_task(task_id):
    """Mark a task as completed."""
    if task_id in tasks:
        tasks[task_id]["done"] = True
        return True

    print("No task with id", task_id)
    return False


def pending_tasks():
    """Return pending task titles sorted by priority."""
    pending = [
        task for task in tasks.values()
        if not task["done"]
    ]
    pending.sort(
        key=lambda task: PRIORITY_ORDER.get(
            task["priority"], 3
        )
    )
    return [task["title"] for task in pending]


def find_task(keyword):
    """Find a task by keyword and return its ID."""
    for task_id, task in tasks.items():
        if keyword.lower() in task["title"].lower():
            return task_id
    return None


def save_tasks(file_name="tasks.json"):
    """Save all tasks to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def load_tasks(file_name="tasks.json"):
    """Load tasks from a JSON file."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            loaded_tasks = json.load(file)
    except FileNotFoundError:
        return {}

    return {
        int(task_id): task
        for task_id, task in loaded_tasks.items()
    }


def export_json(file_name="tasks_export.json"):
    """Export tasks to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def main():
    """Run a small demonstration of the todo manager."""
    add_task("Submit lab report", "high")
    add_task("Buy groceries")
    add_task("Call plumber", "low")
    add_task("Book train tickets", "high")

    complete_task(2)
    complete_task(99)

    print("Pending tasks:", pending_tasks())
    print("Task id for 'plumber':", find_task("plumber"))
    print("Task id for 'gym':", find_task("gym"))

    pending = pending_tasks()
    suggestion = pending[0] if pending else "No pending tasks"
    print("Try this next:", suggestion)

    save_tasks()
    restored = load_tasks()
    print("Tasks restored from file:", len(restored))

    export_json()
    print("Exported tasks to tasks_export.json")


if __name__ == "__main__":
    main()
