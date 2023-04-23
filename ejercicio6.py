##Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.

def contar_vocales (listPalabras):
    vocales = ['a','e','i','o','u']
    totalVocales = 0
    for listPalabras in listPalabras:
        for letra in listPalabras:
            if letra.lower() in vocales:
                totalVocales += 1
    return totalVocales


listPalabras = ["Norma", "Edicilio","Avion", "Sancristobal"]
totalvocales = contar_vocales(listPalabras)
print("La cantidad total de vocales en la lista de palabras es: ", totalvocales)