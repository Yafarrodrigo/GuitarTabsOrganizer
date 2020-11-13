### soporta gp3, gp4, gp5
### afinaciones: Standard E, Standard Eb, Standard D, Standard C,Drop D, Drop Db/C# Drop C
## 18 de 22 acertadas :)

## falta guitarras de 7 cuerdas

import guitarpro
import shutil
import os

sixthStringValue = 0
standardEcount = 0
standardEbcount = 0
standardDcount = 0
standardCcount = 0
standardBcount = 0
dropDcount = 0
dropDbcount = 0
dropCcount = 0
dropBcount = 0

quantityOfStandardE = 0
quantityOfStandardEb = 0
quantityOfStandardD= 0
quantityOfStandardC = 0
quantityOfStandardB = 0
quantityOfDropD = 0
quantityOfDropDb = 0
quantityOfDropC = 0
quantityOfDropB = 0

## FUNCTIONS
def moveFile(gpFile , tuning):

    global quantityOfStandardE
    global quantityOfStandardEb
    global quantityOfStandardD
    global quantityOfStandardC
    global quantityOfStandardB
    global quantityOfDropD
    global quantityOfDropDb
    global quantityOfDropC
    global quantityOfDropB

    if not os.path.isdir(tuning):
        os.mkdir(tuning)

    if tuning == "Standard E":
        quantityOfStandardE += 1
    elif tuning == "Standard Eb":
        quantityOfStandardEb += 1
    elif tuning == "Standard D":
        quantityOfStandardD += 1
    elif tuning == "Standard C":
        quantityOfStandardC += 1
    elif tuning == "Standard B":
        quantityOfStandardB += 1                 
    elif tuning == "Drop D":
        quantityOfDropD += 1
    elif tuning == "Drop Db":
        quantityOfDropDb += 1        
    elif tuning == "Drop C":
        quantityOfDropC += 1
    elif tuning == "Drop B":
        quantityOfDropB += 1
    
    print("[ " + str(fileCount) + " / " + str(len(filesToTest)) + " ]" + " -> " + tuning + " found !")
    shutil.move(gpFile, tuning)    

def resetTuningCount():
    global sixthStringValue
    global standardEcount
    global standardEbcount
    global standardDcount
    global standardCcount
    global standardBcount
    global dropDcount 
    global dropDbcount 
    global dropCcount 
    global dropBcount 

    sixthStringValue = 0
    standardEcount = 0
    standardEbcount = 0
    standardDcount = 0
    standardCcount = 0
    standardBcount = 0
    dropDcount = 0
    dropDbcount = 0
    dropCcount = 0
    dropBcount = 0

def checkTuning(string):
    global sixthStringValue
    global standardEcount
    global standardEbcount
    global standardDcount
    global standardCcount
    global standardBcount
    global dropDcount
    global dropDbcount
    global dropCcount
    global dropBcount

    # checks if its in Standard E
    if (string.number == 6) and (string.value == 40):
        sixthStringValue  = string.value

    elif (string.number == 5) and (string.value == 45) and (sixthStringValue == 40):
        standardEcount += 1

    # checks if its in Standard Eb
    elif (string.number == 6) and (string.value == 39):
        sixthStringValue  = string.value

    elif (string.number == 5) and (string.value == 44) and (sixthStringValue == 39):
        standardEbcount += 1

    # checks if sixth string is D
    elif (string.number == 6) and (string.value == 38):
        sixthStringValue  = string.value

    # check if its in Standard D
    elif (string.number == 5) and (string.value == 43) and (sixthStringValue == 38):
        standardDcount += 1   

    # check if its in Drop D
    elif (string.number == 5) and (string.value == 45) and (sixthStringValue == 38):
        dropDcount += 1  

    # check if its in Drop Db
    elif (string.number == 6) and (string.value == 37):
        sixthStringValue  = string.value

    elif (string.number == 5) and (string.value == 44) and (sixthStringValue == 37):
        dropDbcount += 1

    # check if sixth string is C
    elif (string.number == 6) and (string.value == 36):
        sixthStringValue  = string.value

    # checks if its in Drop C
    elif (string.number == 5) and (string.value == 43) and (sixthStringValue == 36):
        dropCcount += 1

    # check if sixth string is B
    elif (string.number == 6) and (string.value == 35):
        sixthStringValue  = string.value

    # check if its in Drop B
    elif (string.number == 5) and (string.value == 42) and (sixthStringValue == 35):
        dropBcount += 1

    # check if its in Standard B
    elif (string.number == 5) and (string.value == 40) and (sixthStringValue == 35):
        standardBcount += 1

    # or standard C
    elif (string.number == 5) and (string.value == 41) and (sixthStringValue == 36):
        standardCcount += 1 


files = os.listdir(os.path.abspath(os.getcwd()))
filesToTest = []
fileCount = 0

for file in files:
    if file.endswith(('.gp5', '.gp4', '.gp3')):
        filesToTest.append(file)

for gpFile in filesToTest:

    try:
        song = guitarpro.parse(gpFile)
    except:
        print("error reading file - " + str(gpFile))

    resetTuningCount()

    tracks = (track for track in song.tracks)
    
    for track in tracks:
        if (track.isPercussionTrack == False):

            strings = track.strings

            for string in strings:

                checkTuning(string)


    # move Standard E
    if standardEcount >= 1:
        resetTuningCount()
        moveFile(gpFile, "Standard E")

    # move Standard Eb
    if standardEbcount >= 1:
        resetTuningCount()
        moveFile(gpFile, "Standard Eb")
        
    # move Standard D
    if standardDcount >= 1:
        resetTuningCount()
        moveFile(gpFile, "Standard D")

    # move Standard C
    if standardCcount >= 1:
        resetTuningCount()
        moveFile(gpFile, "Standard C")

    # move Standard B
    if standardBcount >= 1:
        resetTuningCount()
        moveFile(gpFile, "Standard B")

    # move Drop D
    if dropDcount >= 1:
        resetTuningCount()
        moveFile(gpFile, "Drop D")

    # move Drop Db
    if dropDbcount >= 1:
        resetTuningCount()
        moveFile(gpFile, "Drop Db")

    # move Drop C
    if dropCcount >= 1:
        resetTuningCount()
        moveFile(gpFile, "Drop C")
    
    # move Drop B
    if dropBcount >= 1:
        resetTuningCount()
        moveFile(gpFile, "Drop B")

    fileCount += 1


print("[ " + str(fileCount) + " / " + str(len(filesToTest)) + " ]")
print("Finished!")
print("---------------------------------------------------------------------------------")
print(" Standard E found:   " + str(quantityOfStandardE))
print(" Standard Eb found:  " + str(quantityOfStandardEb))
print(" Standard D found:   " + str(quantityOfStandardD))
print(" Standard C found:   " + str(quantityOfStandardC))
print(" Standard B found:   " + str(quantityOfStandardB))
print(" Drop D found:       " + str(quantityOfDropD))
print(" Drop Db found:      " + str(quantityOfDropDb))
print(" Drop C found:       " + str(quantityOfDropC))
print(" Drop B found:       " + str(quantityOfDropB))

input("Press any key to exit")


    