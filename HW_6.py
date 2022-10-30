import json

with open('task3.txt', 'r', encoding="utf8") as file:
    data_string = file.read().replace('\n', '')

data_string = data_string [20:data_string.rfind("]")+1]

data_string = data_string.replace('id', ' "id" ')
data_string = data_string.replace('name', ' "name" ')
data_string = data_string.replace('departments', ' "departments" ')
data_string = data_string.replace('employees_count', ' "employees_count" ')

data_json = json.loads(data_string)

def find_max_id():
    max_id = 0
    for enterprise in data_json:
        if enterprise["id"] > max_id:
            max_id = enterprise["id"]

        for dept in enterprise["departments"]:
            if dept["id"] > max_id:
                max_id = dept["id"]

    return max_id


# Задание 1 (Вывести все предприятия и их отделы. Рядом указать количество сотрудников. 
# Для предприятия посчитать сумму всех сотрудников во всех отделах)
for enterprise in data_json:
    emp_count = 0
    for dept in enterprise["departments"]:
        emp_count += dept["employees_count"]
    print(f"{enterprise['name']} ({emp_count} сотрудников)")
    for dept in enterprise["departments"]:
        print("- " + dept["name"] + " (" + (str(dept["employees_count"])) + " сотрудников)")

# Задание 2 (Написать функцию, которая будет принимать 1 аргумент 
# (id отдела или название отдела и возвращать название предприятия, к которому относится)

def get_enterprise_name(x):

    def iterate():
        for enterprise in data_json:
            for dept in enterprise["departments"]:
                if dept["id"] == x or dept["name"] == x:
                    return (enterprise["name"])
    
    result_message = iterate()

    if result_message:
        return result_message
    else:     
        return "No such department"

print(get_enterprise_name(7))
            
# Задание 3 (Написать функцию, которая будет добавлять предприятие)
def add_enterprise (name):
    
    max_id = find_max_id()
    new_enterprise = {"id": max_id + 1, "name": name, "departments": []}
    data_json.append(new_enterprise)
    return data_json

print(add_enterprise("Еще предприятие"))

# Задание 4 (Написать функцию, которая будет добавлять отдел в предприятие. 
# В качестве аргумента принимает id предприятия, в которое будет добавлен отдел, и название отдела)

def add_department (enterprise_id, dept_name):

    max_id = find_max_id()
    
    for enterprise in data_json:
        if enterprise["id"] == enterprise_id:
            new_department = {"id": max_id + 1, "name": dept_name, "employees_count": 0}
            enterprise["departments"].append(new_department)
    return data_json
    
print(add_department(1, "QA отдел"))

# Задание 5 (Написать функцию для редактирования названия предприятия. 
# Принимает в качестве аргумента id предприятия и новое имя предприятия)

def change_enterprise_name (enterprise_id, new_name):
    
    for enterprise in data_json:
        if enterprise["id"] == enterprise_id:
            enterprise["name"] = new_name
            return data_json

    return "No such enterprise"

print(change_enterprise_name(1, "Новое предприятие!!!"))

# Задание 6 (Написать функцию для редактирования названия отдела.
# Принимает в качестве аргумента id отдела и новое имя отдела)

def change_department_name (department_id, new_name):

    for enterprise in data_json:
        for dept in enterprise["departments"]:
            if dept["id"] == department_id:
                dept["name"] = new_name
                return data_json

    return "No such department"

print(change_department_name(16, "НОВЫЙ ОТДЕЛ"))

# Задание 7 (Написать функцию для удаления предприятия. В качестве аргумента принимает id предприятия)

def delete_enterprise (enterprise_id):
    
    for enterprise in data_json:
        if enterprise["id"] == enterprise_id:
            data_json.remove(enterprise)
            return data_json

    return "No such enterprise"


# Задание 8 (Написать функцию для удаления отдела. В качестве аргумента принимает id отдела. 
# Удалить отдел можно только, если в нем нет сотрудников)

def delete_department (department_id):

    for enterprise in data_json:
        for dept in enterprise["departments"]:
            if dept["id"] == department_id and dept["employees_count"] == 0:
                enterprise["departments"].remove(dept)
                return data_json

    return "No such department"


# Задание 9. Написать функцию для переноса сотрудников между отделами одного предприятия. 
# (В качестве аргумента принимает два значения: id отдела, из которого будут переноситься 
# сотрудники, и id отдела, в который будут переноситься сотрудники)

def move_employees (source_dept_id, target_dept_id):
    
    for enterprise in data_json:
        source_dept_ref = None
        target_dept_ref = None

        for dept in enterprise["departments"]:
            if dept["id"] == source_dept_id:
                source_dept_ref = dept

            if dept["id"] == target_dept_id:
                target_dept_ref = dept

            if target_dept_ref and source_dept_ref:
                target_dept_ref["employees_count"] = source_dept_ref["employees_count"] + target_dept_ref["employees_count"]
                source_dept_ref["employees_count"] = 0
                return data_json

    return "No such departments within one enterprise"

