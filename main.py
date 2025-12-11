def fahrenheit_to_celsius(fahrenheit):
    """
    Take temperature in fahrenheit and convert to celsius
    example:
    input: 91.4
    process: (91.4-32)*5/9
    would return: 33
    """
    
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)


print(fahrenheit_to_celsius(100))


def celsius_to_fahrenheit(celsius):
    """
    Take temperature in celsius and convert to fahrenheit
    example:
    input: 33
    process: (33*9/5)+32
    would return: 91.4
    """
    
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


print(celsius_to_fahrenheit(100))

#Lines above are a test

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ") #Use capital C/F to get a valid response
temp = float(input("Enter temperature here: "))

if unit == "C": #Conditional, allows user to receive conversion as Fahrenheit
    temp = round((9 * temp) / 5 + 32, 1) #This line is the formula for conversion
    print(f"The temperature in Fahrenheit is: {temp} °F") 
elif unit == "F": #Conditional, If user chooses Fahrenheit, will receive conversion as Celsius
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is {temp} °C")
else: # Conditional for other scales of temperature
    print(f"{unit} is an invalid unit of measurement.")

print("This is a loop for Temperature Conversion.") #An introduction to while loop

while True: 
    choice = int(input("1 for 2 quit")) #User has to choose between two options #Use integers(1/2), no strings ("").

    if choice == 1: #If user chooses 1, will loop through the 
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        temp = float(input("Enter temperature here: "))

        if unit == "C":
            temp = round((9 * temp) / 5 + 32, 1)
            print(f"The temperature in Fahrenheit is: {temp} °F")
        elif unit == "F":
            temp = round((temp - 32) * 5 / 9, 1)
            print(f"The temperature in Celsius is {temp} °C")
        else:
            print(f"{unit} is an invalid unit of measurement.")
    elif choice == 2: # If user chooses 2, the program will end
        break
    else: #If user chooses anything else, will receive invalid choice
        print("INVALID CHOICE!")
