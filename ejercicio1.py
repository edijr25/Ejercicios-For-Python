##Dada una lista de números, imprimir el número más grande de la lista.

numeros = [1,12,23,35,14,6]

numeroMax = numeros [0]

for numeros in numeros:
    if numeros >numeroMax:
        numeroMax = numeros

print("El numero mas grande es: ", numeroMax)