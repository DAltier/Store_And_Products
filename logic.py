import store
import product

market = store.Store(name = "Market")
strawberries = product.Product(name = "strawberries", price = 10, category = "fruit")
oranges = product.Product(name = "oranges", price = 10, category = "fruit")
apples = product.Product(name = "apples", price = 10, category = "fruit")
broccoli = product.Product(name = "broccoli", price = 10, category = "vegetables")
asparagus = product.Product(name = "asparagus", price = 10, category = "vegetables")
potato = product.Product(name = "potato", price = 10, category = "vegetables")
yogurt = product.Product(name = "yogurt", price = 10, category = "dairy")
butter = product.Product(name = "butter", price = 10, category = "dairy")
milk = product.Product(name = "milk", price = 10, category = "dairy")

market.add_product(strawberries).add_product(oranges).add_product(apples)
market.add_product(broccoli).add_product(asparagus).add_product(potato)
market.add_product(yogurt).add_product(butter).add_product(milk)

for product in market.products :
    product.print_info()
print("*" * 80)

market.sell_product(1).set_clearance("fruit", 20)

print("*" * 80)
for product in market.products :
    product.print_info()

