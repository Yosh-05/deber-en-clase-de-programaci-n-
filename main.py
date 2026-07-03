def mostrar_encabezado():
    print("************************************************")
    print("****************** JUJAM PET *******************")
    print("************************************************")
    print("***************** BIENVENIDO *******************")
    print("***********************************************")
    print("IMPORTANTE: Para seleccionar las opciones use números.")

def obtener_datos_cliente():
    nombre = input("Ingrese su nombre: ")
    cdi = input("Ingrese su cédula: ")
    return nombre, cdi

def mostrar_menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Alimento para mascotas")
    print("2. Juguetes y accesorios")
    print("3. Servicio de baño pet")
    print("4. Finalizar compra")
    print("5. Salir")
    return input("Seleccione una opción: ")

def mostrar_submenu_alimentos():
    print("========= ALIMENTOS =========")
    print("1. Comida para perros")
    print("2. Comida para gatos")
    print("3. Comida para peces")
    print("4. Comida para aves")
    print("5. Regresar")
    print("6. Salir")
    return input("Seleccione: ")

def mostrar_productos(titulo, productos):
    print(f"------ {titulo} ------")
    for i, (nombre, precio) in enumerate(productos, 1):
        print(f"{i}. {nombre} - ${precio}")
    print("5. Regresar")
    print("6. Salir")
    return input("Seleccione: ")

def procesar_producto(compra, total, productos, opcion):
    if opcion in productos:
        idx = int(opcion) - 1
        nombre, precio = productos[idx]
        compra += f"{nombre} - ${precio} "
        total += precio
    return compra, total

def menu_alimentos(compra, total, salir):
    while True:
        smenu = mostrar_submenu_alimentos()
        
        if smenu == "1":
            compra, total, salir = menu_comida_perros(compra, total, salir)
        elif smenu == "2":
            compra, total, salir = menu_comida_gatos(compra, total, salir)
        elif smenu == "3":
            compra, total, salir = menu_comida_peces(compra, total, salir)
        elif smenu == "4":
            compra, total, salir = menu_comida_aves(compra, total, salir)
        elif smenu == "5":
            break
        elif smenu == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        
        if salir:
            break
    
    return compra, total, salir

def menu_comida_perros(compra, total, salir):
    productos = [
        ("Dog Chow", 15),
        ("Pedigree", 18),
        ("Pro Plan", 25),
        ("Royal Canin", 30)
    ]
    while True:
        op = mostrar_productos("COMIDA PARA PERROS", productos)
        if op in ["1", "2", "3", "4"]:
            compra, total = procesar_producto(compra, total, productos, op)
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir:
            break
    return compra, total, salir

def menu_comida_gatos(compra, total, salir):
    productos = [
        ("Whiskas", 10),
        ("Cat Chow", 14),
        ("Pro Plan Gatos", 22),
        ("Royal Canin Gatos", 28)
    ]
    while True:
        op = mostrar_productos("COMIDA PARA GATOS", productos)
        if op in ["1", "2", "3", "4"]:
            compra, total = procesar_producto(compra, total, productos, op)
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir:
            break
    return compra, total, salir

def menu_comida_peces(compra, total, salir):
    productos = [
        ("Tetramin", 5),
        ("Nutrafin", 7),
        ("Sera Vipan", 9),
        ("Tetra Goldfish", 11)
    ]
    while True:
        op = mostrar_productos("COMIDA PARA PECES", productos)
        if op in ["1", "2", "3", "4"]:
            compra, total = procesar_producto(compra, total, productos, op)
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir:
            break
    return compra, total, salir

def menu_comida_aves(compra, total, salir):
    productos = [
        ("Semillas Premium", 7),
        ("Vitakraft", 10),
        ("Kaytee", 13),
        ("ZuPreem", 16)
    ]
    while True:
        op = mostrar_productos("COMIDA PARA AVES", productos)
        if op in ["1", "2", "3", "4"]:
            compra, total = procesar_producto(compra, total, productos, op)
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir:
            break
    return compra, total, salir

def menu_juguetes(compra, total, salir):
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
            compra, total, salir = menu_accesorios_perros(compra, total, salir)
        elif smenu == "2":
            compra, total, salir = menu_accesorios_gatos(compra, total, salir)
        elif smenu == "3":
            compra, total, salir = menu_accesorios_peces(compra, total, salir)
        elif smenu == "4":
            compra, total, salir = menu_accesorios_aves(compra, total, salir)
        elif smenu == "5":
            break
        elif smenu == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        
        if salir:
            break
    
    return compra, total, salir

def menu_accesorios_perros(compra, total, salir):
    productos = [
        ("Juguete mordedor", 1.99),
        ("Correa", 5),
        ("Cama", 20),
        ("Plato", 8)
    ]
    while True:
        op = mostrar_productos("Accesorios para perros", productos)
        if op in ["1", "2", "3", "4"]:
            compra, total = procesar_producto(compra, total, productos, op)
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir:
            break
    return compra, total, salir

def menu_accesorios_gatos(compra, total, salir):
    productos = [
        ("Collar gato", 1.99),
        ("Rascador", 15),
        ("Cama gato", 18),
        ("Juguete plumas", 6)
    ]
    while True:
        op = mostrar_productos("Accesorios para gatos", productos)
        if op in ["1", "2", "3", "4"]:
            compra, total = procesar_producto(compra, total, productos, op)
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir:
            break
    return compra, total, salir

def menu_accesorios_peces(compra, total, salir):
    productos = [
        ("Tunnel peces", 3.50),
        ("Pecera", 25),
        ("Filtro", 12),
        ("Decoración", 9)
    ]
    while True:
        op = mostrar_productos("Accesorios para peces", productos)
        if op in ["1", "2", "3", "4"]:
            compra, total = procesar_producto(compra, total, productos, op)
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir:
            break
    return compra, total, salir

def menu_accesorios_aves(compra, total, salir):
    productos = [
        ("Juguete espejo", 4.99),
        ("Jaula", 30),
        ("Comedero", 7),
        ("Campana", 5)
    ]
    while True:
        op = mostrar_productos("Accesorios para aves", productos)
        if op in ["1", "2", "3", "4"]:
            compra, total = procesar_producto(compra, total, productos, op)
        elif op == "5":
            break
        elif op == "6":
            salir = True
            break
        else:
            print("Opción incorrecta")
        if salir:
            break
    return compra, total, salir

def mostrar_resumen(nombre, cdi, compra, total):
    print("========================================")
    print("          RESUMEN DE COMPRA")
    print("========================================")
    print("Cliente:", nombre)
    print("Cédula:", cdi)
    print("----------------------------------------")
    print("Productos seleccionados:")
    print(compra)
    print("----------------------------------------")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("Gracias por visitar JUJAM PET :D")
    print("========================================")

def main():
    mostrar_encabezado()
    nombre, cdi = obtener_datos_cliente()
    
    total = 0
    compra = ""
    salir = False
    
    while not salir:
        menu = mostrar_menu_principal()
        
        if menu == "1":
            compra, total, salir = menu_alimentos(compra, total, salir)
        elif menu == "2":
            compra, total, salir = menu_juguetes(compra, total, salir)
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
        mostrar_resumen(nombre, cdi, compra, total)
    else:
        print("No realizó ninguna compra. ¡Vuelva pronto!")

if __name__ == "__main__":
    main()
