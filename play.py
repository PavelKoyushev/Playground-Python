from product import Product

product = Product(1, "iPhone 26 Max", 1199.0, 35, "The New iPhone")

product.changePrice(1299.0)

products = [
    product,
    Product(2, "MacBook Pro M5", 1799.0, 15, "Notebook with new M5 chip"),
    Product(3, "Apple Watch XY", 899.0, 21, "New SmartWatch")
]

print("")
for product in products:
    product.showProductInfo()
    print("-" * 40)
print("")
