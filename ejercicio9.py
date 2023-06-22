"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""

palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for v in vocales: 
    contador = 0
    for p in palabra: 
        if p == v:
            contador += 1
    print(v,contador)
    #print("La vocal " + v + " aparece " + str(contador) + " veces")

"""
ANALISIS CON LA PALABRA: podadora.
- Recorre todas las vocales.
- Crea el contador.
- Recorre todas las letras de la palabra.
- Con podadora. Por empezar los ciclo recorriendo las vocales, este es el punto de partida, ellas son las que dan referencia. Entonces, toma la letra a, recorre la palabra y va sumando un uno cada vez que la encuentra, sale de ese segundo, entra al otro ciclo con su valor de contador e imprime lo que contiene el primer ciclo mas el "nuevo" valor del contador.  // Ahora va con la letra e, recorre la palabra y hace la sumatoria si la encuentra, sino la encuentra no le suma al cero, vuelve a salir del ciclo e imprime ese valor. // Ahora va con la letra i, recorre y si la encuentra le suma 1, sino no suma. Sale del ciclo e imprime ese valor. // Va con la o, la encuentra en cada vuelta 2 veces, por lo tanto suma un 1 dos veces, tiene ese nuevo valor. Se sale de ese ciclo, entra en el primero con un nuevo valor de contador, y hace la impresion correspondiente. 

EN DONDE ESTUVIERON MIS ERRORES? 
-> Mis debilidades estan en entender el orden de cada ciclo, si poner un for de primero o uno de segundo, que rol ocupa cada uno en el resto del codigo. Y tambien, entender la funcion que cumple el print segun la indentacion. 

"""










#-> Para cada letra de las vocales / Se crea la variable contador. 
#-> Para cada letra de la palabra / Si la letra de la palabra es igual a la letra de la vocal / Sumale al contador un 1. Listo, ahi queda ese ciclo, ahora contador vale un numero mas. 
#-> Fuera del segundo ciclo, en el ciclo en donde me recorre todas las vocales y me crea la variable contador, imprime la vocal y el nuevo valor de contador. 












































"""for p in palabra:
    contador = 0
    for v in vocales:
        if p == v:
            contador += 1
            print(p,contador)

#-> Para cada letra de palabra. Crea la varible contador.
#-> Para cada vocal.
#-> Si la letra de la palabra es igual a la vocal, suma 1 al contador, imprime esa letra y la suma del contador. Por esto es que siempre me da uno el contador, porque apenas encuentra la igualdad, hace la suma. Asi no funciona.""" 













# OJO : CONCENTRATE, RESPIRA Y ENFOCATE MENTALMENTE SOLO ACA. CONCENTRA TU ENERGIA EN EL TRABAJO QUE ESTAS REALIZANDO.

#Aprendi que puedo meter el contador en el ciclo.



            
            


            
            








