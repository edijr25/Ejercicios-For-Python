##Dada una lista de palabras, imprimir la palabra más larga de la lista.

listaPalabras = ["oso", "perro", "gato", "aleman", "venezuela"]
palabraLarge = listaPalabras[0]

for listaPalabras in listaPalabras:
    if len(listaPalabras)>len(palabraLarge):
        palabraLarge = listaPalabras
    
print("La palabra mas larga es: ", palabraLarge)