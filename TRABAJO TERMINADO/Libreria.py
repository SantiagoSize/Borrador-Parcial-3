
viviendas_arrendadas = []
viviendas_publicadas = []

def solicitar_RUT():
    RUT = input("Ingrese su RUT (No usar guiones ni puntos): ")
    RUT = RUT.replace(".", "").replace("-", "")
    if RUT.endswith("K"):
        RUT = RUT[:-1] + "0"
    print(f"RUT creado: {RUT}")
    return RUT

def crear_contraseña():
    intentos = 3
    while intentos > 0:
        contraseña = input("Cree una contraseña de 8 caracteres utilizando únicamente números: ")
        caracteres = sum(1 for c in contraseña)  
        if caracteres != 8:
            intentos -= 1
            print(f"error, la contraseña no tiene 8 caracteres. (Te quedan {intentos} intentos)")
            continue
        if not contraseña.isdigit():
            intentos -= 1
            print(f"error, la contraseña solo permite caracteres de tipo numérico. (Te quedan {intentos} intentos)")
            continue
        print(f"Contraseña creada: {contraseña}")
        return contraseña
    print("Fallaste tus 3 intentos, el programa se cerrara.")
    return None

def mostrar_reglas():
    print("\nReglas del arriendo")
    reglas = """
    -Tener registro de las últimas tres liquidaciones de sueldo.
    -Pagar con un mes de anticipacion.
    -En caso de atraso de paga tienen una semana para desalojar.
    -Después de la 1 am ya no pueden haber ruidos fuertes y en caso de reclamos por ruidos deberá pagar una multa de 50.000.
    -En caso de daños a la infraestructura lo deberá de pagar el arrendatario.
    -En caso de reclamos excesivos se les dará a los culpables un mes para desalojar.
    -En los gastos comunes solo se cubre luz y agua, gastos como gas e internet los debe pagar el arrendatario.
    -En caso de pérdida de las llaves se le cobrará una nueva más el cambio de ranura.
    """
    print(reglas)

def solicitar_continuacion():
    while True:
        print("\n¿Desea continuar con el arriendo?")
        print("1. Sí")
        print("2. No")
        opcion = input("Seleccione una opcion (1/2): ").strip().lower()
        
        if opcion == "1":
            return True
        elif opcion == "2":
            return False

def solicitar_informacion_arriendo():
    personas = input("3. Cuantas personas seran en el lugar?: ")
    mascotas = input("4. Tienen mascotas? (Si/No): ")
    presupuesto = input("5. Cuanto dinero tienen para el arriendo?: ")
    return personas, mascotas, presupuesto

def solicitar_liquidaciones():
    liquidaciones = []
    for x in range(1, 4):
        liquidacion = input(f"Ingrese su sueldo #{x} de los últimos 3 meses: ")
        liquidaciones.append(liquidacion)
    return liquidaciones

def mostrar_informacion_arriendo(personas, mascotas, presupuesto, liquidaciones):
    print("\nInformacion del arriendo:")
    print(f"Numero de personas: {personas}")
    print(f"Tienen mascotas?: {mascotas}")
    print(f"Presupuesto: {presupuesto}")
    print(f"Sueldo de los últimos tres meses: {', '.join(liquidaciones)}")

def menu_arriendos():
    while True:
        print("\nSeleccione el tipo de arriendo:")
        print("1. Casa")
        print("2. Departamento")
        print("3. Oficina")
        print("4. Volver")
        opcion = input("Seleccione una opcion (1/2/3/4): ").strip().lower()
        
        if opcion == "1":
            opciones_casa()
        elif opcion == "2":
            opciones_departamento()
        elif opcion == "3":
            opciones_oficina()
        elif opcion == "4":
            return
        else:
            print("Opcion incorrecta, intente nuevamente.")

def opciones_casa():
    while True:
        print("\nSeleccione una opcion de casa:")
        print("1. Casa pequeña (2 habitaciones, 1 baño)")
        print("2. Casa mediana (3 habitaciones, 2 baños)")
        print("3. Casa grande (4 habitaciones, 3 baños)")
        print("4. Volver")
        opcion = input("Seleccione una opcion (1/2/3/4): ").strip().lower()
        
        if opcion == "1":
            mostrar_detalles_casa("pequeña", 2, 1, 4, True, 300000)
            break
        elif opcion == "2":
            mostrar_detalles_casa("mediana", 3, 2, 6, True, 500000)
            break
        elif opcion == "3":
            mostrar_detalles_casa("grande", 4, 3, 8, False, 800000)
            break
        elif opcion == "4":
            return
        else:
            print("Opcion incorrecta, intente nuevamente.")

