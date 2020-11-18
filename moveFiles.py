### soporta gp3, gp4, gp5
### afinaciones: Standard E, Standard Eb, Standard D, Standard C,Drop D, Drop Db/C#, Drop C

## falta guitarras de 7 cuerdas

import guitarpro
import shutil
import os
import math

def moveFile(gpFile , tuning, fileCount, filesToTest, UI):

    global tabsMoved
    if not os.path.isdir(tuning):
        os.mkdir(tuning)
    
    print("[ " + str(fileCount) + " / " + str(len(filesToTest)) + " ]" + " -> " + tuning + " found !")

    shutil.move(gpFile, tuning)

    tabsMoved += 1  

    progress = math.floor((fileCount / len(filesToTest))*100)
    UI.prog.update(progress) 

def main(direction, UI):

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
    files = os.listdir(os.path.abspath(direction))
    filesToTest = []

    for file in files:
        if file.endswith(('.gp5', '.gp4', '.gp3')):
            filesToTest.append(file)

    for gpFile in filesToTest:

        fileDirection = direction + "\\" + gpFile

        try:
            song = guitarpro.parse(fileDirection)
        except:
            print("error reading file - " + str(gpFile))
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
            moveFile(fileDirection, "Standard B", fileCount, filesToTest, UI)
            quantityOfStandardB += 1
            UI.changeSong(gpFile)

        # move Drop B
        elif dropBcount >= 1:
            moveFile(fileDirection, "Drop B", fileCount, filesToTest, UI)
            quantityOfDropB += 1
            UI.changeSong(gpFile)

        # move Standard C
        elif standardCcount >= 1:
            moveFile(fileDirection, "Standard C", fileCount, filesToTest, UI)
            quantityOfStandardC += 1
            UI.changeSong(gpFile)

        # move Drop C
        elif dropCcount >= 1:
            moveFile(fileDirection, "Drop C", fileCount, filesToTest, UI)
            quantityOfDropC += 1
            UI.changeSong(gpFile)

        # move Standard D
        elif standardDcount >= 1:
            moveFile(fileDirection, "Standard D", fileCount, filesToTest, UI)
            quantityOfStandardD += 1
            UI.changeSong(gpFile)

        # move Drop D
        elif dropDcount >= 1:
            moveFile(fileDirection, "Drop D", fileCount, filesToTest, UI)
            quantityOfDropD += 1
            UI.changeSong(gpFile)

        # move Drop Db
        elif dropDbcount >= 1:
            moveFile(fileDirection, "Drop Db", fileCount, filesToTest, UI)
            quantityOfDropDb += 1
            UI.changeSong(gpFile)

        # move Standard Eb
        elif standardEbcount >= 1:
            moveFile(fileDirection, "Standard Eb", fileCount, filesToTest, UI)
            quantityOfStandardEb += 1
            UI.changeSong(gpFile)
            
        # move Standard E
        elif standardEcount >= 1:
            moveFile(fileDirection, "Standard E" , fileCount, filesToTest, UI)
            quantityOfStandardE += 1
            UI.changeSong(gpFile)

        else:
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

    if tabsMoved  == 0:
        effectiveness = "100%"        
    else:
        effectiveness = str((tabsMoved / fileCount) * 100) + "%"
        
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

    print()

    print(" effectiveness:     ", effectiveness)


if __name__ == "__main__":

    main(direction, UI)


    