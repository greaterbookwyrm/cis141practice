with open("song_lyrics.txt", "r") as file:
    text = file.read().lower() 

words_to_count = []
for i in range(5):
    word = input(f"Enter word {i+1} to count: ").strip().lower()
    words_to_count.append(word)

word_counts = {}
for word in words_to_count:
    count = text.split().count(word)
    word_counts[word] = count

print("\nWord Frequencies:")
print(word_counts)
#I had to ask for help on this one from a friend of mine- and it took me significantly longer than I would have liked to fully understand this. 
