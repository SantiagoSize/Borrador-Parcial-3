


print("Bienvenido al terminal de arriendo de viviendas de lukironsantieneltik")
from Libreria_LIS import (solicitar_RUT, crear_contraseña, mostrar_reglas, solicitar_continuacion, solicitar_informacion_arriendo, solicitar_liquidaciones,mostrar_informacion_arriendo)



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