#Utilizando contraseña para ingresar al programa
ARCHIVO = "usuarios.txt"
CLAVE = "casique"
import getpass
import os
import pwinput

def continuar():
  input("Enter para continuar") 

def cargar_usuario():
    usuarios = []
    if os.path.exists("usuarios.txt"): 
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario, clave = linea.strip().split(", ") 
                usuarios[usuario] = clave
    return usuarios

def agregar_usuario(usuario, clave):
    with open("usuarios.txt", "a") as archivo: 
        archivo.write(f"{usuario}, {clave}\n")  

def main():
    print("INICIO DE SESION")
    usuarios = cargar_usuario()
    usuario = input("Usuario: ")
    
    clave_ingresada = pwinput.pwinput(prompt="Contraseña: ", mask="*")  
    if usuario in usuarios and usuarios[usuario] == clave_ingresada:
        print("Acceso permitido")
        return True
    else: 
        print("Usuario o contraseña incorrecta.")  
        continuar()
        os.system("cls")
    return False
main()