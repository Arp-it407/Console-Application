import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. [{status}] {task['description']}")

def add_task(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks.append({"description": description, "completed": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Empty description, task not added.")

def complete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as complete: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input, please enter a number.")

def remove_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            save_tasks(tasks)
            print(f"Removed task: {removed['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input, please enter a number.")

def main():
    print("Welcome to Task Manager")
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Quit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

