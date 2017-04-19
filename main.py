# -*- coding: utf-8 -*-


import re

def readFromFile(fileName = "grammer.txt"):


    textFile = open(fileName ,"r")
    grammer = textFile.read()
    textFile.close()

    grammer = grammer.replace(" ","")
    #print("%s" %(grammer))

    return grammer


def stringParser(grammerString = ""):
    parsedList = []

    string = grammerString.split("\n")

    for cell in string:

        line = []

        temp = cell.split("->")
        line.append(temp[0])

        temp = temp[1].split("|")
        line.extend(temp)


        parsedList.append(line)

    return parsedList





def isContexFreeGrammer(grammer = ""):

    regexTemplate = r'(([A-Z]->([a-zA-Z]+|λ)(\|([A-Za-z]+|λ))*)(\n*))*'

    grammerCheck = re.match(regexTemplate ,grammer)

    if grammerCheck and grammer == grammerCheck.group(0):
        print"congrat! grammer is a context free grammer ..."
        return True

    else:
        print"oops! it's not a context free grammer ..."
        #print("\n grammerCheck : %s \n" %grammerCheck.group())
        #print("\n grammer : %s \n" % (grammer))
        return False
