def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)


print(fahrenheit_to_celsius(100))


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


print(celsius_to_fahrenheit(100))

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

print("This is a loop for Temperature Conversion.")

while True:
    choice = int(input("1 for 2 quit"))

    if choice == 1:
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
    elif choice == 2:
        break
    else:
        print("INVALID CHOICE!")
