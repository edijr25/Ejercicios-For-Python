def contadorNegativos(lista):
    contador = 0
    for num in lista:
        if num<0:
            contador+= 1
    return contador

lista = [4,-8,9,-9,-10,-12]
cantidadNegativos = contadorNegativos(lista)
print("La cantidad de negativos es: ", cantidadNegativos)