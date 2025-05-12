sum = 1
while sum > 0:
    counter = int(input("enter a number 0 to stop"))
    if counter > 0:
        print(counter)
    else:
        print("The End")
        break
#I know this isn't 100% correct, you can still technically keep entering numbers after the break point and continue this loop forever, but I'm not sure how to close it
