# Definir la lista de estudiantes
"""estudiantes = [
    [101, 'Ana María Fernández', 88.5],
    [102, 'Luis Miguel Pérez', 92.0],
    [103, 'Pedro Sánchez', 85.0],
    [104, 'María José González', 90.5],
    [105, 'Ana Fernández', 87.0],  # Nombre repetido con promedio diferente
    [106, 'Luis Pérez', 87.0]  # Nombre repetido con promedio diferente
]

# Recortar los nombres a un máximo de 12 caracteres
estudiantes_recortados = [[id, nombre[:12], promedio] for id, nombre, promedio in estudiantes]

# Ordenar la lista por promedio (descendente) y luego por nombre (ascendente)
estudiantes_ordenados = sorted(estudiantes_recortados, key=lambda x: (-x[2], x[1]))

# Imprimir la lista ordenada con formato de f-strings
print(f"{'ID':>4} {'Nombre':<12} {'Promedio':>10}")
print('-' * 26)
for id, nombre, promedio in estudiantes_ordenados:
    print(f"{id:>4} {nombre:<12} {promedio:>10.2f}")"""






# Definir la lista de películas
peliculas = [
    [101, 'Barbie', 9.2],
    [102, 'Como entrenar a tu dragon', 10.0],
    [103, 'Moana', 9.0],
    [104, 'Cars', 9.9],
    [105, 'Como entrenar a tu dragon II', 9.8],  # Título repetido con calificación diferente
    [106, 'Cars II', 8.7]  # Título repetido con calificación diferente
]

# Recortar los títulos a un máximo de 15 caracteres
peliculas_recortadas = [[id, titulo[:15], calificacion] for id, titulo, calificacion in peliculas]

# Ordenar la lista por calificación (descendente) y luego por título (ascendente)
peliculas_ordenadas = sorted(peliculas_recortadas, key=lambda x: (-x[2], x[1]))

# Imprimir la lista ordenada con formato de f-strings
print(f"{'ID':>4} {'Título':<15} {'Calificación':>12}")
print('-' * 33)
for id, titulo, calificacion in peliculas_ordenadas:
    print(f"{id:>4} {titulo:<15} {calificacion:>12.1f}")
