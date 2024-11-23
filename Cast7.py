import os

'''
#Intermediate Coding Exercise 3.4
Try = open("exercise.txt", "w")
Try.write("I like the flexibility of coding in Python.")
Try = open("exercise.txt", "a")
Try.write("\n I want to learn Data Analysis after learning Python.")
Try.write("\n I plan on applying everything that I've learned in every projects that I'm going to build.")
Try.write("\n My goals are to be successful and to have control over my time.")

Try = open("exercise.txt", "r")
print(Try.read())
Try.close
#Ending Intermediate Coding Exercise 3.4
'''

'''
Try = open("exercise.txt", "r")

print(Try.read())

print(Try.readline())

for x in Try:
    print(x)

Try.close()
'''

if os.path.exists("exercise.txt"):
    os.remove("exercise.txt")
else:
    print("File does not exist")