exp = (int(input("how much exp do you have?")))

def level_up(experience):
    level = ""
    if experience <= 99:
        level = "You are level 1"
    elif experience <= 199:
        level = "You are level 2"
    elif experience >= 200:
        level = "you are level 3! Or higher!"
    else:
        cost = "Please make sure to use numbers not words"

    return level


print(level_up(exp))
