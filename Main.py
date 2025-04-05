# Simple To-Do List in Python

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    show_tasks()
    if tasks:
        try:
            index = int(input("\nEnter the task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Removed: {removed_task}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

while True:
    print("\nOptions: 1. Add Task | 2. View Tasks | 3. Remove Task | 4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
