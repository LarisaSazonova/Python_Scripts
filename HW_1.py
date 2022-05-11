#Homework

item_1 = 5
print(item_1)

item_2 = 3
print(item_2)

item_3 = item_1 + item_2
print(item_3)

item_4 = "Yolochka"
print(item_4)

print(str(item_3) + item_4)

print(item_3 * item_4)

item_5 = item_3

item_6 = 15
item_6_type = type(item_6)

print("item_6 ==", item_6)
print("item_6_type ==", item_6_type)

item_7 = str(item_6)
item_7_type = type(item_7)

print("item_7 == ", item_7)
print("item_7_type == ", item_7_type)

age_1 = 10
age_2 = 18
age_3 = 60

if age_1 < age_2:
    print("You don’t have access cause your age is " + str(age_1) + ". It’s less then 18")
elif age_1 >= age_2 & age_1 < age_3:
    print("Welcome!")
elif age_1 > age_3:
    print("Keep calm and look Culture channel")
else:
    print("Technical work")
