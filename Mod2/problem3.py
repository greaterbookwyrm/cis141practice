import math
a = float (input("What is the first triangle side?"))
b = float (input("What is the second triangle side?"))
c = float (input("What is the third triangle side?"))
s = .5*(a+b+c)
squarethis = s*(s-a)*(s-b)*(s-c)
print(math.sqrt(squarethis))
