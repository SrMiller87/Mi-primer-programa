
#---------------------------------------MENU DEL PROGRAMA-------------------------------------------
print("---Si pulsa FIN se cerrara el programa automaticamente---")
user_action = input("Que operacion quieres realizar? [Sumar] / [Restar] / [Multiplicar] / [Dividir] : ").upper()

regresar_menu = input("Quiere salir del programa? (Si) (No) : ")

if regresar_menu == "Si":
    regresar_menu = True
    print("Saliendo...")
elif regresar_menu == "No":
    regresar_menu = False
    print("Continuamos pues")

if user_action == "FIN":
    print("El programa se cerrara")
#--------------------------------------FUNCIONES DEL PROGRAMA---------------------------------------
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
#---------------------------------------VARIABLES-------------------------------------------------

