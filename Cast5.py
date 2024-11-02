#Intermediate Coding Exercise 1.5
class Customer():
    greeting = "Welcome to Coffee Palace!"
    def __init__(self,name,beverage,food,total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total
    
    def __str__(self):
        return f"Name: {self.name}, Beverage: {self.beverage}, Food: {self.food}, Total: {self.total}"


print(Customer.greeting)
c_1 = Customer("Nate","Espresso","Pastrami on Rye",220)
c_2 = Customer("Elaine","Strawberry frappuccino","Tuna wrap",270)
c_3 = Customer("Samirah","Iced caffe latte","Cinnamon roll",225)
c_4 = Customer("Jerry","Caramel macchiato","Glazed doughnut",230)
c_5 = Customer("Paz","Iced tea","Blueberry pancakes",315)

print(c_2)
print(c_4)

print("")
#Ending of Intermediate Coding Exercise 1.5