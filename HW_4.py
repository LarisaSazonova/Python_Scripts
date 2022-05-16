import json

with open('task1.txt', 'r') as file:
    data_string = file.read().replace('\n', '')

data_string = data_string[14:-1]
data_string = data_string.replace("'", '"')
data_string = data_string.replace('firstName', ' "firstName" ')
data_string = data_string.replace('lastName', ' "lastName" ')
data_string = data_string.replace('phone', ' "phone" ')
data_string = data_string.replace('registrationDate', ' "registrationDate" ')

data_json = json.loads(data_string)

for dic in data_json:
    if dic["registrationDate"] == "09.10.2021" or dic["registrationDate"] == "10.10.2021":
        print(dic["lastName"], dic["firstName"])




