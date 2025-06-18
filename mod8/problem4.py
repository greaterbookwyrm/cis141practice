vote_counts = {}
with open("poll.txt", "r") as file:
    for word in file:
        text = file.read().lower() 
        yeacount = text.split().count("yea")
        naycount = text.split().count("nay")
        vote_counts["yea"] = yeacount
        vote_counts["nay"] = naycount

print(vote_counts)
#this was significantly easier to do after I understood problem 3. 
