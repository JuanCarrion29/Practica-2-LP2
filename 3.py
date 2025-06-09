num = int(input("Ingrese un numero: "))

if num < 2:
    print("No es primo")
else:
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print("Es primo")
    else:
        print("No es primo")