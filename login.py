#Utilizando contraseña para ingresar al programa
ARCHIVO = "estudiantes.txt"
CLAVE = "pepito123"
import getpass
import os
import pwinput

def cargar_usuario():
    usuario = {}
    if os.path.exits("usuarios.txt"):
        with open("usuarios.txt", "r")as archivo:
            for linea in archivo:
                usuario, clave = linea.strip().split(" , ")
                usuarios[usuario] = clave
    return usuarios

def agregar_usuario(usuario, clave):
    with open("usuario.txt", "a")as archivo:
              archivo.write(f"{usario}, {clave}")



def inicio():
    print("INICIO DE SESION ")
    usuarios = cargar_usuario()
    usuario = input("Usuario : ")
    
    clave_ingresada = pwinput.pwinput(prompt = "Contraseña : ", mask = " * ")
    if usuario in usuarios and usuarios[usuario] == clave_ingresada:
        print("Acceso permitido")
        return True
    else: 
        print(" Usuario o contrañeña incorrecta.")
        return False
inicio()