'''Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares'''

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

for i in range(num1 , num2 + 1):
    if i % 2 == 0: # modulo 2 da un reciduo de 1 
        continue
    print(i)