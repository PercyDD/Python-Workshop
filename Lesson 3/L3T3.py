name = raw_input("What is your name?")
age = int(raw_input("What is your age?"))

if age >= 15 and age <= 17:
    print(name + " is eligible to join the club!")
else:
    print("Sorry " + name + " you can not join the club!")
