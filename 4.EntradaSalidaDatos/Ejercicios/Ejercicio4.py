'''Hacer un programa que pida al usuario su nombre, su edad y su sexo 
y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>'''


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (f o m): ")

print( "Te llamas: ", nombre, "\nTu edad es: ", edad, "\nEres: ", sexo)

#Solución del profesor

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
sexo = input("Ingresa tu sexo (f o m): ")

print( "Te llamas: {}\nTu edad es: {}\nEres: {}" .format(nombre,edad,sexo))