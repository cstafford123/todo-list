#to do list
#Nico Stafford
#period 4
#1/10/2024

#init
todo = []

#functions
def todolist ():
    menu = input ("Please pick an action")
    if (menu == "1"):
        task = input ("Please enter your task.")
        todo.insert (0,str(task))
        todolist()
    elif (menu == "2"):
        print (str(todo))
        todolist()
    elif (menu == "3"):
       complete = input("What task would you like to complete?(capitalize)")
       i = todo.index (complete)
       todo[i] = "☑ " + complete
       todolist()
    elif (menu == "4"):
        remove = input ("Which task would you like to remove?(capitalize)")
        todo.remove (str(remove))
        todolist()
    elif (menu == "5"):
        todo.clear()
        todolist()
    elif (menu == "6"):
        length = len(todo)
        print(length)
        todolist()
    elif (menu == "7"):
        todo.sort()
        todolist()
    
def runtodolist ():
    print ("Virtual To-Do List Menu")
    print ("1. Add task")
    print ("2. View to-do list")
    print ("3. Mark task as complete")
    print ("4. Remove task")
    print ("5. Clear list")
    print ("6. Print number of items on list")
    print ("7. Sort list alphabetically")
    print ("8. Exit")
    print ("To-Do:")   
    todolist()

#main
runtodolist()
