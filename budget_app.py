class Category:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    def deposit(self, amount):
        if(amount > 0):
            self.amount = self.amount + amount
            return "You have successfully deposited {:.2f} in category {}".format(self.amount, self.category)
        else:
            return "Deposit must be greater than zero!"

    def withdraw(self, amount):
        if(amount > 0 and self.amount >= amount):
            self.amount = self.amount - amount
            return "You have successfully withdrawn {:.2f} from category {}".format(self.amount, self.category)
        else:
            return "Invalid amount, check input and/or balance"
        
    def check_balance(self, amount):
        if(amount <= self.amount):
            return True
        else:
            return False

    def transfer(self, amount, category):
        if(amount > 0 and category.amount >= amount):
            category.amount = category.amount - amount
        else:
            return "Insuficcient amount or invalid input"

        current_amount = self.amount
        self.amount = self.amount + amount
        return "Successfully transfered {:.2f} from {} and now you have {:.2f} in category {}".format(amount, category.category, self.amount, self.category )


food_category = Category("Food", 400)
clothing_category = Category("Clothing", 200)
car_category = Category("Car Expenses", 500)

print("Amount in food is {}".format(food_category.amount))
print("Amount in clothing is {}".format(clothing_category.amount))
print("Amount in car expenses is {}".format(car_category.amount))
print("\n")
print(food_category.deposit(100))
print(clothing_category.withdraw(100))
print(car_category.check_balance(100))
print(food_category.transfer(50, clothing_category))
print("\n")
print("Amount in food is now {}".format(food_category.amount))
print("Amount in clothing is now {}".format(clothing_category.amount))
print("Amount in car expenses is now {}".format(car_category.amount))
        
        