#fibonacci... using functions
num1, num2 = 0,1
fiblist=[]
def getNum():
    return int(input("How many iterations of the fibonacci sequence do you want: "))

def fib():
    global num1, num2#, fiblist***dont need to declare as list.append is a method call
    fiblist.append(num1)
    num1, num2 = num2, num1+num2

for i in range(getNum()):
    fib()
print(fiblist)
