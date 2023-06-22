"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

#Creo fuera del primer ciclo, la variable notas, que me va a ser una lista que me va a almacenar las notas de cada una de las asignaturas. 
notas = [ ]

contador = 0

#En este primer for, recorri cada una de las asignaturas de la lista asignaturas:
for i in asignaturas:
    #Creo la variable nota que va a almacenar cada input en donde el usuario me va a dar la nota de cada materia en cada vuelta del ciclo:
    nota = int(input("Cuanta nota sacaste en " + i + ": "))
    #En cada vuelta del ciclo voy pasando el valor de nota a la lista vacia que esta afuera del ciclo for. Toma una nota, la pasa al ciclo y asi sucesivamente:
    notas.append(nota)

#Este segundo ciclo, lo inicio recorriendo la lista notas. Lista creada gracias al primer for:
for j in notas:
    #Creo la nueva variable asignatura_x, que me va a ir almacenando en cada vuelta el valor de cada una de las asignaturas. Esto se da porque coloco como parametro de asignatura el valor de la variable contador, que cree afuera del ciclo y que comienza en 0.: 
    asignatura_x = asignaturas[contador]
    #Aqui voy aumentando el valor del contador en 1. Para que en cada vuelta la variable asignatura_x pueda recorrer cada una de las asignaturas: 
    contador += 1
    #Imprimo el valor de asignatura_x en cada vuelta del ciclo mas el valor de j en cada vuelta del ciclo. 
    print("En" , asignatura_x, "has sacado:", j)

#Aprendizaje:
# Trata de mirarlo siempre desde los origenes de cada problema. Los fundamentos basicos de cada pedacito del planteamiento. Eso te ayuda a encontrar mas simplicidad en cada solucion. Parte el problema en pequenos problemas y trabajalos en etapas. 

    

