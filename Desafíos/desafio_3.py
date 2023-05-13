from random import randint
print("\nBienvenido al Juego de Adivinar el Número")
nombre_usuario = input("\nPor favor, ingrese su nombre: ")
numero_secreto = randint(1,100)
i = 8
print(f"\nBienvenido {nombre_usuario}, usted tiene 8 intentos para adivinar el número secreto entre 1 y 100.\n")
while i > 0:
    numero_usuario = input("Ingrese un número entero: ")
    if not numero_usuario.isdigit():
        print("Debe ingresar un número entero entre 1 y 100, vuelva a intentarlo.\n\n")
        continue
    numero_usuario = int(numero_usuario)
    if numero_usuario > numero_secreto:
        i -= 1
        print(f"El número secreto es menor, le quedan {i} intentos\n")
        
    elif numero_usuario < numero_secreto:
        i -= 1
        print(f"El número secreto es mayor, le quedan {i} intentos\n")
        
    else:
        print(f"""\nUsted ha adivinado el número secreto, FELICITACIONES
    Número secreto: {numero_secreto}
    Número de intentos: {9-i}
        
    FIN DEL JUEGO""")
        break
else:
    print(f"""Usted no ha adivinado el número secreto, vuelva a intentarlo
    Número secreto: {numero_secreto}
      
    FIN DEL JUEGO""")
    
