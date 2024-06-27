print("|=============================================|")
print("Bienvenido al terminal de arriendo de viviendas")
print("|=============================================|")
from libreriabasyura import (solicitar_RUT, crear_contraseña, mostrar_reglas, solicitar_continuacion, solicitar_informacion_arriendo, solicitar_liquidaciones, mostrar_informacion_arriendo, recomendar_vivienda)

RUT = solicitar_RUT()

contraseña = crear_contraseña()
if contraseña:
    mostrar_reglas()
    if solicitar_continuacion():
        tiempo_arriendo, tipo_sitio, personas, mascotas, presupuesto = solicitar_informacion_arriendo()
        liquidaciones = solicitar_liquidaciones()
        mostrar_informacion_arriendo(tiempo_arriendo, tipo_sitio, personas, mascotas, presupuesto, liquidaciones)
    else:
        print("Lamentamos que no quiera continuar, Buena suerte")
else:
    print("Fallaste en la creación de contraseña, serás expulsado del programa")
