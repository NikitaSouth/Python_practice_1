import datetime

year = datetime.date.today().year
name = input("Please, enter your name ")
age = int(input("Please, enter your age "))
hdyear = (year - age) + 100
print("Hello, " + name, "you will turn 100 in " + str(hdyear))
if age >= 18:
    print("You are over 18")
else:
    print("You are under 18");

