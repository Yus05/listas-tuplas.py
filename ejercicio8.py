"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""
#Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.

palabra = input("Escribe una palabra: ")

#Creo la variable lista que me va a almacenar en una lista cada una de las letras que va a tener la palabra que escribira el usuario:
lista = []


#Voy a recorrer letra por letra la palabra del ususario:
for l in palabra:
    #La variable valor va a almacenar cada letra en cada vuelta.
    valor = l
    #Envio cada uno de esos valores (cada letra) a la variable lista:
    lista.append(l)

#Pongo los valores de lista a la inversa.
lista = lista[::-1]

#Con el metodo join genero un string a partir de lista y guardo ese nuevo valor en la variable palabra, luego imprimo:
palabra = "".join(lista)
print(palabra)



