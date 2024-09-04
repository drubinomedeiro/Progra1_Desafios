def crear_contenido(contenido, proximo_id, titulo, tipo, genero, año, duracion):
    item = {
        'id': proximo_id,
        'titulo': titulo,
        'tipo': tipo,  # Puede ser 'Película' o 'Serie'
        'genero': genero,
        'año': año,
        'duracion': duracion
    }

    contenido.append(item)
    print(f"La {tipo} '{titulo}' creada con ID {item['id']}.")

    return proximo_id + 1

def leer_contenido(contenido):
    if not contenido:
        print("No hay contenido registrado.")
        return
    for item in contenido:
        print(f"ID: {item['id']}, Título: {item['titulo']}, Tipo: {item['tipo']}, Género: {item['genero']}, Año: {item['año']}, Duración: {item['duracion']}")

def actualizar_contenido(contenido, item_id, titulo=None, tipo=None, genero=None, año=None, duracion=None):
    for item in contenido:
        if item['id'] == item_id:
            item['titulo'] = titulo if titulo is not None and titulo != '' else item['titulo']
            item['tipo'] = tipo if tipo is not None and tipo != '' else item['tipo']
            item['genero'] = genero if genero is not None and genero != '' else item['genero']
            item['año'] = año if año is not None else item['año']
            item['duracion'] = duracion if duracion is not None and duracion != '' else item['duracion']
            print(f"{item['tipo']} con ID {item_id} actualizada.")
            return
    print(f"No se encontró el contenido con ID {item_id}.")

def eliminar_contenido(contenido, item_id):
    for item in contenido:
        if item['id'] == item_id:
            contenido.remove(item)
            print(f"El {item['tipo']} con ID {item_id} ha sido eliminado.")
            return
    print(f"No se encontró el contenido con ID {item_id}.")


contenido = []
proximo_id = 1
continuar = 0

while continuar == 0:
    titulo = input("Ingrese el nombre de la película/serie: ")
    tipo = input("Indique si es una serie o película: ")
    genero = input("Indique el género: ")
    año = int(input("Indique su año de estreno: "))
    duracion = input("Indique la duración: ")

    proximo_id = crear_contenido(contenido, proximo_id, titulo, tipo, genero, año, duracion)
    
    continuar = int(input("Si desea continuar ingresando contenido ingrese 0, si desea finalizar el proceso, indique -1: "))
    
    if continuar == -1:
        continuar = -1

print("\nContenido registrado:")
leer_contenido(contenido)

# Preguntar si se desea actualizar contenido
actualizar_opcion = input("\n¿Desea actualizar contenido? (s/n): ").lower()

while actualizar_opcion == 's':
    print("\nActualizar contenido:")

    nuevo_id = int(input("Ingrese el ID de la película/serie a cambiar: "))
    print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")

    nuevo_titulo = input("Nuevo título (deje en blanco para no cambiar): ")
    nuevo_tipo = input("Nuevo tipo (deje en blanco para no cambiar): ")
    nuevo_genero = input("Nuevo género (deje en blanco para no cambiar): ")
    nuevo_año_str = input("Nuevo año (deje en blanco para no cambiar): ")
    nuevo_duracion = input("Nueva duración (deje en blanco para no cambiar): ")

    # Convertir nuevo año a entero si no está vacío
    nuevo_año = int(nuevo_año_str) if nuevo_año_str else None

    actualizar_contenido(contenido, nuevo_id, titulo=nuevo_titulo, tipo=nuevo_tipo, genero=nuevo_genero, año=nuevo_año, duracion=nuevo_duracion)

    print("\nContenido actualizado:")
    leer_contenido(contenido)
    
    # Preguntar si se desea seguir actualizando
    actualizar_opcion = input("\n¿Desea seguir actualizando contenido? (s/n): ").lower()

# Preguntar si se desea eliminar contenido
eliminar_opcion = input("\n¿Desea eliminar contenido? (s/n): ").lower()

while eliminar_opcion == 's':
    print("\nEliminar contenido:")

    eliminar_id = int(input("Ingrese el ID de la película/serie a eliminar: "))
    eliminar_contenido(contenido, eliminar_id)

    print("\nContenido después de la eliminación:")
    leer_contenido(contenido)
    
    # Preguntar si se desea seguir eliminando
    eliminar_opcion = input("\n¿Desea seguir eliminando contenido? (s/n): ").lower()

print("\nProceso finalizado.")