### soporta gp3, gp4, gp5
### afinaciones: Standard E, Standard Eb, Standard D, Standard C,Drop D, Drop Db/C#, Drop C

## falta guitarras de 7 cuerdas

import guitarpro
import shutil
import os
import math

def copyFile(gpFile , tuning, fileCount, filesToTest, UI, fileDirectionOutput):

    global tabsMoved

    pathToCopy = os.path.join(fileDirectionOutput, tuning)


    if not os.path.isdir(pathToCopy):
        os.makedirs(pathToCopy)

    shutil.copy(gpFile, pathToCopy)

    tabsMoved += 1   

    progress = math.floor((fileCount / len(filesToTest))*100)
    UI.prog.update(progress)

def main(directionInput,directionOutput, UI):

    global tabsMoved
    global errorFiles

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

    errorFiles = []
    fileCount = 0
    tabsMoved = 0
    
    files = os.listdir(os.path.abspath(directionInput))
    filesToTest = []

    for file in files:
        if file.endswith(('.gp5', '.gp4', '.gp3')):
            filesToTest.append(file)

    for gpFile in filesToTest:

        fileDirectionInput = os.path.join(directionInput, gpFile)
        fileDirectionOutput = directionOutput

        try:
            song = guitarpro.parse(fileDirectionInput)
        except:
            errorFiles.append(gpFile)
            continue

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

        tracks = (track for track in song.tracks)
        
        for track in tracks:
            if (track.isPercussionTrack == False):

                strings = track.strings

                for string in strings:

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

        # move Standard B
        if standardBcount >= 1:
            copyFile(fileDirectionInput,"Standard B", fileCount, filesToTest, UI, fileDirectionOutput)
            quantityOfStandardB += 1
            UI.changeSong(gpFile)

        # move Drop B
        elif dropBcount >= 1:
            copyFile(fileDirectionInput,"Drop B", fileCount, filesToTest, UI, fileDirectionOutput)
            quantityOfDropB += 1
            UI.changeSong(gpFile)

        # move Standard C
        elif standardCcount >= 1:
            copyFile(fileDirectionInput,"Standard C", fileCount, filesToTest, UI, fileDirectionOutput)
            quantityOfStandardC += 1
            UI.changeSong(gpFile)
        # move Drop C
        elif dropCcount >= 1:
            copyFile(fileDirectionInput,"Drop C", fileCount, filesToTest, UI, fileDirectionOutput)
            quantityOfDropC += 1
            UI.changeSong(gpFile)

        # move Standard D
        elif standardDcount >= 1:
            copyFile(fileDirectionInput,"Standard D", fileCount, filesToTest, UI, fileDirectionOutput)
            quantityOfStandardD += 1
            UI.changeSong(gpFile)

        # move Drop D
        elif dropDcount >= 1:
            copyFile(fileDirectionInput,"Drop D", fileCount, filesToTest, UI, fileDirectionOutput)
            quantityOfDropD += 1
            UI.changeSong(gpFile)

        # move Drop Db
        elif dropDbcount >= 1:
            copyFile(fileDirectionInput,"Drop Db", fileCount, filesToTest, UI, fileDirectionOutput)
            quantityOfDropDb += 1
            UI.changeSong(gpFile)

        # move Standard Eb
        elif standardEbcount >= 1:
            copyFile(fileDirectionInput,"Standard Eb", fileCount, filesToTest, UI, fileDirectionOutput)
            quantityOfStandardEb += 1
            UI.changeSong(gpFile)
            
        # move Standard E
        elif standardEcount >= 1:
            copyFile(fileDirectionInput,"Standard E" , fileCount, filesToTest, UI, fileDirectionOutput)
            quantityOfStandardE += 1
            UI.changeSong(gpFile)

        else:
            copyFile(fileDirectionInput,"unknown" , fileCount, filesToTest, UI, fileDirectionOutput)
            UI.changeSong(gpFile)
            errorFiles.append(gpFile)

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

        fileCount += 1



    