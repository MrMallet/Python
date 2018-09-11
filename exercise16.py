import random
import string

characters= string.ascii_letters + string.punctuation + string.digits
#characters is 94 characters long and looks like:
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789

def password():
    global characters
    length=random.randint(8,16)
    print(length)
    list =[]
    for i in range(length):
        list.append(characters[random.randint(0,93)])

    list= ("".join(list))
    return list

print(password())

#print(characters)
#print(len(characters))
