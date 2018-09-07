import math
num = int(input("Find prime numbers up to: "))
bot, top = 1,num+1
b =[]
a = range(bot,top)

def mod(checkNum):
    CheckNumRange= range(2,(int((math.sqrt(checkNum)))+1))
    prime = True
    for x in CheckNumRange:
        if(checkNum % x == 0):
            prime = False
            break
    return prime

for x in a:
    if (mod(x)== True):
        b.append(x)
print(b)
print(len(b))


#maybe if i use the square root function i can cap the
#upper end of my list

#if the number doesnt have any divisors it will check on
#every number between 1 and it. waste of time. by the
#time we get to five the possible divisors is down by 4/5ths


#if we were looking for prime numbers we could use a
#modified version of this for each number. modifications
#would include compulsory identifying of y so that it
#could be compared to x. additionally we want it to break
# once it finds a divisor but only out to the outer loop
#and on to the next number.
