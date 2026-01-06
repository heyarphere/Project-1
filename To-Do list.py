tasks = []

# function to display the available option
def display_menu():
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Exit")

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
                  