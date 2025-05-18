pi =[-3,141,5,-92,-6,-53,5,8,-97,9,-3,238,-46,26,-4,3,-383,279,-5,-2,-8,41,-97,1] 
pos_counter=0
neg_counter=0
for i in pi:
    if i>0:
        pos_counter+=1 
    if i<0:
        neg_counter+=1
print("The number of positive numbers is",pos_counter)
print("The number of negative numbers is",neg_counter)
