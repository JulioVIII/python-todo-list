
tasks = []


def menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Save tasks")
    print("4. Load tasks")
    print("5. Exit")


def add_task():
    task = input("Enter a task: ")

    if not task:
        print("Task cannot be empty")
        return

    tasks.append(task)

    print("Task added successfully")


def view_tasks():
    if not tasks:
        print("No tasks found")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def save_tasks():
    file = open("tasks.txt", "w")

    for task in tasks:
        file.write(task + "\n")

    file.close()

    print("Tasks saved successfully")


def load_tasks():
    try:
        file = open("tasks.txt", "r")

        tasks.clear()

        for line in file:
            tasks.append(line.strip())

        file.close()

        print("Tasks loaded successfully")

    except FileNotFoundError:
        print("No saved tasks found")


while True:
    menu()
    option = input("Choose an option: ")

    if option == "1":
        add_task()

    elif option == "2":
        view_tasks()

    elif option == "3":
        save_tasks()

    elif option == "4":
        load_tasks()

    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
