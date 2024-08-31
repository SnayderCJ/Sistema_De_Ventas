from Customer import RegularClient, VipClient
from Icrud import Icrud
from clsJson import JsonFile
from Utilis import BorrarPantalla, Menu, green_color, blue_color, purple_color, reset_color, linea
from Company import Company
import time
import os

path, file = os.path.split(__file__)

class CrudClients(Icrud):
    json_file = JsonFile(f"{path}/data/clients.json")
    Company = Company()
    def create(self):
        while True:
            BorrarPantalla()
            menu = Menu(titulo="=== Registro de Cliente ===", opciones=["Cliente Regular", "Cliente VIP", "Volver al menú principal"])
            seleccion = menu.menu()

            if seleccion == "1":
                tipo_cliente = "Regular"
            elif seleccion == "2":
                tipo_cliente = "VIP"
            elif seleccion == "3":
                return
            else:
                print("Opción inválida.")
                time.sleep(2)
                continue 

            nombre = input("Ingresa el nombre del cliente: ")
            apellido = input("Ingresa el apellido del cliente: ")
            dni = input("Ingrese el DNI del cliente: ")

            if tipo_cliente == "Regular":
                tarjeta = input("¿El cliente tiene tarjeta de descuento? (s/n): ").strip().lower() == "s"
                cliente = RegularClient(nombre, apellido, dni, tarjeta)
            else:
                cliente = VipClient(nombre, apellido, dni)

            clientes = self.json_file.read()
            cliente_existente = any(c['DNI'] == dni for c in clientes)

            if cliente_existente:
                print("Este cliente ya está registrado.")
            else:
                clientes.append(cliente.getJson())
                self.json_file.save(clientes)
                print("Cliente registrado exitosamente!")
            time.sleep(3)
    def update(self):
        dni = input("Ingrese el DNI del cliente a actualizar: ")
        clientes = self.json_file.read()

        for cliente in clientes:
            if cliente['DNI'] == dni:
                print(f"Cliente encontrado: {cliente['Nombre']} {cliente['Apellido']}")
                nuevo_nombre = input("Nuevo nombre (presione Enter para dejar sin cambios): ").strip()
                nuevo_apellido = input("Nuevo apellido (presione Enter para dejar sin cambios): ").strip()
                if nuevo_nombre:
                    cliente['Nombre'] = nuevo_nombre
                if nuevo_apellido:
                    cliente['Apellido'] = nuevo_apellido
                self.json_file.save(clientes)
                print("Cliente actualizado exitosamente!")
                break
        else:
            print("Cliente no encontrado.")
            
        time.sleep(3)
    def delete(self):
        dni = input("Ingrese el DNI del cliente a eliminar: ")
        clientes = self.json_file.read()
        for cliente in clientes:
            if cliente['DNI'] == dni:
                print(f"Cliente encontrado: {cliente['Nombre']} {cliente['Apellido']}")
                confirmacion = input("¿Está seguro de que desea eliminar este cliente? (s/n): ").strip().lower()

                if confirmacion == 's':
                    clientes.remove(cliente)
                    self.json_file.save(clientes)
                    print("Cliente eliminado exitosamente!")
                else:
                    print("Eliminación cancelada.")
                break
        else:
            print("Cliente no encontrado.")
        time.sleep(3)
    def consult(self):
        while True:
            BorrarPantalla()
            menu = Menu(titulo="=== Consulta de Clientes ===", opciones=["Buscar por DNI", "Buscar por Nombre", "Buscar por Apellido", "Ver todos los clientes", "Volver al menú principal"])
            seleccion = menu.menu()

            if seleccion == "1":
                dni = input("Ingrese el DNI del cliente: ")
                clientes = self.json_file.find('DNI', dni)
            elif seleccion == "2":
                nombre = input("Ingrese el nombre del cliente: ")
                clientes = self.json_file.find('Nombre', nombre)
            elif seleccion == "3":
                apellido = input("Ingrese el apellido del cliente: ")
                clientes = self.json_file.find('Apellido', apellido)
            elif seleccion == "4":
                clientes = self.json_file.read()
            elif seleccion == "5":
                return
            else:
                print("Opción inválida.")
                time.sleep(2)
                continue 

            if clientes:
                for cliente in clientes:
                    print(f"Nombre: {cliente['Nombre']}, Apellido: {cliente['Apellido']}, DNI: {cliente['DNI']}")
            else:
                print("No se encontraron clientes con esa búsqueda.")
            
            input("Presione Enter para volver al menú...")