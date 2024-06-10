print("Bievenidoal temrinal de arriendo de viviendas lukironsantik")
RUT=input("Ingrese su RUT(No usar guiones ni puntos)")
RUT=RUT.replace(".","").replace("-","")

if RUT.endswith("K"):
    RUT=RUT[:-1]+"0"

print(F"RUT creado: {RUT}")

intentos=3

while intentos>0:
    contraseña=input("Cree ua contraseña de 8 caracteres utilizando unicamente numeros: ")

    if len(contraseña) !=8:
        intentos -=1
        print(f"Error, la contrasña no tiene 8 caracteres.(Te quedan {intentos})")
        continue

    if not contraseña.isdigit():
        intentos -=1
        print(f"Error, la contraseña solo permite caracteres de tipo numerico.(Te quedan {intentos})")
        continue

    print(f"Contraseña creada:{contraseña}")
    break

if intentos==0:
    print("Fallaste tus 3 intentos, te fuiste baneaaaaaaaaado")
else:

    print("\nReglas del arriendo")
    reglas="""
    -Tener registro de las ultimas tres liquidaciones de sueldo.
    -Pagar con un mes de anticipacion
    -En caso de atraso de paga tienen una semana para desalojar
    -Despues de las 1 am ya no pueden haber ruidos fuertes y en caso de reclamos por ruidos debera pagar una multa de 50.000
    -En caso de daños a la infraestructura lo debera de pagar en arrendatario
    -En caso de reclamos excesivos se les dara a los culpables un mes para desalojar
    -En los gastos comunes solo se cubre luz y agua, Gastos como gas e internet los debe pagar el arrendatario 
    -En caso de perdida de las llaves se le cobrara una nueva mas el cambiod de ranura 
    """
    print(reglas)

    continuar=input("Una vez leidas las reglas, Desea continuar con el arriendo? (Si/No): ").strip().lower()
    if continuar != "si" and continuar != "sí":
        print("Lamentamos que no quiera continuar, buena suerte")
    else:

        print("\nRequerimientos de arriendo")

        tiempo_arriendo=input("1. Cuanto tiempo arrendaran?: ")
        tipo_sitio=input("2. Que tipo de casa buscan arrendar?: ")
        personas=input("3. Cuantas personas seran en el lugar?: ")
        mascotas=input("4. Tienen mascotas? (Si/No): ")
        presupuesto=input("5. Cuanto dinero tienen para el arriendo?: ")
        


        liquidaciones=[]
        for x in range(1,4):
            liquidacion=input(f"Ingrese su liquidacion de sueldo #{x}: ")
            liquidaciones.append(liquidacion)

        print("\nInformacion del arriendo:")
        print(f"Tiempo de arriendo: {tiempo_arriendo}")
        print(f"Tipo de sitio: {tipo_sitio}")
        print(f"Numero de personas: {personas}")
        print(f"Tienen mascotas?: {mascotas}")
        print(f"Presupuesto: {presupuesto}")
        print(f"Liquidaciones de sueldo: {", ".join(liquidaciones)}")