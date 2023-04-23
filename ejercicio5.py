##Dada una lista de números, imprimir el número más pequeño de la lista.

listNum = [1,21,2,3,5,66]
minNum = listNum [0]

for listNum in listNum:
    if listNum < minNum:
        minNum = listNum

print("El numero menor es: ", minNum)