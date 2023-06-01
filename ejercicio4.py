"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""
#Cree el input de entrada de datos, lo mantuve como string:
ganadores = input("Escribe los numeros ganadores separados por ','': ")

#Converti los numeros que me dieron por medio del input en una lista:
ganadores = ganadores.split(",")

#Ordene la lista de forma ascendente:
ganadores.sort()

#Recorro con el ciclo for cada uno de los elementos de la lista e imprimo: 
for i in ganadores:
    print(i)





