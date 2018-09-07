word = input("Is your word a palindrome: ")
def checkWord(word):
    revWord = word[::-1]
    if (word == revWord):
        print ("is a palindrome")
    else: print("is not palindrome")
checkWord(word)
