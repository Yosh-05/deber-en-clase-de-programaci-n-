def presentacion():
    print("************************************************")
    print("****************** JUJAM PET *******************")
    print("************************************************")
    print("***************** BIENVENIDO *******************")
    print("************************************************")
    print("IMPORTANTE: Para seleccionar las opciones use números.")
def datos_cliente():
    nombre = input("Ingrese su nombre: ")
    cdi = input("Ingrese su cédula: ")
    return nombre, cdi
def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Alimento para mascotas")
    print("2. Juguetes y accesorios")
    print("3. Servicio de baño pet")
    print("4. Finalizar compra")
    print("5. Salir")
    return input("Seleccione una opción: ")
def comida_perros(compra, total, salir):
    while True:
        print("------ COMIDA PARA PERROS ------")
        print("1. Dog Chow - $15")
        print("2. Pedigree - $18")
        print("3. Pro Plan - $25")
        print("4. Royal Canin - $30")
        print("5. Regresar")
        print("6. Salir")
        op = input("Seleccione: ")
        if op == "1":
            compra += "Dog Chow - $15 " 
            total += 15
        elif op == "2":
            compra += "Pedigree - $18 "   
            total += 18
        elif op == "3":
            compra += "Pro Plan - $25 "   
            total += 25
        elif op == "4":
            compra += "Royal Canin - $30 " 
            total += 30
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir == True:
            break
    return compra, total, salir
def comida_gatos(compra, total, salir):
    while True:
        print("------ COMIDA PARA GATOS ------")
        print("1. Whiskas - $10")
        print("2. Cat Chow - $14")
        print("3. Pro Plan Gatos - $22")
        print("4. Royal Canin Gatos - $28")
        print("5. Regresar")
        print("6. Salir")
        op = input("Seleccione: ")
        if op == "1":
            compra += "Whiskas - $10 "
            total += 10
        elif op == "2":
            compra += "Cat Chow - $14 "
            total += 14
        elif op == "3":
            compra += "Pro Plan Gatos - $22 "
            total += 22
        elif op == "4":
            compra += "Royal Canin Gatos - $28 "
            total += 28
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir == True:
            break
    return compra, total, salir
def comida_peces(compra, total, salir):
    while True:
        print("------ COMIDA PARA PECES ------")
        print("1. Tetramin - $5")
        print("2. Nutrafin - $7")
        print("3. Sera Vipan - $9")
        print("4. Tetra Goldfish - $11")
        print("5. Regresar")
        print("6. Salir")
        op = input("Seleccione: ")
        if op == "1":
            compra += "Tetramin - $5 "
            total += 5
        elif op == "2":
            compra += "Nutrafin - $7 "
            total += 7
        elif op == "3":
            compra += "Sera Vipan - $9 "
            total += 9
        elif op == "4":
            compra += "Tetra Goldfish - $11 "
            total += 11
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir == True:
            break
    return compra, total, salir
def comida_aves(compra, total, salir):
    while True:
        print("------ COMIDA PARA AVES ------")
        print("1. Semillas Premium - $7")
        print("2. Vitakraft - $10")
        print("3. Kaytee - $13")
        print("4. ZuPreem - $16")
        print("5. Regresar")
        print("6. Salir")
        op = input("Seleccione: ")
        if op == "1":
            compra += "Semillas Premium - $7 "
            total += 7
        elif op == "2":
            compra += "Vitakraft - $10 "
            total += 10
        elif op == "3":
            compra += "Kaytee - $13 "
            total += 13
        elif op == "4":
            compra += "ZuPreem - $16 "
            total += 16
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir == True:
            break
    return compra, total, salir
def menu_alimentos(compra, total, salir):
    while True:
        print("========= ALIMENTOS =========")
        print("1. Comida para perros")
        print("2. Comida para gatos")
        print("3. Comida para peces")
        print("4. Comida para aves")
        print("5. Regresar")
        print("6. Salir")
        smenu = input("Seleccione: ")
        if smenu == "1":
            compra, total, salir = comida_perros(compra, total, salir)
        elif smenu == "2":
            compra, total, salir = comida_gatos(compra, total, salir)
        elif smenu == "3":
            compra, total, salir = comida_peces(compra, total, salir)
        elif smenu == "4":
            compra, total, salir = comida_aves(compra, total, salir)
        elif smenu == "5":
            break
        elif smenu == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir == True:
            break
    return compra, total, salir
