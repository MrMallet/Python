import random
a= random.randint(1,100)
counter =0
#print(a)
#print("Do you want to play a game? Guess a number between 1 and 10: ")

def Uguess():
    global counter
    guess = int(input("Guess a number between 1 and 100: "))
    counter+=1
    check(guess)

def check(guess):
    global a
    global counter
    if a==guess:
        print("Good Guess, you won in ",counter, " tries.")
    elif a> guess:
        print("Higher")
        Uguess()
    elif a<guess:
        print("Lower")
        Uguess()

Uguess()
