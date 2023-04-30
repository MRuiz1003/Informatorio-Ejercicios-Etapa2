palabra = input("Ingrese una palabra: ")
cantidad = palabra.upper().count("A")
if cantidad > 0:
    print("La palabra contiene la letra 'a'\nCantidad:", cantidad)
else: 
    print("La palabra no contiene la letra 'a'")