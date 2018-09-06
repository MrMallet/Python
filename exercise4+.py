num = int(input("Enter a number to find its divisors: "))
bot, top= 1,num+1
b =[]
a = range(bot,top)
for x in a:
    if(num % x == 0):
        y = int(num/x)
        if(y<x):    #if y is less than x stop
            break
        b.append(x)
        b.append(y)

print(b)

#if we were looking for prime numbers we could use a
#modified version of this for each number. modifications
#would include compulsory identifying of y so that it
#could be compared to x. additionally we want it to break
# once it finds a divisor but only out to the outer loop
#and on to the next number.



#for speeds sake if we divide by 2 and there is/isnt a
#modulo then we have sorted the list so that theres no
#need to search the top half of the list as any number
#higher that half of the number cannot be multiplied by
#the smallest number that is 2. If we try modulos 3 and
#we get an approximation of a third we can discount the
#upper end 2/3s

#Enter a number to find its divisors: 3453634
#[1, 2, 23, 46, 75079, 150158, 1726817, 3453634]

#In the above example there are four pairs of divisors
#1, 3453634
#2, 1726817
#23, 150158
#46, 75079

#from the first two pairs we can see both 1 and 2 are
#divisors and the range between their divisors have
#to be divided by a float between 1 and 2 in order to
#find their corresponding divisorsself.
#By the time we get down to the 3rd pair we find our
#next divisors is 23 and 150158. there is no need to
#search lower than 23 because weve already modulos
#divided all numbers below that, additionally theres
#no need to searh higher than 150158.
#By this stage we could have cut down our searching
#list to less than 1/23(approx 4-5%) meaning we would
#save near 95% in just our first 20-25 searches. The
#gains going forward with such an algorithm would taper
#off as the divisors get closer together.
#At 46, 75079, after just 46 searches we are at 2% of
#the range, concentrating on the range of 46 - 75079.
