# Angelica Magnussen
# 1001549375
# 11/7/2020
# Windows 10

# PLEASE NOTE: The program will read up to 500 characters in the input file; change maxCharsInFile from 500 to a larger number if more than 500 characters are in the input file
# PLEASE NOTE: Python version 3.8 was used

import os # Import package os so input file can be opened & read, code from https://www.geeksforgeeks.org/os-module-python-examples/

def isAnOperator(charInFile): # isAnOperator() is a pure function that determines whether the string charInFile is an operator ('+, -, *, or \)
    returnVal = 0  # Return false (charInFile is not an operator) by default
    if charInFile == '+': # If charInFile is '+', then charInFile is an operator
        returnVal = 1 # Return true (charInFile is an operator)
    if charInFile == '-': # If charInFile is '-', then charInFile is an operator
        returnVal = 1 # Return true (charInFile is an operator)
    if charInFile == '*': # If charInFile is '*', then charInFile is an operator
        returnVal = 1 # Return true (charInFile is an operator)
    if charInFile == '/': # If charInFile is '/', then charInFile is an operator
        returnVal = 1 # Return true (charInFile is an operator)
    return returnVal # Returns 1 if charInFile is an operator, 0 otherwise

def evaluate(inputA, inputB, operator): # evaluate() is a pure function that performs the operation represented by the string operation on inputA and inputB
    if operator == '+': # If operator is '+', then add & return (inputA + inputB)
        # print(inputA, "+", inputB, "=", inputA + inputB) # For debugging
        return (inputA + inputB) # Return the sum
    if operator == '-':  # If operator is '-', then subtract & return (inputA - inputB)
        # print(inputA, "-", inputB, "=", inputA - inputB) # For debugging
        return (inputA - inputB) # Return the difference
    if operator == '*':  # If operator is '*', then multiply & return (inputA * inputB)
        # print(inputA, "*", inputB, "=", inputA * inputB) # For debugging
        return (inputA * inputB) # Return the product
    if operator == '/':  # If operator is '/', then divide & return (inputA / inputB)
        # print(inputA, "/", inputB, "=", inputA / inputB) # For debugging
        return (inputA / inputB) # Return the quotient

def computeFileLine(tokenArr, index2): # computeFileLine() is a pure function that uses recursion to compute the result of a mathematical expression (stored in tokenArr) in reverse polish notation (RPN), index2 is used to map the operator and the two operands at each iteration
    if len(tokenArr) != 1: # If there is more than one element in tokenArr (a dynamic array whose elements create a mathematical expression in RPN), then there is at least 1 more operator in need of execution
        if isAnOperator(tokenArr[index2]):  # If the string at tokenArr[index2] is an operator token, then convert the two number tokens before the operator token to integers
            operator = tokenArr[index2]  # operator is a string used to store the string representation of an operator in tokenArr[index2]
            inputA = float(tokenArr[index2 - 2])  # Python's built-in float converter float() converts the string tokenArr[index2-2] to an float
            inputB = float(tokenArr[index2 - 1])  # Python's built-in float converter float() converts the string tokenArr[index2-1] to an float
            result = evaluate(inputA, inputB, operator)  # evaluate() determines what operator is used, performs the appropriate arithmetic on inputA and inputB, and stores the result in result
            tokenArr[index2 - 2] = str(result)  # Python's built-in string converter str() converts the float result to a string
            tokenArr.pop(index2)  # The operator at tokenArr[index2] has already been computed so it is removed from tokenArr
            tokenArr.pop(index2 - 1) # The number at tokenArr[index2 - 1] has already been used in its computation so it is removed from tokenArr
            computeFileLine(tokenArr, index2 - 2) # Send index2 back 2 indices because 2 elements of tokenArr were removed, Compute any other operators in tokenArr by calling computeFileLine()
        else:
            computeFileLine(tokenArr, index2 + 1) # Incriment index2 by 1 so that index2 maps to the next element in tokenArr, Compute any other operators in tokenArr by calling computeFileLine()
    else:  # If len(tokenArr) == 1, then all operations in tokenArr have been executed & the final result is stored in tokenArr[0]
        print('>>> Final result is', tokenArr[0]) # Print the final result of the RPN expression stored in tokenArr[0]
        return 0 # Return 0 to signal the end of the function

def loopThroughFileLines(index1, allLines): # loopThroughFileLines() is a pure function that uses recursion to traverse the dynamic array allLines and compute every RPN expression in the input file, at each call index1 increases by 1
    if index1 < len(allLines): # If the end of file has not been reached yet, then compute the next RPN expression in the input file
        tokenArr = allLines[index1].split() # tokenArr is a dynamic array whose elements represent a RPN expression, each element is a string representation of a number or operator
        print('\ntokenArr is', tokenArr, '  len(tokenArr) is', len(tokenArr))  # For debugging
        index2 = 0  # Declare & define index2 for later use, index2 is used to map to string elements (representing a RPN expression) in allLines
        computeFileLine(tokenArr, index2) # computeFileLine() uses index2 to iterate through the elements of tokenArr and compute the RPN represented by tokenArr
        loopThroughFileLines(index1+1, allLines) # Call computeFileLine() to process the next element (a string representation of a RPN expression) in allLines
    else: # If the end of file has been reached, then end the recursive function loopThroughFileLines()
        # print('\nEnd of program: All RPN expressions have been computed') # For debugging, indicate the end of the input file's computation
        return 0 # Return 0 to signal the end of the function

inputFileName = (os.getcwd() + '\input_RPN.txt') # (os.getcwd() + '\input_RPN.txt') returns a string representation of the filepath of input_RPN.txt on the user's computer, Code from https://www.geeksforgeeks.org/os-module-python-examples/
# print('inputFileName is ', inputFileName) # For debugging
inputFile = os.open(inputFileName, os.O_RDONLY) # Open the file and store it as a File object in inputFile, the os.O_RDONLY flag indicates that the file will be read only, Code from https://www.tutorialspoint.com/python/os_open.htm
maxCharsInFile = 500 # maxCharsInFile is an integer that specifies the maximum number of characters that will be read from the input file
byteEncodedStr = os.read(inputFile, maxCharsInFile) # Read the entire contents of the file and store it in byteEncodedStr (a encoded data type called bytes), a maximum of maxCharsInFile characters will be read from inputFile, Code from https://www.tutorialspoint.com/python/os_open.htm
byteDecodedStr = str(byteEncodedStr, 'utf-8') # Decode byteEncodedStr by specifying the encoding type 'utf-8' and store it in byteDecodedStr , Code is form https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
# print('os.read(inputFile, maxCharsInFile) is', byteDecodedStr) # For debugging
allLines = byteDecodedStr.split('\n') # The elements of dynamic array allLines are the string representations of a RPN expression
print('allLines is ', allLines) # For debugging
index1 = 0 # Declare & define index1 for later use, index1 is used to traverse through allLines
loopThroughFileLines(index1, allLines) # loopThroughFileLines() starts at index1 and continues to len(allLines), the RPN expression allLines[index1] is computed at each iteration
