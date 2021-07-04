# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press Shift+F10 to execute a Python script or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

'''
Use Python to create a simple calculator that accepts Reverse Polish Notation (RPN)
and displays the final answer (Intermediate steps or results need not be displayed). 

    It only accepts 4 operators “+”, “-“, “*”, “/”.
    Input numbers will be single digits. 
    The input will be in postfix notation.  
    The input will be provided in a text file called input_RPN.txt.
    Your program should not ask the user for any input. 
    There will be one RPN expression in each line. 
    Your code should be able to read the file and print the result for each RPN in a new line.
    Example of RPN: 4 2 + and your output should be 6. This is a simple expression. More
    complex algebraic notations will be used to test your program like the one below.
    Example algebraic notation: ( 4 + 2 * 5 ) / ( 1 + 3 * 2 )
    Translated into RPN: 4 2 5 * + 1 3 2 * + /

Note: - Your code should be able to read the input file from the same folder (which has
your .py file). Do not hard code the path to the file in your laptop/desktop. Use os to
get the path and read the input file. Also, please take special care to process the line-ending
character correctly; for example, if you write the program on a Mac it should work correctly
when graded using Windows and vice versa.
'''

import pathlib

# For debugging:
# print('pathlib.Path(__file__).parent.absolute() is', pathlib.Path(__file__).parent.absolute()) # Returns filepath of the parent directory of this .py file
# print('pathlib.Path(input_RPN.txt).absolute() is', pathlib.Path('input_RPN.txt').absolute()) # Returns filepath of this input_RPN.txt on the user's computer

def isAnOperator(charInFile):
    returnVal = 0  # return false by default
    if charInFile == '+':
        returnVal = 1  # return true
    if charInFile == '-':
        returnVal = 1  # return true
    if charInFile == '*':
        returnVal = 1  # return true
    if charInFile == '/':
        returnVal = 1  # return true
    return returnVal  # returns 1 if charInFile is an operator, 0 otherwise

def evaluate(inputA, inputB, operator):
    if operator == '+':
        # print(inputA, "+", inputB, "=", inputA + inputB) # For debugging
        return (inputA + inputB)
    if operator == '-':
        # print(inputA, "-", inputB, "=", inputA - inputB) # For debugging
        return (inputA - inputB)
    if operator == '*':
        # print(inputA, "*", inputB, "=", inputA * inputB) # For debugging
        return (inputA * inputB)
    if operator == '/':
        # print(inputA, "/", inputB, "=", inputA / inputB) # For debugging
        return (inputA / inputB)

'''
Read input_RPN.txt that has many lines of RPN input. Postfix is RPN. 
4 * (5 + 8) is the same as  5 8 + 4 * and 
4 / (5 + 8) is the same as 4 5 8 + /.
'''
inputFileName = pathlib.Path('input_RPN.txt').absolute() # Returns a string of the filepath of input_RPN.txt on the user's computer
inputFile = open(inputFileName, 'r') # inputFile is a File object with access to read input_RPN.txt
allLines = inputFile.readlines() # allLines is a dynamic array of strings, each string is a line from input_RPN.txt
print('allLines is ', allLines) # For debugging
result = 0 # Declare & define result for later use
operator = ' ' # Declare & define operator for later use
inputA = 0 # Declare & define inputA for later use
inputB = 0 # Declare & define inputB for later use
for index1 in range(0, len(allLines)):  # index1 is an integer used to iterate through the index values of allLines
    # allLines[index].split()'s deliminators are ' ' & '\n' by default
    tokenArr = allLines[index1].split()  # tokenArr is a dynamic array of input tokens, each token is the string representation of a number or operator
    print('\ntokenArr is', tokenArr, '  len(tokenArr) is', len(tokenArr)) # For debugging
    index2 = 0 # Declare & define index2 for later use, index2 is used as the while-loop's condition statement and will be changed in the while-loop's block so index2 is defined before the while-loop
    while index2 < len(tokenArr): # index2 is an integer used to iterate through the index values of tokenArr, a while-loop is used because index2 changes in while-loop's block (a for-loop would not support the changing of index2 in the execution block)
        # print('tokenArr[', index2, '] is', tokenArr[index2]) # For debugging
        if isAnOperator(tokenArr[index2]): # If the string at tokenArr[index2] is an operator token, then convert the two number tokens before the operator token to integers
            operator = tokenArr[index2] # operator is a string used to store the string representation of an operator in tokenArr[index2]
            # print('index2 is', index2, '  operator is ', operator)  # For debugging
            inputA = float(tokenArr[index2-2]) # Python's built-in float converter float() converts the string tokenArr[index2-2] to an float
            inputB = float(tokenArr[index2-1]) # Python's built-in float converter float() converts the string tokenArr[index2-1] to an float
            result = evaluate(inputA, inputB, operator) # evaluate(inputA, inputB, operator) determines what operator is used, performs the arithmetic, and stores the result in result
            print('> Operation result is', inputA, operator, inputB, '=', result) # For debugging
            tokenArr[index2 - 2] = str(result) # Python's built-in string converter str() converts the float result to a string
            tokenArr.pop(index2) # The operator at tokenArr[index2] has already been computed so it is removed
            tokenArr.pop(index2 - 1) # The number at tokenArr[index2 - 1] has already been used in its computation so it is removed
            index2 = index2 - 2 # Send index2 back 2 indices because 2 elements of tokenArr were removed
            # print('tokenArr is', tokenArr, '  len(tokenArr) is', len(tokenArr), '  index2 is', index2)  # For debugging
        # print('index2 is', index2,'  len(tokenArr) is', len(tokenArr), '  tokenArr[0] is', tokenArr[0]) # For debugging
        if len(tokenArr) == 1: # If len(tokenArr) == 1, then all operations in tokenArr have been executed & the final result is stored in result & tokenArr[0]
            print('>>> Final result is', result)
        index2 = index2 + 1 # Incriment index2 by 1 so that index2 maps to the next element in tokenArr
