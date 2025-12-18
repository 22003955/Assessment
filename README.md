# Assessment
This is the repo for my assessment. 
This is a temperature converting program which helps people (users) convert temperature from one scale to the other and vice versa.
This program has only two scales of conversion: C and F. Thus; if user tries to convert to and/or from K user will receive the output string '{unit} is not a valid unit of measurement.'


The variable 'unit' is assigned input(). In the parenthesis we have the strings wchich asks us wether the temperature is in Celsius or Fahrenheit. User input should be one of those measurements: C or F
Next we ve the variable 'temp' assigned float() - not int()- adter which we have another function; input() In hese parentheses we have the string which tells us to enter the temperature.
Next line starts with the conditional if followed by the variable and (==) -which checks if two variables or values are equal- followed by  the string "C" and a colon
Next line starts with an indentation followed by the variable 'temp' assigned, the function round() followed by the temperature conversion formula. Celsius to Fahrenheit
Next  is -still indented- the function print() followed by the f-string "The temperature in Fahrenheit is: {temp} F"
Next line starts with the conditional elif the variable equals the string and a colon.
Next line is indented: the variable assigned to function round() and in the parentheses we have the formula for temperature conversion Fahrenheit to Celsius.
Next line is also indented: the finction print() the f-string which tells you what the temperature in Celsius is.
Next line starts with the conditional else for other scales of temperature.
The next line is indented: the function print() followed by the f-string '{unit} is not a valid unit of measurement.'

The next line strts with the function print() followed by the string; "This is a loop for temperature conversion."

Next line starts the while True loop:
Next line is indented: the variable choice assigned the functions int() input() followed by the string "1 for 2 quit" Here user has to choose between 1 and 2. 
Next line is still indented: the conditional if the variable equals 1: 
From this line we copy paste our conditionals for temperature conversion with double and triple indents.

After the Temperature conversion conditionals we continue with our choice conditionals:

Next line is indented: we start with the conditional elif the variable choice equals 2 and in the line after that we have indented:
  break
Next line is the conditional else: 
Next line -indented- we have the function print() and the string "INVALID CHOICE!"
