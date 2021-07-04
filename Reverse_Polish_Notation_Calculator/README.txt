Reverse Polish Notation (RPN) Calculator 

INSTRUCTIONS

12. You should only need to use the ‘os’ package, if you want to use any other package you must get permission beforehand.
13.	Input is RPN
14.	Output is the calculated result of the expression

Use Python to create a simple calculator that accepts Reverse Polish Notation (RPN) and displays the final answer (Intermediate steps or results need not be displayed). 

It only accepts 4 operators “+”, “-“, “*”, “/”.
Input numbers will be single digits. 
The input will be in postfix notation.  
The input will be provided in a text file called input_RPN.txt.
Your program should not ask the user for any input. 
There will be one RPN expression in each line. 
Your code should be able to read the file and print the result for each RPN in a new line.
Example of RPN: 4 2 + and your output should be 6. This is a simple expression. More complex algebraic notations will be used to test your program like the one below.
Example algebraic notation: ( 4 + 2 * 5 ) / ( 1 + 3 * 2 )
Translated into RPN: 4 2 5 * + 1 3 2 * + /

Note: - Your code should be able to read the input file from the same folder (which has your .py file). Do not hard code the path to the file in your laptop/desktop. Use os to get the path and read the input file. Also, please take special care to process the line-ending character correctly; for example, if you write the program on a Mac it should work correctly when graded using Windows and vice versa.


Extra credit (5 points each)
A)	Write a separate program that can input an algebraic expression and convert it to RPN and then evaluate the RPN. Print the RPN and the result in separate lines. If you are implementing extra credit, your file should be name as <netid>_EC.py. The input file name will be input_RPN_EC.txt and it will have algebraic expressions.
B)	Add more operators (unary subtraction, or modulo division, etc.). You must document what operators you are adding. Add which ones to comments and make sure to include that as well in your submission so the GTA knows to test using the extra scenarios.

