#Utilizando contraseña para ingresar al programa
ARCHIVO = "estudiantes.txt"
CLAVE = "pepito123"

import pwinput

def agregar_usuario(usuario, clave):
    with open("estudiantes.txt", "a")as archivo:
              archivo.write(f"{usario}, {clave}")



def inicio():
    print("INICIO DE SESION ")
    usuarios = cargar_usuarios()
    usuario = input("Usuario : ")
    
    clave_ingresada = pwinput.pwinput(prompt = "Contraseña : ", mask = " * ")
    if usuario in usuarios and usuarios[usuario] == clave_ingresada:
        print("Acceso permitido")
        return True
    else: 
        print(" Usuario o contrañeña incorrecta.")
        return False