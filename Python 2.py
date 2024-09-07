
    # #escape sequence

# str1= "This is Yash's notepad. He uses a pen"   #will print in the same line
# print(str1)

# str2= "This is Yash's notepad. \nHe uses a pen"   # \n will print in the next line
# print(str2)

# str3= "This is Yash's notepad.\t He uses a pen"    # \t will print with a tab space
# print(str3)

    # #indexing

# name = "YASH RAVAL"   
# print(name[7])

    # #slicing

# name = "YASH RAVAL"
# # print (name[2:5])   #character at index 5 not included (ending index not included)
# print(name[2:])     #same as [2:len(name)]
# print(name[ :7])    #same as [0:7]
# print(name[-6:-1])   #negative indexing

    # #some string functions

name = "i work as a Product manager in an IT company"
print(name.count("o"))    #count the number of o in the string
name = name.capitalize()  #will capitalize the 1st character(0th index)
print(name)
print(name.replace("as", "AS"))   #will replace the string
print(name.find("p"))     #will return the index of the character in ""

# Initialize an empty list to store tasks
tasks = []

# Function to display the list of tasks
def show_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f'"{task}" has been added to your to-do list.')

# Function to delete a task
def delete_task():
    show_tasks()
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        removed_task = tasks.pop(task_number)
        print(f'"{removed_task}" has been removed from your to-do list.')
    except (IndexError, ValueError):
        print("Invalid task number. Please try again.")

# Function to show the menu options
def show_menu():
    print("\nChoose an option:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
