import json
from datetime import datetime
import sys

try:
    with open("task-list.json", "r", encoding="utf-8") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []
except json.JSONDecodeError:
    tasks = []

def w_json():
    with open("task-list.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)  
        

def add(description: str):
    n = len(tasks) 
    max_id = max((task["id"] for task in tasks), default= 0) + 1
    task = {
        "id": max_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
        
    tasks.append(task)
    
    w_json()
    print(f"Task added successfully (ID: {max_id})")


def update(id: int, new_description: str):
    for task in tasks:
        if task["id"] == id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
    
    w_json()


def delete_task(id: int):
    for i, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(i) 
            w_json()
            return
            
    print("ID not found.")  
    

def change_status(id: int, status: str):
    for task in tasks:
        if task["id"] == id:
            task["status"] = status

    w_json()


def list__all_tasks():
    print("Task list:")
    for task in tasks:
        print(f'{task["id"]} - Description: {task["description"]} - Status: {task["status"]}')
        
        
def list_tasks(status: str):
    print(f"{status} list:")
    for task in tasks:
        if task["status"] == status:
            print(f'{task["id"]} - Description: {task["description"]}')
            

args = sys.argv


if len(args)<2:
    print("Invalid")
    exit()
    
try:
    if args[1] == "update":
        update(int(args[2]), args[3])
        print("Updated successfully.")  
                
    elif args[1] == "add":
        add(args[2])

    elif args[1] == "delete":
        delete_task(int(args[2]))
        print("Deleted successfully")
        
    elif args[1] == "mark-in-progress":
        change_status(int(args[2]), "in-progress")
        print("Successfully changed.")
        
    elif args[1] == "mark-done":
        change_status(int(args[2]), "done")
        print("Successfully changed.")
        
    elif args[1] == "list":
        if len(args) == 2:
            list__all_tasks()
        if len(args) > 2:
            list_tasks(args[2])

    else:
        print("Invalid cmd")

except IndexError:
    print("Error: missing arguments.")
except ValueError:
    print("Error: ID must be a number.")
    
