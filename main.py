

from product_manager import ProductManager
from product import Product

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje nekoliko proizvoda
product1 = Product(name="Televizor", price=55555, quantity=3)
product2 = Product(name="Frižider", price=33333, quantity=2)
product3 = Product(name="Mikrotalasna", price=11111, quantity=5)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)



