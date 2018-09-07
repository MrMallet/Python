import math
def getNum():
    return int(input("Check a number to see if its prime: "))

def mod(num):
    CheckNumRange= range(2,(int((math.sqrt(num)))+1))
    prime = True
    for x in CheckNumRange:
        if(num % x == 0):
            prime = False
            break
    return prime

if mod(getNum()):
    print("This is prime")
else:
    print("This is not prime")
