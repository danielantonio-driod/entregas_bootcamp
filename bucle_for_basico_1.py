# 1 imprime todos los números enteros del 0 al 100
print(" Ejercicio 1: Números del 0 al 100")
for i in range(101):
    print(i)

# 2 múltiplos de 2 entre 2 y 500
print("\n Ejercicio 2: Múltiplos de 2 entre 2 y 500")
for i in range(2, 501, 2):
    print(i)

# 3 contando Vanilla Ice
print("\n Ejercicio 3: Contando Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# 4 Wow. Número gigante a la vista
print("\n Ejercicio 4: Suma de números pares del 0 al 500000")
suma_pares = 0
for i in range(0, 500001, 2):
    suma_pares += i
print(f"Suma total de números pares entre 0 y 500000: {suma_pares}")

# 5 regrésame al 3
print("\n Ejercicio 5: Cuenta regresiva desde 2024 de 3 en 3")
for i in range(2024, -1, -3):
    print(i)

# 6 contador dinámico
print("\n Ejercicio 6: Contador dinámico con variables")
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
