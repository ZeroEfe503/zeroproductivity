import json
tasks = {}

# Funcion para agregar una tarea
def add_task ():
    name_task = input("nombre de la tarea: ")
    importance = int(input("Nivel de imporacia (1-5): "))
    complete = False
    new_task = {"Nombre" : name_task, "Importancia" : importance, "Estado": complete}
    count = len(tasks) + 1
    tasks.update({"Tarea " + str(count) : new_task})

# Funcion para ver las tareas
def view_tasks():
    for key, value in tasks.items():
        if not value["Estado"]:
            print(f'{key}: {value["Nombre"]} - Nivel de Importacia {value["Importancia"]} - Tarea no realizada')
        else:
            print(f'{key}: {value["Nombre"]} - Nivel de Importacia {value["Importancia"]} - Tarea realizada')

# Eliminar una tarea
def delete_task():
    for key, value in tasks.items():
        print(f'{key}: {value["Nombre"]}')
    task_del = input("Que tarea queires eliminar: ")
    if task_del in tasks:
        del tasks[task_del]
    else:
        print("La tarea no existe")

def complete_task():
    pass

def edit_task():
    pass

def fliter_tasks():
    pass

def save_task():
    with open("datos.txt", "w") as archivo:
        json.dump(tasks, archivo, indent=4)


def load_task():
    pass



add_task()
add_task()
view_tasks()
delete_task()
view_tasks()
