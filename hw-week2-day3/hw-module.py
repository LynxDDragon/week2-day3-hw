#Module should have the following capabilities:

#1) Has a function to calculate the square footage of a house
#Reminder of Formula: Length X Width == Area

#2) Has a function to calculate the circumference of a circle

#Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

def squared_feet(num1, num2):
    return num1 * num2

def findCircum(rad):
    return 3.14*rad*rad

print("Enter Radius of Circle: ", end="")
r = float(input())

c = findCircum(r)
print("\nCircumference = {:.2f}".format(c))