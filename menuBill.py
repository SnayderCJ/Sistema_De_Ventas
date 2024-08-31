from Utilis import green_color, blue_color, purple_color, reset_color,red_color, BorrarPantalla,linea, Menu
from CrudClients import CrudClients
from CrudProducts import CrudProducts
from Company import Company
from Sales import Sale, SaleDetail, Product
from Icrud import Icrud
from clsJson import JsonFile
from Customer import RegularClient, VipClient
from Product import Product 
from datetime import date
import datetime
import os
import time

path, file = os.path.split(__file__)

class CrudSales(Icrud):
  def create(self):
    company = Company()
    company.show()

    print(green_color + "*" * 90 + reset_color)
    print(blue_color + "Registro de Venta".center(90))
    print(f"Factura#: {'F0999999':<15} {' ' * 10} Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 90)

    # Información del cliente
    dni = input("Ingresa el DNI del cliente: ")  # Solicita el número de cédula del cliente
    json_file = JsonFile(f"{path}/data/clients.json")

    client = json_file.find("DNI", dni)
    if not client:
        print("Cliente no existe")
        return

    client = client[0]
    if client['Valor'] == 0.1:
        cli = RegularClient(client['Nombre'], client['Apellido'], client['DNI'], True)
    elif client['Valor'] == 0:
        cli = RegularClient(client['Nombre'], client['Apellido'], client['DNI'], False)
    elif client['Valor'] >= 10000:
        cli = VipClient(client['Nombre'], client['Apellido'], client['DNI'])

    # Mostrar datos del cliente
    print(f"Cliente: {cli.first_name} {cli.last_name}")
    print("-" * 90)

    sale = Sale(cli)

    print(f"{'Linea':<8}{'Id_Articulo':<15}{'Descripción':<30}{'Precio':<10}{'Cantidad':<10}{'Subtotal':<10}")
    print(reset_color + "-" * 90)

    # Detalle de la venta
    follow = "s"
    line = 1

    while follow.lower() == "s":
        print(f"{line:<8}", end="")
        id = int(input("Ingresa el ID del producto: "))  # Solicita el ID del producto
        json_file = JsonFile(f"{path}/data/products.json")

        prods = json_file.find("ID", id)  # Busca el producto por su ID

        if not prods:
            print("Producto no existe")
            time.sleep(1)
        else:
            prods = prods[0]
            product = Product(prods["ID"], prods["Description"], prods["Precio"], prods["Stock"])  # Crea un producto
            qyt = int(input("Ingresa la cantidad: "))  # Solicita la cantidad de producto
            subtotal = product.preci * qyt
            print(f"{product.descrip:<30}{product.preci:<10}{qyt:<10}{subtotal:<10}")
            sale.add_detail(product, qyt)  # Agrega el detalle de la venta
            follow = input("¿Desea agregar otro producto? (s/n): ").lower()
            if follow == "s":
                line += 1
            else:
                print("-" * 90)
                print(f"{'Subtotal:':<40} {round(sale.subtotal, 2):<10}")
                print(f"{'Descuento:':<40} {round(sale.discount, 2):<10}")
                print(f"{'Iva     :':<40} {round(sale.iva, 2):<10}")
                print(f"{'Total   :':<40} {round(sale.total, 2):<10}")

    # Confirmación de la venta
    print("¿Está seguro de grabar la venta? (s/n): ", end='')
    procesar = input().lower()  # Pregunta si se quiere grabar la venta

    if procesar == "s":
        print(green_color + "😊 Venta Grabada satisfactoriamente 😊" + reset_color)
        json_file = JsonFile(f"{path}/data/invoices.json")
        invoices = json_file.read()
        ult_invoices = invoices[-1]["factura"] + 1 if invoices else 1
        data = sale.getJson()
        data["factura"] = ult_invoices
        invoices.append(data)
        json_file.save(invoices)
    else:
        print(red_color + "🤣 Venta Cancelada 🤣" + reset_color)

    time.sleep(2)
  def update(self):
    pass

  def delete(self):
    pass

  def consult(self):
    pass

opc = ''
while opc != '4':
    BorrarPantalla()
    menu_main = Menu("Menu facturación", ["Clientes", "Productos", "Ventas", "Salir"],)
    opc = menu_main.menu()
    if opc == '1':
        opc1 = ''
        while opc1 != '5':
            BorrarPantalla()
            menu_clients = Menu("Menu clientes", ["Crear", "Actualizar", "Eliminar", "Consultar", "Salir"])
            opc1 = menu_clients.menu()
            crud = CrudClients()
            if opc1 == '1':
                crud.create()
            elif opc1 == '2':
                crud.update()
            elif opc1 == '3':
                crud.delete()
            elif opc1 == '4':
                crud.consult()
            print("Regresando al menu principal")
    elif opc == '2':
        opc2 = ''
        while opc2 != '5':
            BorrarPantalla()
            menu_products = Menu("Menu productos", ["Crear", "Actualizar", "Eliminar", "Consultar", "Salir"])
            opc2 = menu_products.menu()
            crud = CrudProducts()
            if opc2 == '1':
                crud.create() 
            elif opc2 == '2':
                crud.update()
            elif opc2 == '3':
                crud.delete()
            elif opc2 == '4':
                crud.consult()
    elif opc == '3':
        opc3 = ''
        while opc3 != '5':
            BorrarPantalla()
            menu_sales = Menu("Menu ventas", ["Crear", "Actualizar", "Eliminar", "Consultar", "Salir"])
            opc3 = menu_sales.menu()
            if opc3 == '1':
                crud = CrudSales()
                crud.create()   
            elif opc3 == '2':
                pass
            elif opc3 == '3':
                pass
            elif opc3 == '4':
                pass
    
    print("Regresando al menu principal")

BorrarPantalla()
input("Presione una tecla para salir...")
BorrarPantalla()
            
