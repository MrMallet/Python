import random
a = random.sample(range(100),5)
b = random.sample(range(100),10)

print(a)
print(b)

list=[x*y for x in a for y in b if x*y %2 != 0]
print(list)
