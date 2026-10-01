def view_task(tasks):
    if len(tasks) == 0:
        print("No tasks found")
        return 
    for index, task in enumerate(tasks):
        if task["Done"]==True:
            status = "Done"
        else:
            status = "Pending"
        print(index + 1 ,"." , task["description"], "-" , status) 
def add_task(tasks):
    description = input("Enter your task :")
    task = {
        "description" : description ,
        "Done": False
    }
    tasks.append(task)
    print("Task Added Successfully....!")

def mark_done(tasks):
    if len(tasks) ==0:
        print("No tasks found")
        return 
    view_task(tasks)
    task_num =int(input("Enter the task number :"))
    index = task_num -1
    tasks[index]["Done"]=True
    print("Task Marked Successfully...!")

def delete_task(tasks):
    if len(tasks) ==0:
         print("No tasks found")
         return  
    view_task(tasks)
    task_del = int(input("Enter Which task do you want to delete :"))
    index = task_del -1
    del tasks[index]
    print("Task Deleted Successfully....!")


def main():
    tasks = []

    while True:
        print("===== TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice :")
        if choice == "1":
            view_task(tasks)
            #print("View tasks selected")
        elif choice == "2":
            add_task(tasks)
           # print("Add task selected")
        elif choice == "3":
            mark_done(tasks)
            #print("Mark done selected")
        elif choice == "4":
            delete_task(tasks)
            #print("Delete task selected")             
        elif choice == "5":
            print("Goodbye!")
            break 
        else:
            print("Invalid choice, try again")
main()            