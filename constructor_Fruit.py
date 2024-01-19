class Fruit:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
name = input('Enter fruit name: ').strip().capitalize()
quantity = int(input('Enter quantity: '))
price = float(input('Enter price: '))

userInput = Fruit(name,quantity,price)

print('Name:',name)
print('Quantity:',quantity)
print('Price:',price)
