def bienvenida():
    print("===============================================")
    print("Bienvenido al terminal de arriendo de viviendas")
    print("===============================================")

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
        contraseña = input("creee una contraseña de 8 caracteres utilizando unicamente numeros: ")
        if not (contraseña.isdigit() and sum(1 for _ in contraseña) == 8):
            intentos -= 1
            if not contraseña.isdigit():
                print(f"error, la contraseña solo permite caracteres de tipo numerico. (Te quedan {intentos} intentos)")
            else:
                print(f"error, la contraseña no tiene 8 caracteres. (Te quedan {intentos} intentos)")
            continue
        print(f"Contraseña creada: {contraseña}")
        return contraseña
    print("Fallaste tus 3 intentos, seras expulsado")
    return None


def mostrar_reglas():
    print("\nReglas del arriendo")
    reglas = """
    -Tener registro de las últimas tres liquidaciones de sueldo.
    -Pagar con un mes de anticipación.
    -En caso de atraso de paga tienen una semana para desalojar.
    -Después de la 1 am ya no pueden haber ruidos fuertes y en caso de reclamos por ruidos deberá pagar una multa de 50.000.
    -En caso de daños a la infraestructura lo debera de pagar el arrendatario.
    -En caso de reclamos excesivos se les dara a los culpables un mes para desalojar.
    -En los gastos comunes solo se cubre luz y agua, gastos como gas e internet los debe pagar el arrendatario.
    -En caso de pérdida de las llaves se le cobrará una nueva mas el cambio de ranura.
    """
    print(reglas)

def solicitar_continuacion():
    continuar = input("Una vez leídas las reglas, ¿Desea continuar con el arriendo? (Si/No): ").strip().lower()
    return continuar == "si" or continuar == "sí"

def solicitar_informacion_arriendo():
    tiempo_arriendo = input("1.Cuanto tiempo arrendaran?: ")
    tipo_sitio = input("2.Que tipo de casa buscan arrendar?: ")
    personas = input("3.Cuántas personas serán en el lugar?: ")
    mascotas = input("4.Tienen mascotas? (Si/No): ")
    presupuesto = int(input("5. ¿Cuanto dinero tienen para el arriendo?: "))
    recomendar_vivienda(presupuesto)
    return tiempo_arriendo, tipo_sitio, personas, mascotas, presupuesto

def solicitar_liquidaciones():
    liquidaciones = []
    for x in range(1, 4):
        liquidacion = input(f"Ingrese su sueldo #{x} de los últimos 3 meses: ")
        liquidaciones.append(liquidacion)
    return liquidaciones

def mostrar_informacion_arriendo(tiempo_arriendo, tipo_sitio, personas, mascotas, presupuesto, liquidaciones):
    print("\nInformación del arriendo:")
    print(f"Tiempo de arriendo: {tiempo_arriendo}")
    print(f"Tipo de sitio: {tipo_sitio}")
    print(f"Número de personas: {personas}")
    print(f"¿Tienen mascotas?: {mascotas}")
    print(f"Presupuesto: {presupuesto}")
    print(f"Sueldo de los últimos tres meses: {', '.join(liquidaciones)}")

def recomendar_vivienda(presupuesto):
    if 300000 <= presupuesto <= 499000:
        print("Arriendo n1 ")
    elif 500000 <= presupuesto <= 799000:
        print("Arriendo n2")
    elif presupuesto > 800000:
        print("Arriendo n3")
    else:
        print("no tiene el presupuesto minimo.")

bienvenida()
RUT = solicitar_RUT()
if RUT:
    contraseña = crear_contraseña()
    if contraseña:
        mostrar_reglas()
        if solicitar_continuacion():
            tiempo_arriendo, tipo_sitio, personas, mascotas, presupuesto = solicitar_informacion_arriendo()
            liquidaciones = solicitar_liquidaciones()
            mostrar_informacion_arriendo(tiempo_arriendo, tipo_sitio, personas, mascotas, presupuesto, liquidaciones)