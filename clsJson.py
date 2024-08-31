import json
class JsonFile:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)
    def read(self):
        try:
            with open(self.filename,'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data
     
    def find(self,atributo,buscado):
        try:
            with open(self.filename,'r') as file:
                datas = json.load(file)
                data = [item for item in datas if item[atributo] == buscado ]
        except FileNotFoundError:
            data = []
        except KeyError:
            print(f"Error: El atributo '{atributo}' no se encuentra en algunos elementos del archivo.")
            data = []
        return data