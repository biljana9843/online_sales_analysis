

from product_manager import ProductManager
from product import Product
from cart import Cart

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje nekoliko proizvoda
product1 = Product(name="Televizor", price=60000, quantity=3)
product2 = Product(name="Frižider", price=45000, quantity=2)
product3 = Product(name="Mikrotalasna", price=15000, quantity=5)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

# Prikazivanje svih proizvoda
print("Lista svih proizvoda:")
manager.display_all_products()

# Prikazivanje ukupne vrednosti inventara
print(manager.calculate_total_value())

# Kreiranje instance klase Cart
cart = Cart()

# Dodavanje proizvoda u korpu
cart.add_to_cart(product1, 1)
cart.add_to_cart(product2, 2)
cart.add_to_cart(product3, 1)

# Ispis sadržaja korpe
print("\nSadržaj korpe:")
cart.display_cart()

# Ispis ukupne vrednosti korpe
print(f"\nUkupna vrednost za naplatu: {cart.calculate_total()} RSD")
