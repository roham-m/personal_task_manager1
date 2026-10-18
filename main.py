from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv
import os


load_dotenv()

name = input("enter your name: ")
print("welcome", name)

admin_mode = input("do you want to enter admin mode (yes/no)?   ")

if admin_mode == "yes":
    admin_password = input("enter admin password: ")
    if admin_password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode activated")

    else:
        print("wrong password!!!")




tasks = load_tasks()

count = int(input("how many tasks do you want to add? : "))

for i in range(count):
    task = input("enter a task: ")
    tasks.append(task)

show_tasks(tasks)
save_tasks(tasks)