'''Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa'''

tupla = ('a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'ñ', 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z')

OpcionMes = int(input("Ingrese el número de la letra del alfabeto: "))
OpcionMes -= 1

print("Tu letra es: ", tupla[OpcionMes])