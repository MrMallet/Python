import random
cows = [0,0,0,0]
check=[]
def ranNum():
    return random.randint(1000,9999)

def guess():
    return input("Guess a 4 digit number: ")

def checkCow(check):
    global cows
    cowCount, bullCount =0,0
    for x in range(len(check)):
        if check[x] ==1 and cows[x] ==1:
            cowCount +=1
        if cows[x] == 1 and check[x] !=1:
            bullCount+=1
    print ("Cows: " ,cowCount, "Bulls: ",bullCount)

def setCow(check):
    global cows
    for x in range(4):
        if check[x] == 1:
            cows[x] = 1
    print (cows)
    print(check)

def compareNums(num,uguess):
    check = [0,0,0,0]
    for x in range(len(num)):
        if num[x] == uguess[x]:
            check[x] = 1
    setCow(check)
    checkCow(check)


if __name__=="__main__":
    print("Welcome to the cows and bulls game")
    num=list(str(ranNum()))
    print(num)
    while(check != [1,1,1,1]):
        uguess=list(guess())
        compareNums(num, uguess)
    print("Congratulations, you guessed right!!!")
