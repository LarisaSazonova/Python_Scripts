#проверка ввода integer, причем строка, в которой
#только цифра, пропускается

def CheckAge (x):
    if type(x) != int and type(int(x)) != int:
        print("Please put an integer")
        return

    x = int(x)

    if x < 18:
        print("You don’t have access cause your age is " + str(x) + ". It’s less then 18")
    elif x >= 18 and x <= 60:
        print("Welcome!")
    elif x > 60:
        print("Keep calm and look Culture channel")
    else:
        print("Technical work")

print(CheckAge("1"))