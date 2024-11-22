#Intermediate Coding Exercise 1.5
class Customers:
    greeting = "Welcome to the Coffee Palace!"
    def __init__(self, Name, Beverage, Food, Total):
        self.Name = Name
        self.Beverage = Beverage
        self.Food = Food
        self.Total = Total

    def __str__(self):
        return f"Customer Name: {self.Name}\n Beverage: {self.Beverage}\n Food: {self.Food}\n Total: {self.Total}\n"

c_1 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
c_2 = Customers("Elaine", "Strawberry Frappuccino", "Tuna wrap", 270)
c_3 = Customers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
c_4 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c_5 = Customers("Paz", "Iced tea", "Blueberry pancakes", 315)


print(Customers.greeting)
print(c_2)
print(c_4)
#Ending of Intermediate Coding Exercise 1.5

#Intermediate Coding Exercise 1.9
class ClubMembers():
    def __init__(self, Name, Birthday, Age , Favorite_food, Goal):
        self.Name = Name
        self.Birthday = Birthday
        self.Age = Age
        self.Favorite_food = Favorite_food
        self.Goal = Goal

    def __str__(self):
        return f"Name: {self.Name}\n Birthday: {self.Birthday}\n Age: {self.Age}\n Favorite Food: {self.Favorite_food}\n Goal: {self.Goal}\n"
    
class ClubOfficers(ClubMembers):
    def __init__(self, Name, Birthday, Age, Favorite_food, Goal,Position):
        self.Position = Position
        super().__init__(Name, Birthday, Age, Favorite_food, Goal)

    def __str__(self):
        return f"{super().__str__()}Position: {self.Position}"
    
m_1 = ClubMembers("Tom", "January 16", "14", "Ice Cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", "16", "Beef stroganoff", "To be the world's greatest chef", "Treasurer")

print(m_1)
print(o_4)
#End of Intermediate Coding Exercise 1.9