names = ["Michele", "Robin", "Sara", "Michele"]
names = list(names)
print(names)
names = set(names)
print(names)
names = list(names)
print(names[2])

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
d =[]
def compare(a,b):
    for x in a:
        for y in b:
            if (x==y):
                d.append(x)
    return d
#d = list(compare(a,b))
d = set(compare(a,b))
print(d)
