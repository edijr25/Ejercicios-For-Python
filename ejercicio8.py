##Un bar nos contrato para administrar el consumo de los clientes en las distintas mesas del local
##para esto debemos desarrollar un algoritomo que nos permita el ingreso de los siguientes datos de varias mesas:
##Nombre del cliente (No puede ser numero)
#La edad
#Tipo de bebida (validar cerveza limonada, gaseosa, ninguno)
##Tipo de comida (Papitas, hamburguesa, rabas, ninguno)
#Importe total

##Necesatos saber: 
#tipo de bebida mas vendida
##la edad del que pago el importe mas alto
#cuanta gente mayor de 18 años no pidió bebida

#While --> Seguir
#nombre_cliente, edad_cliente, bebida, comida, importe
#contador por bebida
#flag edadMayor importeMayor
#contadorMayorSinBebida
#

cont_mayor_sin_bebida= 0
flag_mayor = False
cont_cerveza = 0
cont_limonada = 0
cont_gaseosa = 0
cont_ninguna = 0
importe_mayor = None
edad_mayor= None
seguir = "s"

while (seguir=="s"):
    nombre = input("Ingrese nombre: ")
    edad= int(input("Ingrese edad: "))
    while (edad <18):
        edad = int(input("Edad invalida. Reingrese edad: "))
    bebida = input("Ingrese la bebida: ")
    while (bebida != "cerveza" and bebida != "limonada" and bebida != "gaseosa" and bebida != "ninguna"):
        bebida = input("Bebida invalida, ingrese la bebida: ")
    comida = input("Ingrese la comida: ")
    while (comida != "papitas" and comida != "hamburguesas" and comida != "rabas" and comida != "ninguna"):
        comida = input("Comida invalida, ingrese la comida: ")
    importe = int(input("Importe total es: "))
    seguir = input("Quiere continuar?: (n/s)")



print("Fin del programa")
