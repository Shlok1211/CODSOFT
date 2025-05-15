tasks = []

#function to show all tasks
def showAllTasks():
    if len(tasks) == 0:
        print("No tasks found !")
    else:
        print("Your Tasks :-")
        for i,j in enumerate(tasks,1):  #Starts from 1 index
            if j["done"]:
                status = "Done"
            else:
                status = "Pending"
            print({f"{i}. {j['title']} [{status}]"})
    print()

#funtion to add new task
def addNewTask():
    title = input("Enter the Task :- ")
    tasks.append({"title": title, "done": False})
    print("Task added to the pending list \n")

#function to update task
def updateTask():
    showAllTasks()
    try:
        n = int(input("Enter the Task Number to Update :- "))
        if (1 <= n) & (n<=len(tasks)):
            newTitle = input('Enter the new Task :- ')
            tasks[n-1]["title"] = newTitle
            print("Task Updated Successfully")
        else:
            print("The task number entered is invalid")
    except ValueError:
        print("The Task number entered is invalid")

#function to delete task
def deleteTask():
    showAllTasks()
    try:
        n = int(input("Enter the Task Number to Delete :- "))
        if (1 <= n) & (n<=len(tasks)):
            tasks.pop(n-1)
            print("Task Deleted Successfully")
        else:
            print("The task number entered is invalid")
    except ValueError:
        print("The Task number entered is invalid")

#funtion to mark the task as done
def markDone():
    showAllTasks()
    try:
        n = int(input("Enter the Task Number to mark as Done :- "))
        if (1 <= n) & (n<=len(tasks)):
            tasks[n-1]["done"] = True
            print("Task Marked as Done")
        else:
            print("The task number entered is invalid")
    except ValueError:
        print("The Task number entered is invalid")

#Main menu and function call loop
while True:
    print("\n----- This is the Menu of To Do List -----")
    print("1. View all the Tasks")
    print("2. Add a new Task")
    print("3. Update an existing Task")
    print("4. Delete an existing Task")
    print("5. Mark existing Task as Done")
    print("6. Exit")
    print("-"*42)

    choice = int(input("Enter your choice (1-6) :- "))
    print("-" * 42)
    print()

    if choice == 1:
        showAllTasks()
    elif choice == 2:
        addNewTask()
    elif choice == 3:
        updateTask()
    elif choice == 4:
        deleteTask()
    elif choice == 5:
        markDone()
    elif choice == 6:
        print("Thanks for using To Do List App.")
        print("@CodSoft")
        break

    else:
        print("Invalid choice !, Please enter a number between 1-6 ")