#Rock, paper, scissors
input1 = ''
input2 = ''
score1, score2 =0,0
def again():
    choice=input("Do you want to play again? Y or N")
    if choice == 'y':
        start()
    else:
        print('Thanks for playing')

def playGame(a,b):
    global score2
    global score1
    if a==b:
        print("Draw Game- No Score")
        print("Player1 score: ", score1)
        print("Player2 score: ", score2)
        again()
    elif a=='r' and b=='p':
        print("Player Two Wins")
        score2 +=1
        print("Player1 score: ", score1)
        print("Player2 score: ", score2)
        #print(score2)
        again()
    elif a=='p' and b =='r':
        print("Player One Wins")
        score1+=1
        print("Player1 score: " , score1)
        print("Player2 score: " , score2)
        again()
    elif a=='p' and b=='s':
        print("Player Two Wins")
        score2+=1
        print("Player1 score: " , score1)
        print("Player2 score: " , score2)
        again()
    elif a=='s' and b=='p':
        print("Player One Wins")
        score1+=1
        print("Player1 score: " , score1)
        print("Player2 score: " , score2)
        again()
    elif a=='r' and b=='s':
        print("Player One Wins")
        score1+=1
        print("Player1 score: " , score1)
        print("Player2 score: " , score2)
        again()
    elif a=='s' and b=='r':
        print("Player Two Wins")
        score2+=1
        print("Player1 score: " , score1)
        print("Player2 score: " , score2)
        again()

def start():
    input1= input("Player one, pick R(rock) or P(paper) or S(scissors): ")
    input2= input("Player two, pick R(rock) or P(paper) or S(scissors): ")
    playGame(input1, input2)

start()
