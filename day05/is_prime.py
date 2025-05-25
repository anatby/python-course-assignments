import math
num = int(input("please enter a whole number"))
for i in range(2, int(math.sqrt(num))):
  if num % i == 0:
    print("not prime")
    break
print("prime")
