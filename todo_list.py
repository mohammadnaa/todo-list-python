
tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {task['title']} {status}")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def mark_done():
    show_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num - 1]['done'] = True
        print("Task marked as done!")
    except:
        print("Invalid input.")

def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted!")
    except:
        print("Invalid input.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

