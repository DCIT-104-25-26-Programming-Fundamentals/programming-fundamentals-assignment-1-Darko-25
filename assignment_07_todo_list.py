

def add_task(tasks):
    """Prompt for a task description and add it to the list."""
    description = input("Enter task: ")
    tasks.append(description)
    print(f'Task added: "{description}"')


def view_tasks(tasks):
    """Display all tasks, numbered from 1. Show a message if empty."""
    if not tasks:
        print("Your task list is empty. Add something to get started!")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def delete_task(tasks):
    """Show tasks, ask which number to remove, and delete it."""
    if not tasks:
        print("Your task list is empty. Nothing to delete.")
        return

    view_tasks(tasks)
    choice = input("Enter task number to delete: ")

    if not choice.isdigit():
        print("Error: Please enter a valid task number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("Error: That task number does not exist.")
        return

    removed = tasks.pop(index)
    print(f'Task "{removed}" has been removed.')


def print_menu():
    """Display the menu options."""
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


if __name__ == "__main__":
    tasks = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")
        print()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please enter a number from 1 to 4.")

        print()