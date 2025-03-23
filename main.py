

from product_manager import ProductManager
from product import Product

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

