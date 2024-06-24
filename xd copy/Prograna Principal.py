print("===============================================")
print("Bienvenido al terminal de arriendo de viviendas")
print("===============================================")



from Libreria import (solicitar_RUT, crear_contraseña, mostrar_reglas, solicitar_informacion_arriendo,
    solicitar_liquidaciones, mostrar_informacion_arriendo, solicitar_continuacion,menu_arriendos, especificaciones_arriendo, mostrar_informacion_vivienda,agregar_vivienda_arrendada, agregar_vivienda_publicada, ver_viviendas)

RUT = solicitar_RUT()
contraseña = crear_contraseña()
#lo de abajo es nuestro menu principal
if contraseña:
    while True:
        print("\n¿Que desea hacer?")
        print("1. Arrendar una vivienda")
        print("2. Poner una vivienda en arriendo")
        print("3. Ver viviendas Publicadas o Arrendadas")
        print("4. Salir")
        opcion = input("Seleccione una opción (1/2/3/4): ").strip().lower()
        
        if opcion == "1":
            mostrar_reglas()
            if solicitar_continuacion():
                personas, mascotas, presupuesto = solicitar_informacion_arriendo()
                liquidaciones = solicitar_liquidaciones()
                mostrar_informacion_arriendo(personas, mascotas, presupuesto, liquidaciones)
                menu_arriendos()
                agregar_vivienda_arrendada(f"personas: {personas}, mascotas: {mascotas}, presupuesto: {presupuesto}, sueldos: {', '.join(liquidaciones)}")
            else:
                print("Lamentamos que no quiera continuar, sera llevado al menu principal") 
        elif opcion == "2":
            tamaño, habitaciones, baños, direccion, precio = especificaciones_arriendo()
            mostrar_informacion_vivienda(tamaño, habitaciones, baños, direccion, precio)
            agregar_vivienda_publicada(f"tamaño: {tamaño} m2, habitaciones: {habitaciones}, baños: {baños}, dirección: {direccion}, precio: {precio}")
        elif opcion == "3":
            ver_viviendas()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion incorrecta, intente nuevamente.")
