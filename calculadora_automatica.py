
N1 = int(input("Escribe el primer numero: "))
N2 = int(input("Escribe el segundo numero: "))

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

Type = int(input("Elige una opción: "))

if Type == 1:
    print("El resultado es {}".format(N1 + N2))

if Type == 2:
    print("El resultado es {}".format(N1 - N2))

if Type == 3:
    print("El resultado es {}".format(N1 * N2))

if Type == 4:
    print("El resultado es {}".format(N1 / N2))
