import random
a = random.sample(range(100),5)
b=[]
c=[]
def getFirst(a):
    return a[0]
def getLast(a):
    return a[len(a)-1]

print(a)
b.append(getFirst(a))
b.append(getLast(a))
print(b)
c=[getFirst(a),getLast(a)]
print(c)
