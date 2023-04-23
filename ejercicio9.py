# Inicializar las variables para almacenar estadísticas
bebidas = {"cerveza": 0, "limonada": 0, "gaseosa": 0, "ninguno": 0}
mayor_importe = 0
edad_mayor_importe = 0
mayores_sin_bebida = 0

# Ingresar los datos de cada mesa
while True:
    # Leer los datos de la mesa actual
    nombre = input("Ingrese el nombre del cliente: ")
    while nombre.isdigit():
        nombre = input("Error: el nombre no puede ser un número. Ingrese nuevamente el nombre del cliente: ")
    edad = int(input("Ingrese la edad del cliente: "))
    bebida = input("Ingrese el tipo de bebida (cerveza, limonada, gaseosa o ninguno): ")
    while bebida.lower() not in ["cerveza", "limonada", "gaseosa", "ninguno"]:
        bebida = input("Error: el tipo de bebida ingresado no es válido. Ingrese nuevamente el tipo de bebida (cerveza, limonada, gaseosa o ninguno): ")
    comida = input("Ingrese el tipo de comida (papitas, hamburguesa, rabas o ninguno): ")
    while comida.lower() not in ["papitas", "hamburguesa", "rabas", "ninguno"]:
        comida = input("Error: el tipo de comida ingresado no es válido. Ingrese nuevamente el tipo de comida (papitas, hamburguesa, rabas o ninguno): ")
    importe = float(input("Ingrese el importe total: "))

    # Actualizar las estadísticas de la mesa actual
    bebidas[bebida] += 1
    if importe > mayor_importe:
        mayor_importe = importe
        edad_mayor_importe = edad
    if edad > 18 and bebida == "ninguno":
        mayores_sin_bebida += 1
    
    # Preguntar si se desea ingresar otra mesa
    respuesta = input("¿Desea ingresar otra mesa? (s/n): ")
    if respuesta.lower() != "s":
        break

# Imprimir las respuestas a las preguntas
print("Tipo de bebida más vendida:", max(bebidas, key=bebidas.get))
print("Edad del que pagó el importe más alto:", edad_mayor_importe)
print("Cantidad de mayores de 18 años que no pidieron bebida:", mayores_sin_bebida)
