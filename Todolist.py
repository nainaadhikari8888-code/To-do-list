import json
import time
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    name = input("Enter task: ")
    reminder = int(input("Set reminder (seconds, 0 for none): "))
    task = {
        "name": name,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Pending",
        "reminder": reminder
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return

    for i, t in enumerate(tasks):
        # ✅ FIX: handle old & new keys
        name = t.get("name", t.get("task_name", "Unknown"))
        created = t.get("created", t.get("created_on", "N/A"))
        status = t.get("status", "Pending")

        print(i+1, name, "|", status, "|", created)

def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    n = int(input("Enter task number: "))
    if 1 <= n <= len(tasks):
        print("1.Edit Name  2.Mark Completed")
        ch = int(input("Choice: "))
        if ch == 1:
            tasks[n-1]["name"] = input("New task name: ")
        elif ch == 2:
            tasks[n-1]["status"] = "Completed"
        save_tasks(tasks)
        print("Task updated")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    n = int(input("Enter task number to delete: "))
    if 1 <= n <= len(tasks):
        tasks.pop(n-1)
        save_tasks(tasks)
        print("Task deleted")

def reminders(tasks):
    print("Reminders started...")
    for t in tasks:
        if t.get("reminder", 0) > 0 and t.get("status") == "Pending":
            time.sleep(t["reminder"])
            print("🔔 Reminder:", t.get("name", t.get("task_name")))

def main():
    tasks = load_tasks()
    while True:
        print("\n1.Add 2.View 3.Update 4.Delete 5.Reminders 6.Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            add_task(tasks)
        elif ch == 2:
            view_tasks(tasks)
        elif ch == 3:
            update_task(tasks)
        elif ch == 4:
            delete_task(tasks)
        elif ch == 5:
            reminders(tasks)
        elif ch == 6:
            print("Program exited")
            break
        else:
            print("Invalid choice")

main()
