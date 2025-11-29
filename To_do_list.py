def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\nTo Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks found")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("Enter task to add: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete")
        else:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Removed task: {removed}")
            else:
                print("Invalid number")

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice")
