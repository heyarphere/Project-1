tasks = []

# function to display the available option
def display_menu():
    print("\n1. Add Task🤺")
    print("2. Edit Task👨‍🏫")
    print("3. Delete Task😶‍🌫️")
    print("4. Exit🫣")

# start an infinite loop to continuously interact with the user
while True:
    display_menu()

    # get the user's choice
    choice = input("Select an option: ")

    # option 1: Add Task
    if choice == '1':
        # prompt the user to enter a task
        task = input("Enter task: ")
        # Add the task to the list
        tasks.append(task)
        print("Task added successfully.")

    # option 2: Edit Task
    elif choice == '2':
        if tasks:
            # Display the current tasks with their indices 
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            # prompt the user to enter the index of the task to edit
            try:
                task_index = int(input("Enter task index to edit: ")) - 1
                if task_index < 0 or task_index >= len(tasks):
                    print("Invalid index.")
                else:
                    new_task = input("Enter new task: ")
                    tasks[task_index] = new_task
                    print("Task updated successfully.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("NO tasks available to edit.")
    # option 3: Delete Task
    elif choice == '3':
        if tasks:
            # display the current tasks with their indices
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            # prompt the user to enter the index of the task to delete
            try:
                task_index = int(input("Enter task index to delete: ")) -1
                if task_index < 0 or task_index >= len(tasks):
                    print("Invalid index.")
                else:
                    removed = tasks.pop(task_index)
                    print(f"Task '{removed}' deleted successfully.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("NO tasks available to delete.")

    # option 4: Exit
    elif choice == '4':
        # Exit the application
        print("Exiting the application. Goodbye!") 
        break
    # handle invalid menu choices
    else:
        print("Invalid choice. Please select a valid option.")

