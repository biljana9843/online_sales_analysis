

from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        self.cart_items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.cart_items)
        return f"Ukupna vrednost korpe: {total} RSD"

def display_cart(self):
    for item in self.cart_items:
        print(item["product"].name, item["quantity"])

# Primer korišćenja:
if __name__ == "__main__":
    # Kreiramo proizvode
    laptop = Product(name="Laptop", price=85000, quantity=10)
    telefon = Product(name="Telefon", price=45000, quantity=5)

    # Kreiramo instancu Cart
    korpa = Cart()

    # Dodajemo proizvode u korpu
    korpa.add_to_cart(laptop, 2)
    korpa.add_to_cart(telefon, 1)

    # Prikazujemo sadržaj korpe
    print("Sadržaj korpe:")
    print(korpa.display_cart())

    # Računamo ukupnu vrednost korpe
    print(korpa.calculate_total())
