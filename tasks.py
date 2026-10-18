import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def show_tasks(tasks):
    for task in tasks:
        print(task)

def save_tasks(tasks):
    with open("tasks.json", "w", indent = 2) as file:
        json.dump(tasks, file)