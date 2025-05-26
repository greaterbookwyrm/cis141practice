#I decided to be a little extra and include an input prompt :) 
test = (input("What word is a Palendrome?"))


def is_palendrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return lower_s == flipped_s


print(is_palendrome(test))
