import json

Filename = 'todolist.json'

def loadt():
    try:
        with open(Filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def savet(tasks):
    with open(Filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_menu():
    print("\nToDo List:")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


def viewt(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        index = 1
        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['description']} - {status}")
            index += 1

def addt(tasks):
    description = input("Enter the task description: ")
    tasks.append({"description": description, "completed": False})
    savet(tasks)
    print("Task added successfully.")

def done(tasks):
    viewt(tasks)
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        savet(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def deletet(tasks):
    viewt(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        savet(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = loadt()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            viewt(tasks)
        elif choice == '2':
            addt(tasks)
        elif choice == '3':
            done(tasks)
        elif choice == '4':
            deletet(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
