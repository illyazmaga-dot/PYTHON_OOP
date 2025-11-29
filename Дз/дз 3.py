class Product:
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available

class Cart:
    def __init__(self):
        self.items = []
    def add(self, product):
        if product.available:
            self.items.append(product)
        else:
            print("Товару немає в наявності")
    def remove(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                break
    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
    def show_cart(self):
        for item in self.items:
            print(item.name, "-", item.price)