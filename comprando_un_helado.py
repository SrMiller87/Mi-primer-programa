
apetece_helado_input = input("Te apetece un helado? (Si / No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print ("Te he dicho que dijeras Si o No, asi que lo tomare como un no")
    apetece_helado = False



tiene_dinero_input = input("Tienes dinero para un helado? (Si / No): ").upper()
esta_el_heladero_input = input("Esta el señor que vende helados? (Si / No): ").upper()
esta_tu_tia_input = input("Estas con tu tia? (Si / No): ").upper()

apetece_helado = apetece_helado_input == "SI"
tiene_dinero = tiene_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_el_heladero = esta_el_heladero_input == "SI"

if apetece_helado and tiene_dinero and esta_el_heladero:
    print("Pues comete un helado")
else:
    print("Pues entonces nada")

