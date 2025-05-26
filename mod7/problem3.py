#I am so sad I didn't see this problem earlier in the week, I absolutely would have made a massive table for all the pokemon types haha. I love Pokemon. 
atk = input("Is a Fire, Water, or Grass type attacking?")
defender = input("Is a Fire, Water or Grass type defending?")

# changed the name of "input" because that is a python function and I am lazy
def type_advantage(attacker, defender):
    loweratk = attacker.lower()
    lowerdef = defender.lower()
    win = "Super Effective!"
    lose = "Not Very Effective"
    draw = "Neutral"
    if loweratk == "fire":
        if lowerdef == "fire":
            result = draw
        elif lowerdef == "water":
            result = lose
        elif lowerdef == "grass":
            result = win
    elif loweratk == "water":
        if lowerdef == "fire":
            result = win
        elif lowerdef == "water":
            result = draw
        elif lowerdef == "grass":
            result = lose
    elif loweratk == "grass":
        if lowerdef == "fire":
            result = lose
        elif lowerdef == "water":
            result = win
        elif lowerdef == "grass":
            result = draw
    return result


print(type_advantage(atk, defender))
