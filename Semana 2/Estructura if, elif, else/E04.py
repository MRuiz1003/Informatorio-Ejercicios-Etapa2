nota = int(input("Ingrese una nota del 0 al 10: "))
if nota >= 0 and nota <= 10:
    if nota >= 5:
        print("El alumno esta aprobado con una nota de", nota)
    else:
        print("El alumno esta desaprobado con una nota de", nota)
else:
    print("La nota ingresada no es valida, intentelo nuevamente")