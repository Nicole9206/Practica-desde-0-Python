'''Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla'''

tupla = ('enero' , 'febrero' , 'marzo' , 'abril' , 'mayo' , 'junio' , 'julio' , 'agosto' , 'septiembre' , 'octubre' , 'noviembre' , 'diciembre')

OpcionMes = int(input("Ingrese el número del mes: "))
OpcionMes -= 1

print("Tu mes es: ", tupla[OpcionMes])

