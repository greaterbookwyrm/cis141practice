old = (int(input("how old are you?")))
car = (input("are you taking a car across the ferry?"))

# changed the name of "input" because that is a python function and I am lazy
def ferry_fare(age, vehicle):
    lowercar = vehicle.lower()
    cost = 0
    if age <= 19:
        cost = 0
    elif age >= 19:
        if lowercar == "yes":
            cost += 20
        elif lowercar == "no":
            cost += 10
    elif age > 64:
        if lowercar == "yes":
            cost += 15
        elif lowercar == "no":
            cost += 5
    else:
        cost = "Please make sure to use numbers not words for your age, and only Yes or No for if you're taking a car"

    return cost


print(ferry_fare(old,car))
