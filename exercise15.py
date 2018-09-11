sentence = input("Please input a sentence: \n")

def flipper(sentence):
    senList = sentence.split(" ")
    revList= senList[::-1]
    return (" ".join(revList))

print(flipper(sentence))

#print("Please input a sentence:")
#print("sentence:", sentence)
#senList = sentence.split(" ")
#print(senList)
#revList= senList[::-1]
#print (" ".join(revList))