def opciones_departamento():
    while True:
        print("\nSeleccione una opcion de departamento:")
        print("1. Departamento pequeño (1 habitacion, 1 baño)")
        print("2. Departamento mediano (2 habitaciones, 1 baño)")
        print("3. Departamento grande (3 habitaciones, 2 baños)")
        print("4. Volver")
        opcion = input("Seleccione una opcion (1/2/3/4): ").strip().lower()
        
        if opcion == "1":
            mostrar_detalles_departamento("pequeño", 1, 1, 2, False, 200000)
            break
        elif opcion == "2":
            mostrar_detalles_departamento("mediano", 2, 1, 4, True, 400000)
            break
        elif opcion == "3":
            mostrar_detalles_departamento("grande", 3, 2, 6, True, 600000)
            break
        elif opcion == "4":
            return
        else:
            print("Opcion incorrecta, intente nuevamente.")

def opciones_oficina():
    while True:
        print("\nSeleccione una opcion de oficina:")
        print("1. Oficina pequeña (1 sala, 1 baño)")
        print("2. Oficina mediana (2 salas, 1 baño)")
        print("3. Oficina grande (3 salas, 2 baños)")
        print("4. Volver")
        opcion = input("Seleccione una opcion (1/2/3/4): ").strip().lower()
        
        if opcion == "1":
            mostrar_detalles_oficina("pequeña", 1, 1, 4, False, 500000)
            break
        elif opcion == "2":
            mostrar_detalles_oficina("mediana", 2, 1, 8, False, 1000000)
            break
        elif opcion == "3":
            mostrar_detalles_oficina("grande", 3, 2, 12, False, 1500000)
            break
        elif opcion == "4":
            return
        else:
            print("Opcion incorrecta, intente nuevamente.")

def mostrar_detalles_casa(tamaño, habitaciones, baños, personas, mascotas, costo):
    print(f"\nHa seleccionado una casa {tamaño} con {habitaciones} habitaciones y {baños} baños.")
    print(f"Capacidad para {personas} personas.")
    print(f"Permite mascotas?: {'Sí' if mascotas else 'No'}")
    print(f"Precio del arriendo: {costo}")
    confirmar_arriendo()

def mostrar_detalles_departamento(tamaño, habitaciones, baños, personas, mascotas, costo):
    print(f"\nHa seleccionado un departamento {tamaño} con {habitaciones} habitaciones y {baños} baños.")
    print(f"Capacidad para {personas} personas.")
    print(f"Permite mascotas?: {'Sí' if mascotas else 'No'}")
    print(f"Precio del arriendo: {costo}")
    confirmar_arriendo()

def mostrar_detalles_oficina(tamaño, salas, baños, personas, mascotas, costo):
    print(f"\nHa seleccionado una oficina {tamaño} con {salas} salas y {baños} baños.")
    print(f"Capacidad para {personas} personas.")
    print(f"Permite mascotas?: {'Sí' if mascotas else 'No'}")
    print(f"Precio del arriendo: {costo}")
    confirmar_arriendo()

def confirmar_arriendo():
    while True:
        print("\n¿Está seguro de que desea arrendar esta vivienda?")
        print("1. Si")
        print("2. No")
        opcion = input("Seleccione una opcion (1/2): ").strip().lower()
        
        if opcion == "1":
            print("Gracias por su arriendo.")
            menu_post_arriendo()
            break
        elif opcion == "2":
            print("Cancelando el arriendo.")
            break
        else:
            print("Opcion incorrecta, intente nuevamente.")

def menu_post_arriendo():
    while True:
        print("\n¿Que desea hacer ahora?")
        print("1. Volver al inicio")
        print("2. Arrendar otra vivienda")
        print("3. Salir del programa")
        opcion = input("Seleccione una opcion (1/2/3): ").strip().lower()
        
        if opcion == "1":
            return  
        elif opcion == "2":
            menu_arriendos()  
            break
        elif opcion == "3":
            print("Saliendo del programa.")
            exit()  
        else:
            print("Opcion incorrecta, intente nuevamente.")

def especificaciones_arriendo():
    print("\nIngrese las especificaciones de la vivienda en arriendo:")
    tamaño = input("1. Tamaño (en metros cuadrados): ")
    habitaciones = input("2. Numero de habitaciones: ")
    baños = input("3. Numero de baños: ")
    direccion = input("4. Direccion: ")
    precio = input("5. Precio del arriendo: ")
    return tamaño, habitaciones, baños, direccion, precio

def mostrar_informacion_vivienda(tamaño, habitaciones, baños, direccion, precio):
    print("\nInformacion de la vivienda en arriendo:")
    print(f"Tamaño: {tamaño} m2")
    print(f"Habitaciones: {habitaciones}")
    print(f"Baños: {baños}")
    print(f"Direccion: {direccion}")
    print(f"Precio del arriendo: {precio}")

def agregar_vivienda_arrendada(vivienda):
    viviendas_arrendadas.append(vivienda)

def agregar_vivienda_publicada(vivienda):
    viviendas_publicadas.append(vivienda)

def ver_viviendas():
    print("\nViviendas Arrendadas:")
    if viviendas_arrendadas:
        for vivienda in viviendas_arrendadas:
            print(vivienda)
    else:
        print("No hay viviendas arrendadas.")

    print("\nViviendas Publicadas:")
    if viviendas_publicadas:
        for vivienda in viviendas_publicadas:
            print(vivienda)
    else:
        print("No hay viviendas publicadas.")
