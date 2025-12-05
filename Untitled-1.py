"""##INPUT para agregar de consola y 3 formas de printear
#saludo = input("Escribe un saludo: ")
#nombre = input("Tu nombre: ")
#edad = input("Tu edad: ")
#print (saludo + " Soy " + nombre + " tengo " + edad + " años")
#print (saludo, "Soy", nombre, ", tengo", edad, "años")
#print (f"{saludo} soy {nombre}, tengo {edad} años")"""

"""##Operaciones básicas
#a = float(input("Dame un numero: "))
#b = float(input("Otro numero: "))
#print(a+b)"""

"""##Par o Impar
#numero = int(input ("dame un num: "))
#resto = numero % 2
#if resto == 0:
#    print ("El numero ", numero, " es par")
#else:
#    print ("El numero ", numero, " es impar")"""

"""#Pide 3 números y muestra el mayor.
a = int(input("Num 1: "))
b = int(input("Num 2: "))
c = int(input("Num 3: "))
mayor = max(a,b,c)
print("el numero mas grande es ", mayor)"""

### CONDICIONALES Y BUCLES. FOR Y WHILE. FOR cuando tengo un rango, WHILE cuando no se cuántos bucles.
"""#While del 1 al 10
contador = 1
while contador <= 10:
    print(contador)
    contador += 1"""

"""#While sumar uno a uno hasta el 10
suma = 0
numero = 1
while numero <= 10:
    suma = suma + numero
    print(suma)
    numero += 1"""

"""#FOR I IN RANGE: Tabla de un numero
numero = int(input("Qué tabla queres ver: "))
for i in range(1,11):
    print(numero, "x", i, ":", numero*i)"""

"""#WHILE Adivina numero del 1 al 10
import random
from random import randint
numero = random.randint(1,10)
i = int(input("Adivina el numero: "))

while i != numero:
    if i < numero:
        i = int(input("es mas grande: "))
    else:
        i = int(input("es mas chico: "))
print ("Correcto! el numero es ", numero)"""

"""#Otra opcion de adivina numero
import random

numero = random.randint(1,10)
i = int(input("Adivina el numero: "))

while i != numero:
    if i < numero:
        i = int(input("Es más grande: "))
    else:
        i = int(input("Es más chico: "))

print("¡Correcto! El número es", numero)"""

"""#Pide una palabra y cuenta cuántas vocales tiene.
palabra = input("Escribe una palabra: ")
contador = 0
for letra in palabra:
    if letra.lower() in "aeiou": #.lower() se usa para que funcione igual con mayúsculas o minúsculas.
        contador += 1
print(f"La palabra tiene {contador} vocales.")"""

## LISTAS Y DICCIONARIOS

"""#Crea una lista vacía y deja que el usuario agregue productos hasta escribir "salir".
productos = []
while True:
    producto = input("escribe el producto o salir para terminar: ")
    if producto.lower() == "salir":
        break
    productos.append(producto)
print("Lista de productos: ", productos)"""

#Crea una lista con los números del 1 al 10 y muestra otra lista con sus cuadrados.