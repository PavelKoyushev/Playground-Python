class Product:
    def __init__(self, id: int, title: str, price: float, count: int, description: str):
        self.id = id
        self.title = title
        self.price = price
        self.count = count
        self.description = description
        
    def __del__(self):
        print("Product removed ->", self.title)

    def changePrice(self, newPrice: float):
        if newPrice > 100:
            self.price = newPrice
        else:
            print("The price must be greater than 100$!")

    def showProductInfo(self):
        print(f"Title: {self.title}")
        print(f"Price: {self.price}$")
        print(f"Count: {self.count}")
        print(f"Total: {self.count * self.price}$")
        print(f"Description: {self.description}")

