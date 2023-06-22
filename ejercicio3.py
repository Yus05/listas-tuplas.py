"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""

"""
courses = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]


for note in courses:
    x = input("Cual ha sido tu nota en " + note + ": ")
    print("Tu nota en " + note + " fue de: " + x)
    
#En mi solucion: Por medio del ciclo for recorro cada una de las asignatura del curso para hacer la pregunta al usuario e inmediatamente imprimo la nota de la asignatura segun su respuesta. 
#Debia dar la impresion al final, despues de preguntar cada nota.    
"""


#ALF:
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])

#Declara la variable scores antes de comenzar el ciclo. 
#Recorre con el ciclo for cada asignatura. Crea dentro del ciclo una nueva variable en donde se va a almacenar cada una de las respuestas del usuario. 
#Por medio del metodo append, agrega a la variable que creo fuera del ciclo (scores) el valor de la nueva variable que almacena las respuesta del usuario (score).
#Aqui finaliza el primer ciclo for. En donde ya cada respuesta del usuario es almacenada y existe para cada asignatura.

#Entendiendo el segundo ciclo for: 
#for i in range(len(subjects)):
    #print("En " + subjects[i] + " has sacado " + scores[i])
# FUNCION LEN: Podemos conocer LA LONGITUD DE UNA LISTA
# FUNCION RANGE: Utilizando esta funcion seremos capaces de crear una secuencia de numeros enteros los cuales facilmente podemos iterar

#range(len(subjects)->El len(subjects) es: range(0, 5)
#Si es asi, entonces podria leerse: Para i, en el rango de 0 al 5, o sea en el rango de la longitud de la lista subjects que va del 0 al 5.
#------------------------------------------------------
"""
Explicacion video YT:
PRIMER FOR:
- Declaramos la varible scores como una lista vacia, porque aun no conocemos su valor.
- Inciamos el primer ciclo for, en donde vamos a iterar dentro de cada una de las materias del curso.
- En la variable score, vamos a almacenar de forma temporal las calificaciones que el usuario introduzca. Aca es donde se declara el input.
- Debemos guardar la variable score (que se esta sobreescribiendo cada vez que se ejecute el ciclo) en la variable scores. Lo hacemos por medio de la funcion append. scores.append(score) -> Entonces, en cada iteracion vamos a adjuntar el valor de score en scores.

SEGUNDO FOR:
- Ya tenemos adjuntadas las calificaciones en la lista, ahora debemos imprimir las materias y las calificaciones. Para hacer esto vamos a utilizar lo que es un range. 
- for i in range(len(subjects)): --> El iterardor i va a estar leyendo la funcion range, que va a tener como parametro de entrada o limite la longitud de nuestra lista, esta lista puede ser subjects o scores ya que miden exactamente lo mismo, usamos subjects. Lo que me arroja len(subjects) es la longitud, cuantos elementos tiene. 
- print("En " + subjects[i] + " has sacado " + scores[i]) --> Dice: En sibjects posicion 0 has sacado scores posicion 0... Y asi sucesivamente. Va iterando cada valor de i en cada vuelta de ciclo para cada lista.
"""








