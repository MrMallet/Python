a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
num= int(input("input a number: "))
for x in a:
    if(x < num):
        #print(x)
        b.append(x)
print(b)
