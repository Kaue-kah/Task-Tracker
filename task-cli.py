import json
from datetime import datetime
import sys

try:
    with open("tasks.json", "r", encoding="utf-8") as arquivo:
        tasks = json.load(arquivo)
except FileNotFoundError:
    tasks = []

def save_tasks():
    with open("tasks.json", "w", encoding="utf-8") as arquivo:
        json.dump(tasks, arquivo, ensure_ascii=False, indent=4)

def add_task(nome: str):
    ultimo_id = tasks[-1]["id"] if tasks else 0
    task = {
        "id": ultimo_id + 1,
        "name": nome,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks()
    print(f"Task added successfully (ID: {ultimo_id + 1})")

def update_task(id: int, new_name: str):
    for task in tasks:
        if task["id"] == id:
            task["name"] = new_name
            task["updatedAt"] = datetime.now().isoformat()
            break
    save_tasks()

def change_status(id: int, status: str):
    for task in tasks:
        if task["id"] == id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            break
    save_tasks()

def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            break
    save_tasks()

def list_tasks():
    for task in tasks:
        print(f'{task["name"]} - ( ID: {task["id"]} )')

def list_done():    
    print("Done Tasks: ")
    i = 0
    for task in tasks:
        if task["status"] == "done":
            print(f'{i+1} - {task["name"]} - ( ID: {task["id"]} )')
            i += 1

def list_todo():
    print("Todo Tasks: ")
    i = 0
    for task in tasks:
        if task["status"] == "todo":
            print(f'{i+1} - {task["name"]} - ( ID: {task["id"]} )')
            i += 1

def list_inprogress():
    print("In progress Tasks: ")
    i = 0
    for task in tasks:
        if task["status"] == "in-progress":
            print(f'{i+1} - {task["name"]} - ( ID: {task["id"]} )')
            i += 1


args = sys.argv
if len(args) < 2:
    print("Comando inválido.")
    exit()

cmd = args[1]

if cmd == "add":
    add_task(args[2])

if cmd == "update":
    update_task(int(args[2]), args[3]) 

if cmd == "delete":
    delete_task(int(args[2]))          

if cmd == "mark-in-progress":
    change_status(int(args[2]), "in-progress") 

if cmd == "mark-done":
    change_status(int(args[2]), "done")       

if cmd == "list":
    if len(args) > 2:
        match args[2]:
            case "done":
                list_done()
            case "todo":
                list_todo()       
            case "in-progress":
                list_inprogress()  
            case _:
                print("Comando inválido!")
    else:
        list_tasks()              

        
        
#         import json
# from datetime import datetime
# import sys

# try:
#     with open("tasks.json", "r", encoding="utf-8") as arquivo:
#         tasks = json.load(arquivo)
# except FileNotFoundError:
#     tasks = []

# def save_tasks():
#     with open("tasks.json", "w", encoding="utf-8") as arquivo:
#         json.dump(tasks, arquivo, ensure_ascii=False, indent=4)

# def add_task(nome: str):
#     ultimo_id = tasks[-1]["id"] if tasks else 0
#     task = {
#         "id": ultimo_id + 1,
#         "name": nome,
#         "status": "todo",
#         "createdAt": datetime.now().isoformat(),
#         "updatedAt": datetime.now().isoformat()
#     }
#     tasks.append(task)
#     save_tasks()
#     print(f"Task added successfully (ID: {ultimo_id + 1})")

# def update_task(id: int, new_name: str):
#     for task in tasks:
#         if task["id"] == id:
#             task["name"] = new_name
#             task["updatedAt"] = datetime.now().isoformat()
#             save_tasks()
#             return
#     print(f"Task ID {id} não encontrada.")

# def change_status(id: int, status: str):
#     for task in tasks:
#         if task["id"] == id:
#             task["status"] = status
#             task["updatedAt"] = datetime.now().isoformat()
#             save_tasks()
#             return
#     print(f"Task ID {id} não encontrada.")

# def delete_task(id: int):
#     # ✅ busca pelo ID real, não pelo índice
#     for i, task in enumerate(tasks):
#         if task["id"] == id:
#             tasks.pop(i)
#             save_tasks()
#             return
#     print(f"Task ID {id} não encontrada.")

# def list_tasks():
#     for task in tasks:
#         print(f'{task["name"]} - ( ID: {task["id"]} )')  # ✅ "name" corrigido

# def list_done():
#     print("Done Tasks: ")
#     for i, task in enumerate(tasks):
#         if task["status"] == "done":
#             print(f'{i+1} - {task["name"]} - ( ID: {task["id"]} )')

# def list_todo():
#     print("Todo Tasks: ")
#     for i, task in enumerate(tasks):
#         if task["status"] == "todo":
#             print(f'{i+1} - {task["name"]} - ( ID: {task["id"]} )')

# def list_inprogress():
#     print("In progress Tasks: ")
#     for i, task in enumerate(tasks):
#         if task["status"] == "in-progress":
#             print(f'{i+1} - {task["name"]} - ( ID: {task["id"]} )')


# args = sys.argv
# if len(args) < 2:
#     print("Comando inválido.")
#     exit()

# cmd = args[1]

# if cmd == "add":
#     add_task(args[2])

# if cmd == "update":
#     update_task(int(args[2]), args[3])  # ✅ int()

# if cmd == "delete":
#     delete_task(int(args[2]))  # ✅ int()

# if cmd == "mark-in-progress":
#     change_status(int(args[2]), "in-progress")  # ✅ int()

# if cmd == "mark-done":
#     change_status(int(args[2]), "done")  # ✅ int()

# if cmd == "list":
#     if len(args) > 2:
#         match args[2]:
#             case "done":
#                 list_done()
#             case "todo":
#                 list_todo()       # ✅ era list_done
#             case "in-progress":
#                 list_inprogress() # ✅ parênteses adicionados
#             case _:
#                 print("Comando inválido!")
#     else:
#         list_tasks()  # ✅ parênteses adicionados