'''Escribir un programa que solicite al usuario un vocal en minuscula,
 y luego una letra en mayúsculas. El programa debe convertir la letra 
 en minúscula y la vocal en mayúscula, y al final, deben ser 
 concatenadas ambas'''


vocal = input("Ingrese una vocal en minuscula: ")
print(vocal.upper())

letra = input("Ingrese una letra en mayúscula: ")
print(letra.lower())

print (  letra.lower() , vocal.upper())

#Solucion profesor 
vocal = input("Ingrese una vocal en minuscula: ")

consonante = input("Ingrese una consonante en mayúscula: ")

vocal = vocal.upper()
consonante = consonante.lower()

print("La consonante fue : {} \nLa vocal fue: {}".format(consonante , vocal))