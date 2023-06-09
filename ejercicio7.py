"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

#En esta sub lista cree la lista de las letras que debo eliminar:
abc_x = abc[2::3] #Letras a eliminar


#En este for recorro cada letra del abc, y a su vez cada letra del abc_x. La condicion, si valor y letra coinciden, remueve ese valor de abc. Ya quedan eliminados los valores de abc_x en abc, y si vuelvo a imprimir abc FUERA del ciclo, me imprime el abc sin esos valores.
for letra in abc:
    for valor in abc_x:
        if valor == letra:
            abc.remove(valor)
print(abc)


    





    
    

        

    
        



