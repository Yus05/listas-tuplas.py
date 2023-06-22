"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

DEBO USAR EL CICLO FOR.
"""

vector_1 = [1,2,3]

vector_2 = [-1,0,2]

producto = []

contador = 0

for i in vector_1:
    x = i * vector_2[contador]
    contador += 1
    producto.append(x)


suma = 0

for e in producto:
    suma += e
#Tambien usando la funcion sum() 

print("El vector 1 es:",vector_1, "El vector 2 es:",vector_2,"\n""Y su producto escalar es:", suma)



