num = int(input("Find prime numbers up to: "))
bot, top = 1,num+1
b =[]
a = range(bot,top)

def mod(checkNum):
    CheckNumRange=[]
    CheckNumRange= range(2,checkNum)
    prime = True
    #print(CheckNumRange)
    for x in CheckNumRange:
        #print(x)
        #print(checkNum)
        if(checkNum % x == 0):
            #print("this has divisors")
            prime = False
            break
            #y = int(num/x)
            #if(y<x):    #if y is less than x stop
                #print("y is greater than x")
                #break
    return prime

for x in a:
    if (mod(x)== True):
        b.append(x)
print(b)
#print(b.amount)


#if we were looking for prime numbers we could use a
#modified version of this for each number. modifications
#would include compulsory identifying of y so that it
#could be compared to x. additionally we want it to break
# once it finds a divisor but only out to the outer loop
#and on to the next number.
