# Initialize an empty to-do list
todo_list = []

def addTask(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list\n")

def viewTasks():
    if todo_list:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    else:
        print("To-Do List is empty.")

def completeTask(i):
    if 1 <= i <= len(todo_list):
        completed_task = todo_list.pop(i - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")

while True:
    print("\nTo-Do List Menu\n")
    print("Press 1 to Add Task\n")
    print("Press 2 to View Tasks\n")
    print("Press 3 to Complete Task\n")
    print("Press 4 to Exit\n")

    choice = input("Enter your choice\n")

    if choice == '1':
        task = input("Enter the task\n")
        addTask(task)
    elif choice == '2':
        viewTasks()
    elif choice == '3':
        viewTasks()
        taskIndex = int(input("Enter the index of the task to mark as completed\n"))
        completeTask(taskIndex)
    elif choice == '4':
        print("Exiting the to-do list\n")
        break
    else:
        print("Invalid choice\n")





