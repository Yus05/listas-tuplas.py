"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""
#Almacene los valores en la lista:
numeros = [1,2,3,4,5,6,7,8,9,10]

#Ordene los valores de la lista de manera descendete:
numeros.sort(reverse=True)

#Recorro cada uno de los elementos de la lista y los convierto en str, para imprimirlos.
for i in numeros:
    numeros_str = str(i)
    print(numeros_str, end=",")


