num1, num2 = 0,1
highNum = int(input("Please input number of fibonacci iterations: "))
fiblist =[]

for x in range(highNum):
    fiblist.append(num1)
    num1, num2 = num2, num1+num2

print(fiblist)
