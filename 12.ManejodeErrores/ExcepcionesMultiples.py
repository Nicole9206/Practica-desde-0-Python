while True:
    try:
        num1 = int(input("Ingrese un numero: "))
        resultado = 100 / num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

while True:
    try:
        edad= int(input("ingresa tu edad: "))
        print("Tu edad es: ",edad)
    #except ValueError:
        #print("Has colocado un valor errroneo")
    except KeyboardInterrupt:
        print("Has cancelado la ejecución")
        break
    