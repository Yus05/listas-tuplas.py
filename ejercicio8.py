"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""
#Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.

palabra = input("Escribe una palabra: ")

lista = []

for l in palabra:
    valor = l
    lista.append(l)

lista = lista[::-1]

palabra = "".join(lista)
print(palabra)

#LUNES: Analiza este ejercicio y escribe que hiciste en cada paso. Piensa si cumples con la propuesta del ejercicio. Y tambien explicate de nuevo, por que no te funcionaba el metodo split. 

