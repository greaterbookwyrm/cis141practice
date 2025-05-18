##1. Create a list of integers (you get to pick!). Write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
# I think this is right? I am not sure what "Iterate through the list" means? 
# I absolutely almost missed that I should be only calculating the even numbers AGAIN- glad I double checked the questions. 
pi = [3,141,5,92,6,53,5,8,97,9,3,238,46,26,4,3,383,279,5,2,8,41,97,1] 
even_total=0
for item in pi:
    if item % 2 == 0:
        even_total += item
print(even_total)
