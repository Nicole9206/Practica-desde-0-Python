''' Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio'''


def areaCuadrado(base , altura):
    return base * altura 

print(areaCuadrado(10 , 10))


def areaCirculo(radio):
    area = (radio**2) * 3.14
    print(area)
areaCirculo(10)