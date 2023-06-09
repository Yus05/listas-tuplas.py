"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

notas = [ ]

contador = -1


for i in asignaturas:
    nota = int(input("Nota de " + i + ": "))
#Con el metodo append, agrego nota a notas:
    notas.append(nota)
#Ya tengo la lista de las calificaciones y la lista de las asignaturas.

#En el proximo ciclo recorro cada una de las notas que dio el usuario:
for j in notas:
    #Cree la variable contado fuera del ciclo, para sumarle un valor dentro del ciclo, pero antes del if. Esto me permite tomar el valor nuevo que va a tener contador en cada iteracion para usarlo dentro del if: 
    contador += 1
    #Creo la condicion, si el valor de la nota es menor a cinco, imprime la asignatura segun el valor del contador que uso como parametro para saber que asignatura debe imprimir. El parametro contador me va a permitir que se imprima especificamente la asignatura que corresponde segun la vuelta del ciclo. 
    if j < 5:
        print("Debes volver a cursar:", asignaturas[contador])

#NOTA: El contador va a ir sumando un valor en cada vuelta. El resultado de esa suma va a representar el indice de cada uno de los elementos de la lista asignaturas y voy a poder usarlo para imprimir en especifico la materia que necesite segun la condicion del if. 
        

       
       
    
        



        
        




    





    

