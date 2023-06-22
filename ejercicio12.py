"""
Escribir un programa que almacene las matrices

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[-1, 0],
     [0, 1],
     [1, 1]]

en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.     
"""

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[-1, 0],
     [0, 1],
     [1, 1]]

a1 = A[0]
#a1 = [1,2,3]

a2 = A[1]
#a2 = [4,5,6]

b1 = [B[0][0], B[1][0], B[2][0]]
#b1 = [-1,0,1]

b2 = [B[0][1], B[1][1], B[2][1]]
#b2 = [0,1,1]

#multiplica a1 * b1 = valor1
#multiplica a1 * b2 = valor2
#multiplica a2 * b1 = valor3
#multiplica a2 * b2 = valor4

#Con un ciclo for para cada valor.

#MI IDEA: Crear 4 sub-listas, en cada sub-lista pongo 3 valores que son los que se van a a multiplicar entre si. Y por medio del ciclo for, se multiplica cada uno y el valor se almacena para crear la lista final que es el producto.

#Vamos con el primer valor. a1 * b1.
#a1 = [1,2,3]
#b1 = [-1,0,1]

contador = 0
valor_1 = []

for a in a1:
    x = a * b1[contador]
    contador += 1
    valor_1.append(x)
valor_1 = sum(valor_1)


#multiplica a1 * b2 = valor2
#a1 = [1,2,3]
#b2 = [0,1,1]

contador = 0
valor_2 = []

for a in a1:
    x = a * b2[contador]
    contador += 1
    valor_2.append(x)
valor_2 = sum(valor_2)



#multiplica a2 * b1 = valor3
#a2 = [4,5,6]
#b1 = [-1,0,1]

contador = 0
valor_3 = []

for a in a2:
    x = a * b1[contador]
    contador += 1
    valor_3.append(x)
valor_3 = sum(valor_3)



#multiplica a2 * b2 = valor4
#a2 = [4,5,6]
#b2 = [0,1,1]

contador = 0
valor_4 = []

for a in a2:
    x = a * b2[contador]
    contador += 1
    valor_4.append(x)
valor_4 = sum(valor_4)


total = [[valor_1, valor_2],[valor_3, valor_4]]
print(total)


#OPERACION:
#A.B celda1.1=(1 * -1)+(2 * 0)+(3 * 1)= -1+0+3= 2
#A.B celda2.1=(1 * 0)+(2 * 1)+(3 * 1)= 0+2+3= 5
#A.B celda1.2 =(4 * -1)+(5 * 0)+(6 * 1)= -4+0+6= 2
#A.B celda2.2 =(4 * 0)+(5 * 1)+(6 * 1)= 0+5+6= 11
# 2 5
# 2 11


#https://www.youtube.com/watch?v=pgqMaCQnWNc&list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz&index=65

#https://www.youtube.com/watch?v=eRBuGozq6Us