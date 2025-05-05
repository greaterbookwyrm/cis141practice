"""
A store charges $5 for shipping on any order under $50. 
If the order amount is $50 or more, shipping is free.
Ask the user for the order total and print the total cost, including shipping.
Write your code here :-)
"""

cost = float(input("What was your order total?"))
if cost >= 50:
    print("Your total is " + str(cost))
else:
    total = cost + 5
    print("Your total is " + str(total))
