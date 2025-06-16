counter = 0 
while counter == 0:
    print("To stop putting trails into the list, type in 0")
    hikes = input("what trail did you go on?")
    if hikes == "0":
        with open("hiking_log.txt", "r") as ending:
            print(ending.read())
        counter += 1
    else: 
        miles = input("How many miles was it?")
        with open("hiking_log.txt", "a") as hiking_log:
            hiking_log.write(hikes + "\t")
            hiking_log.write(miles +"\n")
