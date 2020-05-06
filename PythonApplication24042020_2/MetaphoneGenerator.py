import csv
import requests
import json
import jellyfish
import easygui
import sys

#URL for homophones
homophoneBaseUrl = 'https://api.datamuse.com/words?'
startsWith = 'sp='
soundsLike = 'sl='

#URL for test names
nameURL = 'https://randomuser.me/api/?results='
numPersons = '10'

#1. create a list of words to get potential rhymes with as testName[]
testNames = []
potentialMetaphones = []
#promt user for input test names
filename = easygui.fileopenbox()

if not filename:
    sys.exit()

#eventual output in the same directory
outputFileType = (filename[filename.rfind("."):filename.rfind(".")+5])
outputFile = filename[0: filename.rfind(".")] + "_metaphones" + outputFileType

f = open(outputFile, "w")

with open(filename) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        testNames.append(row[0])

#call endpoint with this test name
    for name in testNames:
        matchFlag = False
        startingLetterParam = startsWith + name[0:2].lower() + '*&'
        soundsLikeLetterParam = soundsLike + name.lower()
        url = homophoneBaseUrl + startingLetterParam + soundsLikeLetterParam
       
        # GET potential rhymes
        response = requests.get(url)
        homophoneList = response.json() #list
    
        if homophoneList:
            for homophone in homophoneList:
                if homophone["score"] > 89 and jellyfish.metaphone(name) == jellyfish.metaphone(homophone["word"]) and name.upper() != homophone["word"].upper():
                    matchFlag = True
                    #print(name + "," + homophone["word"].title())#---------------------------------------debug
                    f.write(name + "," + homophone["word"].title())
                    f.write("\n")
        else:#--------------------------------------------------------------------------------------------debug
            print(name + ":" + "no homophone returned")#--------------------------------------------------debug
            matchFlag = True#--------------------------------------------------debug

        if matchFlag != True:
            print(name + ":" + "no good match")