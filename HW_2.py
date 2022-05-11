#Преобразовать написанный код в 26-33 пунктах в
# в функцию, принимающую на вход возраст

def CheckAge (x):
    if x < 18:
        print("You don’t have access cause your age is " + str(x) + ". It’s less then 18")
    elif x >= 18 and x <= 60:
        print("Welcome!")
    elif x > 60:
        print("Keep calm and look Culture channel")
    else:
        print("Technical work")

print(CheckAge(61))

