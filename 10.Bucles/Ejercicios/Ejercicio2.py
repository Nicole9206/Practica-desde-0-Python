'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''

edad =  int(input("Digite su edad, para mostrar sus años: "))
i = 1 

while i <= edad: # != diferente de 
    print("Ha cumplido: {} años".format(i))
    i += 1