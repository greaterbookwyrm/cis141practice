#I am upset with how long it took me to do this because of simple spelling errors
test = input("What word should I count the vowels for?")

# changed the name of "input" to "thing" because that is a python function and I am lazy
def count_vowels(thing):
    lowerthing = thing.lower()
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for char in lowerthing:
        if char == "a":
            a += 1
        elif char == "e":
            e += 1
        elif char == "i":
            i += 1
        elif char == "o":
            o += 1
        elif char == "u":
            u += 1
    return (
        "the number of\nAs: "
        + str(a)
        + "\nEs: "
        + str(e)
        + "\nIs: "
        + str(i)
        + "\nOs: "
        + str(o)
        + "\nUs: "
        + str(u)
    )


print(count_vowels(test))

