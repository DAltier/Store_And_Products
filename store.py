class Store :
    def __init__(self, name, products = []) :
        self.name = name
        self.products = products
    
    def add_product(self, new_product) :
        self.products.append(new_product)
        return self

    def sell_product(self, id) :
        found = False
        for product in self.products :
            if product.id == id :
                print("Sold:")
                self.products[id].print_info()
                del self.products[id]
                found = True
        if not found :
            print("Product id not found")
        return self

    def inflation(self, percent_increase) :
        for product in self.products :
            product.update_price(percent_increase, True)
        return self 

    def set_clearance(self, category, percent_discount) :
        for product in self.products :
            if product.category == category :
                product.update_price(percent_discount, False)
        return self
    