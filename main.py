
from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Enter your name: ")
print("Welcome back,", name)

admin_mode = input("Do you want to enter admin mode (yes/no)? ").lower()

if admin_mode == "yes":
    admin_password = input("Enter admin password: ")

    if admin_password == os.getenv("TASK_MANAGER_ADMIN_PASSWORD"):
        print("Admin mode activated!")
    else:
        print("Wrong password!")

tasks = load_tasks()

if tasks is None:
    tasks = []

count = int(input("How many tasks do you want to add? "))

for i in range(count):
    task_name = input("Enter a task: ")

    priority = input("Enter priority (low/medium/high): ").lower()

    while priority not in ["low", "medium", "high"]:
        print("Invalid priority!")
        priority = input("Enter priority (low/medium/high): ").lower()

    task = {
        "name": task_name,
        "priority": priority
    }

    tasks.append(task)

show_tasks(tasks)

print("total tasks:", len(tasks))
save_tasks(tasks)

