numeros = []
for i in range(4):
    num = int(input(f"Ingrese el numero {i+1}: "))
    numeros.append(num)

mayor = max(numeros)
posicion = numeros.index(mayor)

print(f"El mayor numero es {mayor} y está en la posición {posicion} de la lista.")