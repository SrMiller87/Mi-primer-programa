
pokemon_elegido = input("Contra quien quieres luchar? / (Squirtle), / (Charmander), / (Bulbasaur): ").upper()

vida_pikachu = 100
vida_enemigo = 0
daño_pokemon = 0
# SELECCION DE POKEMON / PICK THE POKEMON
if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    nombre_pokemon = "SQUIRTLE"
    daño_pokemon = 10

elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 100
    nombre_pokemon = "CHARMANDER"
    daño_pokemon = 15

elif pokemon_elegido == "BULBASAUR":
    vida_enemigo = 80
    nombre_pokemon = "BULBASAUR"
    daño_pokemon = 8
# ELECCION DE ATAQUE / PICK THE ATTACK
while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("Que ataque quieres utilizar? (Chispazo) / (Bola Voltio) :").upper()

    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10
    elif ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 15

    print("La vida del enemigo es ahora de {}".format(vida_enemigo))
# ATAQUE DEL POKEMON ENEMIGO / ENEMY POKEMON ATTACK
    if pokemon_elegido == "SQUIRTLE":
        vida_pikachu -= daño_pokemon
        print("{} ha usado pistola agua".format(nombre_pokemon))

    elif pokemon_elegido == "CHARMANDER":
        vida_pikachu -= daño_pokemon
        print("{} ha usado llamarada".format(nombre_pokemon))

    elif pokemon_elegido == "BULBASAUR":
        vida_pikachu -= daño_pokemon
        print("{} ha usado latigo cepa".format(nombre_pokemon))

    print("La vida del pikachu es ahora de {}".format(vida_pikachu))
# FIN DEL COMBATE MSG / END OF COMBAT MSG
if vida_enemigo <= 0:
    print("Has Ganado!!")
elif vida_pikachu <= 0:
    print("Has perdido :(")

print("El combate a terminado")