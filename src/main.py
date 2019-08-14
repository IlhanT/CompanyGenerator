from random import randrange
import json

# Constants
NAMES = json.loads(open('names.json').read())
TYPES = json.loads(open('types.json').read())

# Variables
industry = str(input("Put in the industry your company is based on."))


# Create company function
def create_company(industry):
    returnname = ''

    # The size of the names.json array
    maxposnames = randrange(11)
    # The size of the types.json array
    maxpostypes = randrange(7)

    currentposition = 0

    for name in NAMES:
        if currentposition == maxposnames:
            returnname = name
            currentposition = 0
            break

        currentposition += 1

    returnname = returnname + " " + industry

    for type in TYPES:
        if currentposition == maxpostypes:
            returnname = returnname + " " + type
            break

        currentposition += 1

    return returnname


print(create_company(industry))
