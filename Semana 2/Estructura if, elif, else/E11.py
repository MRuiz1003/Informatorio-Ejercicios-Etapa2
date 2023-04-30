numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("La suma de los dos numeros pares es", numero1 + numero2)
else:
    print("El/los numeros ingresados no son pares")