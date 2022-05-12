#проверка ввода integer, причем строку, в которой
#только цифра, функция принимает

def check_age (age):

    try:
        age = int(age)
    except ValueError:
        print("Please put an integer")
        return

    if age < 18:
        print(f"You don’t have access cause your age is {age}. It is less then 18")
    elif 18 <= age <= 60:
        print("Welcome!")
    elif age > 60:
        print("Keep calm and look Culture channel")

check_age(2)