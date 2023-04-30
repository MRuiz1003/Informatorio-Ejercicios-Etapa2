numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(numero1, "es mayor que", numero2, "y", numero3)
elif numero2 > numero1 and numero2 > numero3:
    print(numero2, "es mayor que", numero1, "y", numero3)
elif numero3 > numero1 and numero3 > numero2: 
    print(numero3, "es mayor que", numero2, "y", numero1)
else:
    print("Los tres numeros son iguales")