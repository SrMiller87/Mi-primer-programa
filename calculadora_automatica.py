def menu(regresar_menu):
    user_action = input("Que operacion quieres realizar? [Sumar] / [Restar] / [Multiplicar] / [Dividir] : ").upper()
    accionar_menu = 0
    while accionar_menu <= 0:
        accionar_menu + 1
    while accionar_menu > 0:
        print("Volviendo al menu...")
        return user_action

while user_action == "SUMAR":
    primer_numero = int(input("Primer Numero: "))
    segundo_numero = int(input("Segundo Numero: "))
    if primer_numero and segundo_numero:
        print("El resultado de la Suma es: ")
        print(primer_numero + segundo_numero)

while user_action == "RESTAR":
    primer_numero = int(input("Primer Numero: "))
    segundo_numero = int(input("Segundo Numero: "))
    if primer_numero and segundo_numero:
        print("El resultado de la Resta es: ")
        print(primer_numero - segundo_numero)

while user_action == "MULTIPLICAR":
    primer_numero = int(input("Primer Numero: "))
    segundo_numero = int(input("Segundo Numero: "))
    if primer_numero and segundo_numero:
        print("El resultado de la Multiplicacion es: ")
        print(primer_numero * segundo_numero)

while user_action == "DIVIDIR":
    primer_numero = int(input("Primer Numero: "))
    segundo_numero = int(input("Segundo Numero: "))
    if primer_numero and segundo_numero:
        print("El resultado de la Division es: ")
        print(primer_numero / segundo_numero)

