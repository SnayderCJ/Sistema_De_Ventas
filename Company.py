from Utilis import green_color, blue_color, purple_color, reset_color

class Company:
    next = 0    
    def __init__(self, name = "Super Maxi", ruc = "0943213456001"):
        Company.next += 1
        self._id = Company.next
        self.name = name
        self.ruc = ruc
    
    def __str__(self):
        return f"id:{self._id}\nCompañia:{self.name}\nRuc:{self.ruc}\n"
    
    def show(self):
        print(f"{blue_color}Compañia: {purple_color}{self.name}{reset_color}\n{blue_color}Ruc: {purple_color}{self.ruc}{reset_color}")
    
if __name__ == "__main__":
    comp = Company()
    comp.show()

