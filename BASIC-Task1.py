# Create an empty list to hold tasks
task_list = []

# Function to display the current tasks
def display_tasks():
    if not task_list:
        print("Your to-do list is empty.")
    else:
        print("Tasks to be Completed:")
        for index, task in enumerate(task_list, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['name']} - {status}")

# Function to add a new task
def add_task(task_name):
    task = {"name": task_name, "completed": False}
    task_list.append(task)
    print(f"A new task '{task_name}' has been added.")

# Function to mark a task as done
def complete_task(task_number):
    if 1 <= task_number <= len(task_list):
        task_list[task_number - 1]["completed"] = True
        print(f"Task {task_number} has been marked as completed.")
    else:
        print("Invalid task number. Please provide a valid task number.")

# Function to remove a task
def remove_task(task_number):
    if 1 <= task_number <= len(task_list):
        removed_task = task_list.pop(task_number - 1)
        print(f"The task '{removed_task['name']}' has been removed.")
    else:
        print("Invalid task number. Please provide a valid task number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. View to-do list")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Exit")
    choice = input("Please enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task_name = input("Enter the new task: ")
        add_task(task_name)
    elif choice == '3':
        display_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        complete_task(task_number)
    elif choice == '4':
        display_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please select a valid option.")
