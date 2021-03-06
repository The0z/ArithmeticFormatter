Can be run at: https://repl.it/@The0z/fcc-ArithmeticArranger#arithmetic_arranger.py

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Rules:
Situations that will return an error:
1)If there are too many problems supplied to the function. The limit is five, anything more will return:
Error: Too many problems.

2)The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
Error: Operator must be '+' or '-'.

3)Each number (operand) should only contain digits. Otherwise, the function will return:
Error: Numbers must only contain digits.

4)Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
Error: Numbers cannot be more than four digits.

If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

What I Learned:
-How to handle strings so they print out on their proper lines
-Error handling of bad data inputted to program.
-How to use optional variables
-Creating Functions
-Spliting, manipulating, and formatting strings.

What I could improve on:
-Better understanding of the available list methods
-cleaner way to create empty lists
-Implement try method in python for all other cases not accounted for.
