#Intermediate Coding Exercise 2.4
Flavor = ["Vanilla", "Chocolate", "Strawberry", "Cookies N' Cream", "BubbleGum"]
Toppings = ["Almonds", "Banana Slices", "Chocolate Syrup", "Caramel Syrup", "White Chocolate Chips"]

ice_cream = dict(zip(Flavor, Toppings))
print (ice_cream)

ice_cream["Chocolate"] = "BlueBerries"
ice_cream.update ({"Matcha" : "Pistachios", "Ube" : "Mango Slices"})
print(ice_cream)
#Ending Intermediate Coding Exercise 2.4

#Intermediate Coding Exercise 2.8
groceries = {"Chicken" : 8, "Apples" : 6, "Cucumbers" : 3, "Milk" : 2, "Oranges" : 4}
groceries.pop("Oranges")

print(groceries)

speakers = {"Sir Rafael" : 54, "Ms. Joan" : 33, "Ms. Dana" : 67}
names = speakers.keys()
print(names)

Results = {
    "Carl": "passed",
    "Quentin": "failed",
    "John Y.": "passed",
    "Peter": "failed",
    "Max T.": "passed",
    "Joseph": "passed",
    "Jone": "failed",
    "Jorge": "failed",
    "George": "passed",
    "Ben": "passed",
    "Jerome": "passed",
    "Rick": "failed",
    "Max G.": "failed",
    "John P.": "failed",
    "Vince": "passed"
}

print(Results.get("Jorge"))
