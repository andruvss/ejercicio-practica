import csv 



lista_de_contacto = []
lista_contactos = []


def listar_contacto():
    print("Agregar contacto")
    nombre_del_usuario = input("Ingrese su nombre: ")
    numero_del_usuario = int(input("Ingrese su número: "))
    correo_electronico = input("Ingrese su correo electronico: ")
    lista_de_contacto = [nombre_del_usuario, numero_del_usuario,correo_electronico]
    lista_contactos.append(lista_de_contacto)
    print("CONTACTO REGISTRADO EXITOSAMENTE!")


def mostrar_contacto():
    print("Mostrar contacto")
    if len (lista_contactos)==0:
        print("!lista vacia porfavor, vuelva a ingresar sus datos!")
    else:
        print("\tLISTA de contactos")
        for c in lista_contactos:
            print(f"NOMBRE: {c[0]}\nNUMERO DE CONTACTO: {c[1]}\nCORREO ELECTRONICO: {c[2]}\n")
            
def Guardar_archivo():
    lista_contactos = input("Ingrese nombre para guardar el archivo")
    with open("lista_contactos_csv","w",newline="") as archivo:
        lista_contactos = csv.writer(archivo)
        lista_contactos.writerow()


def salir_programa():
    print("!ADIOS, GRACIAS POR VENIR")
    exit()
 
  

