class Client:
    def __init__(self, first_name = "Consumidor", last_name = "Final", dni = "0999999999"):
        self.first_name = first_name
        self.last_name = last_name
        self.__dni = dni
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, value): # Value no esta funcionando en el metodo (No se tendria que cambiar un DNI)
        self.__dni.isnumeric() and len(self.__dni) == 10

    def __str__(self):
        return f"Nombre:{self.first_name} {self.last_name}\n DNI:{self.dni}\n"

class RegularClient(Client):
    def __init__(self, first_name = "Cliente", last_name = "Regular", dni = "0999999999", card = False):
        super().__init__(first_name, last_name, dni)
        self.__discount = 0.10 if card else 0.5

    @property
    def discount(self):
        return self.__discount
    
    def __str__(self):
        return f"Cliente Regular\nNombre: {self.first_name} {self.last_name}\nDNI: {self.dni}\nDescuento: {self.discount}\n"
    
    def show(self):
        print(f"Cliente Regular: {self.first_name} {self.last_name}, DNI: {self.dni}") # Para mostrar el Cliente
    
    def getJson(self):
        return {"Nombre":self.first_name, "Apellido":self.last_name, "DNI":self.dni, "Valor":self.discount}
    
class VipClient(Client):
    def __init__(self, first_name = "Cliente", last_name = "VIP", dni = "0999999999"):
        super().__init__(first_name, last_name, dni)
        self.__limit = 10000

    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limit(self, value):
        self.__limit = 10000 if (value < 10000 or value > 20000) else value

    def __str__(self):
        return f"Cliente VIP\nNombre: {self.first_name} {self.last_name}\nDNI: {self.dni}\nLimite de credito: {self.limit}\n"
    
    def show(self):
        print(f"Cliente Regular: {self.first_name} {self.last_name}, DNI: {self.dni}") # Para mostrar el Cliente

    def getJson(self):
        return {"Nombre":self.first_name, "Apellido":self.last_name, "DNI":self.dni, "Valor":self.limit}

if __name__ == "__main__":
    client1 = RegularClient("Snayder", "Cedeno", "0944104942", True)
    print(client1)
    print(client1.getJson())

    client2 = VipClient("Gabriel", "Hasqui", "0951777838")
    print(client2)
    print(client2.getJson())