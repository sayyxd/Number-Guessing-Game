import json, os

FILE = "todos.json"

def load():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save(tasks):
    json.dump(tasks, open(FILE, "w"), indent=2)

tasks = load()
while True:
    print("\n1. Add  2. View  3. Done  4. Delete  5. Quit")
    choice = input("Choose: ")
    if choice == "1":
        tasks.append({"task": input("Task: "), "done": False})
    elif choice == "2":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. [{'x' if t['done'] else ' '}] {t['task']}")
    elif choice == "3":
        i = int(input("Task number: ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]["done"] = True
    elif choice == "4":
        i = int(input("Task number: ")) - 1
        if 0 <= i < len(tasks):
            tasks.pop(i)
    elif choice == "5":
        break
    save(tasks)
