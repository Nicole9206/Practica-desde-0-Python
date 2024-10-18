'''Crear un programa que pida al usuario una letra, 
y si es vocal, muestre el mensaje "Es vocal". Sino, 
decirle al usuario que no es vocal'''

vocal = input('Ingrese una vocal: ')

if vocal.lower() == "a":
    print("Es vocal")
elif vocal.lower() == "e":
    print("Es vocal")
elif vocal.lower() == "i":
   print("Es vocal")
elif vocal.lower() == "o":
   print("Es vocal")
elif vocal.lower() == "u":
    print("Es vocal")
else:
    print('No es vocal')