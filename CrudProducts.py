from Utilis import green_color, blue_color, purple_color, reset_color, BorrarPantalla,linea, Menu
from Company import Company
from Product import Product
from Icrud import Icrud
from clsJson import JsonFile
import os
import time

path, file = os.path.split(__file__)

class CrudProducts(Icrud):
    json_file = JsonFile(f"{path}/data/products.json")
    Company = Company()

    def create(self):
        productos = self.json_file.read()
        
        if productos:
            next_id = max(producto['ID'] for producto in productos) + 1
        else:
            next_id = 1 

        descrip = input("Ingrese la descripción del producto: ")

        while True:
            try:
                preci = float(input("Ingrese el precio del producto: "))
                if preci <= 0:
                    raise ValueError("El precio debe ser positivo.")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                stock = int(input("Ingrese la cantidad en stock: "))
                if stock < 0:
                    raise ValueError("El stock no puede ser negativo.")
                break
            except ValueError as e:
                print(f"Error: {e}")

        producto_existente = any(p['Descripción'] == descrip for p in productos)

        if producto_existente:
            print("Este producto ya está registrado.")
        else:
            producto = Product(next_id, descrip, preci, stock)
            productos.append(producto.getjson())
            self.json_file.save(productos)
            print("Producto registrado exitosamente!")
        time.sleep(3)

    def update(self):

        product_id = int(input("Ingrese el ID del producto a actualizar: "))
        productos = self.json_file.read()

        for producto in productos:
            if producto['ID'] == product_id:
                print(f"Producto encontrado: {producto['Descripción']}")
                nuevo_preci = input("Nuevo precio (presione Enter para dejar sin cambios): ").strip()
                nuevo_stock = input("Nuevo stock (presione Enter para dejar sin cambios): ").strip()

                if nuevo_preci:
                    producto['Precio'] = float(nuevo_preci)
                if nuevo_stock:
                    producto['Stock'] = int(nuevo_stock)

                self.json_file.save(productos)
                print("Producto actualizado exitosamente!")
                break
            else:
                print("Producto no encontrado.")
            time.sleep(3)
        
    def delete(self):
        product_id = int(input("Ingrese el ID del producto a eliminar: "))
        productos = self.json_file.read()

        for producto in productos:
            if producto['ID'] == product_id:
                print(f"Producto encontrado: {producto['Descripción']}")
                confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ").strip().lower()

                if confirmacion == 's':
                    productos.remove(producto)
                    self.json_file.save(productos)
                    print("Producto eliminado exitosamente!")
                else:
                    print("Eliminación cancelada.")
                break
            else:
                print("Producto no encontrado.")
            time.sleep(3)

    def consult(self):
        while True:
            BorrarPantalla()
            menu = Menu(titulo="=== Consulta de Productos ===", opciones=["Buscar por ID", "Buscar por Descripción", "Ver todos los productos", "Volver al menú principal"])
            seleccion = menu.menu()

            if seleccion == "1":
                product_id = int(input("Ingrese el ID del producto: "))
                productos = self.json_file.find('ID', product_id)
            elif seleccion == "2":
                descrip = input("Ingrese la descripción del producto: ")
                productos = self.json_file.find('Descripción', descrip)
            elif seleccion == "3":
                productos = self.json_file.read()
            elif seleccion == "4":
                return
            else:
                print("Opción inválida.")
                time.sleep(2)
                continue 

            if productos:
                for producto in productos:
                    print(f"ID: {producto['ID']}, Descripción: {producto['Descripción']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")
            else:
                print("No se encontraron productos con esa búsqueda.")
            
            input("Presione Enter para volver al menú...")