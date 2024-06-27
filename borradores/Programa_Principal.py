
print("|=============================================|")
print("Bienvenido al terminal de arriendo de viviendas")
print("|=============================================|")


def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Arrendar una vivienda")
        print("2. Publicar una vivienda")
        print("3. Opción 3")
        print("4. Salir")
        opcion = input("Seleccione una opción (1/2/3/4): ")
        menu_principal()

from Libreria_LIS import (solicitar_RUT, crear_contraseña, mostrar_reglas, solicitar_continuacion, solicitar_informacion_arriendo, solicitar_liquidaciones, mostrar_informacion_arriendo)



RUT = solicitar_RUT()

contraseña=crear_contraseña()
if contraseña:
    mostrar_reglas()
    if solicitar_continuacion():
        tiempo_arriendo, tipo_sitio,personas,mascotas,presupuesto=solicitar_informacion_arriendo()
        liquidaciones= solicitar_liquidaciones()
        mostrar_informacion_arriendo(tiempo_arriendo,tipo_sitio,personas,mascotas,presupuesto,liquidaciones)
    else:
        print("Lamentamos que no quiera continuar, Buena suerte") 
else:
    print("Fallaste en la creacion de contraseña, sera expulsado del programa")