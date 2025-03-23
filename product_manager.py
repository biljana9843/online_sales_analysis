

from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        for product in self.products:
            print(product.display_info())

    def calculate_total_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return f"Ukupna vrednost svih proizvoda: {total_value} RSD"
    
    def remove_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return f"Proizvod '{name}' je uklonjen."
   


# Primer korišćenja:
if __name__ == "__main__":
    manager = ProductManager()

    # Dodajemo proizvode
    product1 = Product(name="Laptop", price=85000, quantity=10)
    product2 = Product(name="Telefon", price=45000, quantity=5)
    manager.add_product(product1)
    manager.add_product(product2)

    # Prikazujemo sve proizvode
    print("Lista svih proizvoda:")
    manager.display_all_products()

    # Računamo ukupnu vrednost
    print(manager.calculate_total_value())
