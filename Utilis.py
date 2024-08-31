import os

#colores para la impresion de texto
green_color = '\033[32m'
blue_color = '\033[34m'
purple_color = '\033[35m'
reset_color = '\033[0m'
red_color = '\033[31m'

def BorrarPantalla():
    os.system('cls')

def linea():
    print(f"{purple_color}{80*'='}{reset_color}")

class Menu:
    def __init__(self, titulo="", opciones=[]):
        self.titulo = titulo
        self.opciones = opciones
        
    def menu(self):
        print(self.titulo)
        for index, opcion in enumerate(self.opciones, start=1):
            print(f"{index}. {opcion}")
        opc = input(f"Elija opción [1...{len(self.opciones)}]: ") 
        return opc
