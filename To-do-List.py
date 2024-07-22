
def  show_task():
   print()
   if len(todos)<=0:
      print("No To-Tasks")
   for i,task in enumerate(todos ,start=1):
      print(i,task)
            
def  add_task():
   print()
   task=input("Enter New task.")
   todos.append(task)
   print(f"Task {task} Added")

def  Remove():
   print()
   for i,task in enumerate(todos ,start=1):
      print(i,task)
   num=int(input("Enter Number of Task to Remove"))
   if 1<=num<=len(todos):
      todos.pop(num-1)
      print("Task was Removed")
   else:
      print("Invalid Task Number")

todos=[]

while True:
 print("\nOptions:")
 print("1.Show task")
 print("2.Add New task")
 print("3.Remove")
 print("4.Exit")

 choose=input("Choose an option:")
 if choose=="1":
    show_task()

 elif choose=="2":
    add_task()

 elif choose=="3":
    Remove()

 elif choose=="4":
    break
 else:
    print("Invalid Option , Please Try Again")