def accesorios_perros(compra, total, salir):
    while True:
        print("------ Accesorios para perros ------")
        print("1. Juguete mordedor - $1.99")
        print("2. Correa - $5")
        print("3. Cama - $20")
        print("4. Plato - $8")
        print("5. Regresar")
        print("6. Salir")
        op = input("Seleccione: ")
        if op == "1":
            compra += "Juguete mordedor - $1.99 "
            total += 1.99
        elif op == "2":
            compra += "Correa - $5 "
            total += 5
        elif op == "3":
            compra += "Cama - $20 "
            total += 20
        elif op == "4":
            compra += "Plato - $8 "
            total += 8
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir == True:
            break
    return compra, total, salir
def accesorios_gatos(compra, total, salir):
    while True:
        print("------ Accesorios para gatos ------")
        print("1. Collar - $1.99")
        print("2. Rascador - $15")
        print("3. Cama - $18")
        print("4. Juguete con plumas - $6")
        print("5. Regresar")
        print("6. Salir")
        op = input("Seleccione: ")
        if op == "1":
            compra += "Collar gato - $1.99 "
            total += 1.99
        elif op == "2":
            compra += "Rascador - $15 "
            total += 15
        elif op == "3":
            compra += "Cama gato - $18 "
            total += 18
        elif op == "4":
            compra += "Juguete plumas - $6 "
            total += 6
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir == True:
            break
    return compra, total, salir
def accesorios_peces(compra, total, salir):
    while True:
        print("------ Accesorios para peces ------")
        print("1. Tunnel - $3.50")
        print("2. Pecera - $25")
        print("3. Filtro - $12")
        print("4. Decoración - $9")
        print("5. Regresar")
        print("6. Salir")
        op = input("Seleccione: ")
        if op == "1":
            compra += "Tunnel peces - $3.50 "
            total += 3.50
        elif op == "2":
            compra += "Pecera - $25 "
            total += 25
        elif op == "3":
            compra += "Filtro - $12 "
            total += 12
        elif op == "4":
            compra += "Decoración - $9 "
            total += 9
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir == True:
            break
    return compra, total, salir
def accesorios_aves(compra, total, salir):
    while True:
        print("------ Accesorios para aves ------")
        print("1. Juguete espejo - $4.99")
        print("2. Jaula - $30")
        print("3. Comedero - $7")
        print("4. Campana - $5")
        print("5. Regresar")
        print("6. Salir")
        op = input("Seleccione: ")
        if op == "1":
            compra += "Juguete espejo - $4.99 "
            total += 4.99
        elif op == "2":
            compra += "Jaula - $30 "
            total += 30
        elif op == "3":
            compra += "Comedero - $7 "
            total += 7
        elif op == "4":
            compra += "Campana - $5 "
            total += 5
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir == True:
            break
    return compra, total, salir
def juguetes(compra, total, salir):
    while True:
        print("======= JUGUETES Y ACCESORIOS =======")
        print("1. Accesorios para perros")
        print("2. Accesorios para gatos")
        print("3. Accesorios para peces")
        print("4. Accesorios para aves")
        print("5. Regresar")
        print("6. Salir")
        smenu = input("Seleccione: ")
        if smenu == "1":
            compra, total, salir = accesorios_perros(compra, total, salir)
        elif smenu == "2":
            compra, total, salir = accesorios_gatos(compra, total, salir)
        elif smenu == "3":
            compra, total, salir = accesorios_peces(compra, total, salir)
        elif smenu == "4":
            compra, total, salir = accesorios_aves(compra, total, salir)
        elif smenu == "5":
            break
        elif smenu == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir == True:
            break
    return compra, total, salir
def resumen_compra(nombre, cdi, compra, total):
    print("========================================")
    print("          RESUMEN DE COMPRA")
    print("========================================")
    print("Cliente:", nombre)
    print("Cédula:", cdi)
    print("----------------------------------------")
    print("Productos seleccionados:")
    print(compra)
    print("----------------------------------------")
    print(f"TOTAL A PAGAR: ${total:}")
    print("Gracias por visitar JUJAM PET :D")
    print("========================================")
presentacion()
nombre, cdi = datos_cliente()
total = 0
compra = ""
salir = False
while salir == False:
    menu = menu_principal()
    if menu == "1":
        compra, total, salir = menu_alimentos(compra, total, salir)
    elif menu == "2":
        compra, total, salir = juguetes(compra, total, salir)
    elif menu == "3":
        print("Servicio de baño agregado.")
        compra += "Servicio de baño pet - $8 "  
        total += 8
    elif menu == "4":
        break
    elif menu == "5":
        salir = True
    else:
        print("Opción inválida.")
if total > 0:
    resumen_compra(nombre, cdi, compra, total)
else:
    print("Gracias por visitarnos, te esperamos :D")
