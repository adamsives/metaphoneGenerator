import json
import requests
import datetime
import random
import string

#URL for test names
nameURL = 'https://randomuser.me/api/?results='
numPersons = '10'

#call endpoint to get random names
response = requests.get(nameURL + numPersons)
randomNameListRaw = response.json()

# parse x:
for testPerson in randomNameListRaw["results"]:
    givenName = testPerson["name"]["first"]
    #middleName =  TODO:
    familyName = testPerson["name"]["last"]
    gender = testPerson["gender"]
    dob = testPerson["dob"]["date"]
    dobYear = dob[0:4]
    dobDay = dob[5:7]
    dobMonth = dob[8:10]
    postcode = random.randint(2000,2999)
    id = sourceSystemID()

def random_alphaNumeric_string(lettersCount, digitsCount):
    sampleStr = ''.join((random.choice(string.ascii_letters) for i in range(lettersCount)))
    sampleStr += ''.join((random.choice(string.digits) for i in range(digitsCount)))
    
    # Convert string to list and shuffle it to mix letters and digits
    sampleList = list(sampleStr)
    random.shuffle(sampleList)
    finalString = ''.join(sampleList)
    return finalString

def sourceSystemID():
    selectorInt = random.randint(1,5)
    global src

    if selectorInt == 1:
        src = "CP-"
    elif selectorInt == 2:
        src = "H-"
    elif selectorInt == 3:
        src = "OOHC-"
    elif selectorInt == 4:
        src = "ROD-"
    else:
        src = "SH-"

    return src + random_alphaNumeric_string(5,5)

