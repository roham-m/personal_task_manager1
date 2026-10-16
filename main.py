from tasks import show_tasks
 
name = input("enter your name: ")
print("welcome ", name)
tasks = []
count = int(input("how many tasks do you want to add? :"))
for i in range(count):
    task = input("enter a task: ")
    tasks.append(task)

show_tasks(tasks)