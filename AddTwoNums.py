# Add Two Numbers in Python
# Author: Ziheng Wang
# Using a function
# function to add two numbers
def add(a, b):
    # converting input to float and adding
    result = float(a) + float(b)
    return result
# taking user input
a = input("First Number: ")
b = input("Second Number: ")
# calling function
res = add(a, b)
print("The Answer is: ")
print(res)
