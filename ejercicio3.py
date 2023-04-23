##Dado un número entero n, imprimir la secuencia de números pares menores o iguales a n.

def imprimir_numeros_pares(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

# Ejemplo de uso
numero = int(input("Ingrese un número entero: "))
print("La secuencia de números pares menores o iguales a", numero, "es:")
imprimir_numeros_pares(numero)
