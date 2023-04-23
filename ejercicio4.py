##Dado un número entero n, imprimir la suma de los números impares menores o iguales a n.

def imprimir_numeros_impares(n):
    for i in range (1,n+1):
        if i %2 != 0:
            print (i)

numero = int(input("Ingrese un numero entero: "))
print ("La secuencia de numeros impares menores o iguales a", numero, "es: ")
imprimir_numeros_impares(numero)