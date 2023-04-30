numero1 = float(input("Ingrese el primero numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
if numero1 > numero2:
    print(numero1, "es mayor que", numero2)
elif numero1 < numero2:
    print(numero2, "es mayor que", numero1)
else:
    print("Los dos numeros son iguales:", numero1)
