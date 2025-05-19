random = [
    "Lorem",
    "ipsum",
    "dolor",
    "sit",
    "Olympic",
    "Olympic",
    "amet",
    "consectetur",
    "adipiscing",
    "elit",
    "Quisque",
    "faucibus",
    "ex",
    "sapien",
    "vitae",
    "pellentesque",
    "sem",
    "placerat",
    "Olympic",
    "Olympic",
    "Olympic",
    "Olympic",
    "Olympic",
]
counter = []
for item in random:
    if len(item) >= 4:
        counter.append(item)
print(counter)
