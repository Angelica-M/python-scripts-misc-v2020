# Angelica Magnussen
# 1001549375
# 12/02/2020
# Windows 10

inputFileName = "Java_input.txt" # inputFileName is the name of the input file

# OPEN & READ FILE, THEN STORE THE FILE LINES IN A STRING ARRAY
fileObject = open(inputFileName, "r") # fileObject is a reference to the input file
tempStr = fileObject.read() # tempStr is a String that contains the entire contents of the input file
fileLineArray = tempStr.split("\n") # fileLineArray is a String array whose elements are the text lines of the input file

# READ EACH CHARACTER IN THE ORDER IT APPEARS IN FILE & TAKE APPROPRIATE ACTION
def getLastNestedValue(nestLevelArray, index): # getLastNestedValue() returns the nested bracket level of the file line nestLevelArray[index] before any characters on that line are read
    if index == 0: # If nestLevelArray[index] is the 1st file line, then...
        return nestLevelArray[index] # Return 0 as nestLevelArray[index=0] is 0
    else: # If nestLevelArray[index] is not the 1st file line, then...
        return nestLevelArray[index-1] # Return the nested bracket level of the line before it

nestLevelArray = [] # nestLevelArray is a dynamic array that houses the nested-bracket-level of every Java code line
for index in range(0, len(fileLineArray)-1): # Initialize nestLevelArray
    nestLevelArray.append(0) # For every file line, add an element of value 0 to nestLevelArray

def isCharAQuote(char): # isCharAQuote() returns 1 if char is a quote character, 0 otherwise
    if (char == "\"") | (char == "\'") : # If char is a quote (single or double) symbol, then...
        return 1 # Return true (1)
    else: # If char is not a quote (single or double) symbol, then...
        return 0 # Return false (0)

def flipVar(var): # flipVar() returns 1 (true) if var is 0 (false), 0 (false) otherwise
    if var == 0 : # If var is 0 (false), then...
        return 1 # Return true (1)
    else: # If var is 1 (true), then...
        return 0 # Return false (0)

global shouldIgnoreBrackets # Declare shouldIgnoreBrackets global, shouldIgnoreBrackets determines when the program should count brackets
shouldIgnoreBrackets = 0 # shouldIgnoreBrackets is set to 0 (false) by default
for index in range(0, len(fileLineArray)-1): # For every file line (index) in fileLineArray, read each character and determine what the nested bracket level of that line is
    # Value in nestLevelArray[index] is the nested bracket length of the file line in fileLineArray[index]
    nestLevelArray[index] = nestLevelArray[index] + getLastNestedValue(nestLevelArray, index)
    global index2 # Declare index2 global, index2 is used to map to the characters in file lines by fileLineArray[index][index2]
    index2 = 0 # Initialize index2
    while index2 < len(fileLineArray[index]): # While index2 maps to a character in the file line at fileLineArray[index], then...
        if fileLineArray[index][index2] == "{": # Check if character is an open bracket
            if shouldIgnoreBrackets == 0:  # If we should count this bracket because it's valid (e.g. not commented) then...
                nestLevelArray[index] = nestLevelArray[index] + 1 # Incriment the nested bracket level of this file line by 1
        elif fileLineArray[index][index2] == "}": # Check if character is a closing bracket
            if shouldIgnoreBrackets == 0:  # If we should count this bracket because it's valid (e.g. not commented) then...
                nestLevelArray[index + 1] = nestLevelArray[index + 1] - 1 # Decriment the nested bracket level of the next file line by 1
        elif (fileLineArray[index][index2-1] == "/") & (fileLineArray[index][index2] == "/") : # If "//" appears, ignore the rest of the file line
            index2 = len(fileLineArray[index]) # Make index2 > len(fileLineArray[index] so that the rest of the characters on the file line are ignored/skipped
        else: # If a "{", "}", or "//" is not found, then...
            if isCharAQuote(fileLineArray[index][index2]): # Check if character fileLineArray[index][index2] is a single or double quote
                shouldIgnoreBrackets = flipVar(shouldIgnoreBrackets) # Flip the value of shouldIgnoreBrackets from 0 to 1 or from 1 to 0
        index2 = index2 + 1 # Iterate to the next character in the file line fileLineArray[index]

# PRINT RESULTS OUT TO SCREEN
for index in range(0, len(fileLineArray)-1): # For every file line...
    print(nestLevelArray[index], fileLineArray[index]) # Print the nested bracket level and file line
