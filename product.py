

class Product:
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    #prikaz informacija o proizvodu
    def display_info(self):
        return f"Proizvod: {self.name}, Cena: {self.price} RSD, Količina: {self.quantity}"

    #azuriranje kolicine proizvoda
    def update_quantity(self, amount):    
        self.quantity += amount
        return f"Ažurirana količina proizvoda {self.name}: {self.quantity}"

# Primer korišćenja:
if __name__ == "__main__":
   
    proizvod = Product(name="Laptop", price=85000, quantity=10)   
    print(proizvod.display_info())   
    print(proizvod.update_quantity(-2))  # Smanjuje količinu za 2
