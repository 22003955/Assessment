temp=int(input("Please input the temperature here: "))

forecast={
    'Monday': temp < 10,
    'Tuesday': temp > 10 < 20,
    'Wednesday': temp > 20 < 25,
    'Thursday': temp < 10,
    'Friday': temp < 20,
    'Saturday': temp > 20,
    'Sunday': temp > 0
}

def classify_temperature(temp):
    if temp<10:
        print("Cold")
    elif temp<20:
        print("Warm")
    elif temp>20:
        print("Hot")

for key, value in forecast.items():
    print(f'Today is {key} and it is {value}!')
