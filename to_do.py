import json
tasks = {}
task_counter = 0

# Funcion para agregar una tarea
def add_task ():
    global task_counter
    name_task = input("nombre de la tarea: ")
    importance = int(input("Nivel de imporacia (1-5): "))
    new_task = {"Nombre" : name_task, "Importancia" : importance, "Estado": False }
    task_counter += 1
    tasks.update({"Tarea " + str(task_counter) : new_task})

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

# Completar Tarea
def complete_task():
    for key, value in tasks.items():
        print(f'{key}: {value["Nombre"]}')
    task_complete = input("¿Que tarea completaste?: ")
    if task_complete in tasks:
        tasks[task_complete]["Estado"] = True
    else:
        print("La tarea no existe")
    
# def edit_task():
#    pass

# def fliter_tasks():
#    pass

# def save_task():
#    pass


# def load_task():
#    pass

while True:
    print("\n--- ZeroProductivity ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    
    option = input("Elige una opción: ")
    
    if option == "1":
        add_task()
    elif option == "2":
        view_tasks()
    elif option == "3":
        complete_task()
    elif option == "4":
        delete_task()
    elif option == "5":
        break
    else:
        print(f"{option} no es una opcion valida")