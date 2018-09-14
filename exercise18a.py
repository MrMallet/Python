import random
cows = [0,0,0,0]
check=[]
def ranNum():
    return random.randint(1000,9999)

def guess():
    return input("Guess a 4 digit number: ")



def compareNums(num,uguess):
    cowCount, bullCount =0,0
    for x in range(len(num)):
        if num[x] == uguess[x]:
            cowCount+= 1
        elif uguess[x] in num:
            bullCount+=1
    return cowCount, bullCount




if __name__=="__main__":
    print("Welcome to the cows and bulls game")
    num=list(str(ranNum()))
    print(num)
    cowCount, guessCount = 0,0
    while(cowCount != 4):
        uguess=list(guess())
        guessCount+=1
        cowCount, bullCount = compareNums(num, uguess)
        print ("Cows: " ,cowCount, "Bulls: ",bullCount)
    print("Congratulations, you guessed right in ", guessCount, " goes!!!")
