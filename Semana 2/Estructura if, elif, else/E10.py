letra = input("Ingrese una letra: ").upper()
if letra.isalpha() and len(letra) == 1:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print("La letra es una vocal")
    else:
        print("La letra es una consonante")
else:
    print("El caracter ingresado no es una letra, intente nuevamente")