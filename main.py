import random
import sys
from string import ascii_uppercase, digits
from pick import pick

ascii_string = ascii_uppercase + digits

title = "Select the number of keys to receive:"
options = [
    '10 keys',
    '20 keys',
    '30 keys',
    '40 keys',
    '50 keys',
    '60 keys',
    '70 keys',
    '80 keys',
    '90 keys',
    '100 keys',
    'Exit the program'
]


def getKey():
    x = 0
    key = ''

    while x < 29:
        if x == 5 or x == 11 or x == 17 or x == 23:
            key += '-'
        else:
            key += random.choice(ascii_string)
        x += 1
    return key


def generateKeys(keysCount):
    with open('keys.txt', 'w', encoding='utf-8') as file:
        print("Loading...")
        for i in range(1, keysCount + 1):
            file.write(f"{i}. {getKey()}\n")
        file.close()
        print("Complete!")


if __name__ == "__main__":
    option, index = pick(options, title, indicator='=>', default_index=2)
    match index:
        case 0:
            generateKeys(10)
        case 1:
            generateKeys(20)
        case 2:
            generateKeys(30)
        case 3:
            generateKeys(40)
        case 4:
            generateKeys(50)
        case 5:
            generateKeys(60)
        case 6:
            generateKeys(70)
        case 7:
            generateKeys(80)
        case 8:
            generateKeys(90)
        case 9:
            generateKeys(100)
        case 10:
            sys.exit()
