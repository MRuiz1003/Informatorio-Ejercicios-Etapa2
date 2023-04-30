caracter = input("Ingrese un caracter: ")
if len(caracter) == 1:
    if caracter.isalpha():
        if caracter.isupper():
            print("El caracter es una letra mayuscula")
        else:
            print("El caracter es una letra minuscula")
    elif caracter.isnumeric():
        print("El caracter es un numero")
    else:
        print("El caracter es un caracter especial")
else:
    print("La cantidad de caracteres ingresada no es correcta, ingrese solo uno")