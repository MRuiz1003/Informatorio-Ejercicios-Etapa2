numero = int(input("Ingrese un numero entero: "))
if numero % 2 == 0 and numero % 3 == 0:
    print("El numero es multiplo de 2 y de 3")
elif numero % 2 == 0 and numero % 3 != 0:
    print("El numero es multiplo de 2 pero no es multiplo de 3")
elif numero % 2 != 0 and numero % 3 == 0:
    print("El numero es multiplo de 3 pero no es multiplo de 2")
else:
    print("El numero no es multiplo de 2 ni multiplo de 3")