import os
import time
from funciones import *


#ejercicio python prueba practica

while True:
    os.system('cls')
    print("MENÚ DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Mostrar contacto")
    print("3. Guardar contacto en un archivo")
    print("4. Salir del programa ")
    opc= int(input("Ingrese una opción: "))
    os.system('cls')
    if opc== 1:
        listar_contacto()

    elif opc== 2:
        mostrar_contacto()
        
    elif opc== 3:
        Guardar_archivo()
    else:
        salir_programa()
    time.sleep(3)
        



