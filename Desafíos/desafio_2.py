print("\n\tANALIZADOR DE TEXTOS\n\n")

#Entradas
texto = input("Ingrese un texto para ser analizado: ").lower().strip()
letras = []
cantidad_letras = []



#Inciso 1
print("\n\nA continuacion debe ingresar tres letras: \n")

for i in range(3):
    letras.append(input(f"Ingrese la letra {i + 1}: ").lower())
    cantidad_letras.append(texto.count(letras[i]))
    
#Inciso 2
cantidad_palabras = len(texto.split(" "))

#Inciso 3
#Asignación de la última letra por si el texto termina en . o ,
if texto[-1] == "." or texto[-1] == ",":
    ultima_letra = texto[-2]
else:
    ultima_letra = texto[-1]
    
#Inciso 5
python_en_texto = {
    True: f"La palabra 'python' aparece " + str(texto.count("python")) + " veces en el texto.",
    False: "La palabra 'python' no aparece en el texto."
}

#Salidas

#1
print("\n\n1- Veces que aparece cada letra ingresada en el texto:\n")
print(f"""La letra '{letras[0]}' aparece {cantidad_letras[0]} veces.
La letra '{letras[1]}' aparece {cantidad_letras[1]} veces.
La letra '{letras[2]}' aparece {cantidad_letras[2]} veces.""")

#2
print("\n\n2- Cantidad de palabras del texto:\n")
print("Palabras totales: " + str(cantidad_palabras) + ".")

#3
print("\n\n3- Primer y última letra del texto:\n")
print(f"""La primer letra es '{texto[0]}'.
La ultima letra es '{ultima_letra}'.""")

#4
print("\n\n4- Texto dado vuelta:\n")
print(f"'{texto[::-1]}'")

#5
print("\n\n5- ¿La palabra 'python' aparece en el texto?:\n")
print(python_en_texto[texto.count("python") > 0])