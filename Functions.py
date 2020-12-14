import json

def first_quest():
    text_file = open("text_file.txt", "w")
    user_string = input("Введите строку : ")
    string_list = []
    while True:
        if user_string == "":
            break
        else:
            user_string += "\n"
            string_list.append(user_string)
            user_string = input("Введите следующую строку. Для завершения оставьте строку пустой : ")
    text_file.writelines(string_list)
    text_file.close()
    text_file = open("text_file.txt", "r")
    full_user_file = text_file.read()
    print(f"Задание 1:\n{full_user_file}")
    text_file.close()

def second_quest():
    text_file = open("test_file_text.txt", "r")
    value_strings = 0
    for line in text_file:
        value_strings += 1
        line_list = line.split()
        if len(line_list) == 1:
            quantity_word = "слово"
        elif 5 > len(line_list) > 1:
            quantity_word = "слова"
        else:
            quantity_word = "слов"
        print(f"В строке {value_strings}: {len(line_list)} {quantity_word}")
    if value_strings == 1:
        quantity_string = "строка"
    elif 5 > value_strings > 1:
        quantity_string = "строки"
    else:
        quantity_string = "строк"
    print(f"В файле test_file_text.txt: {value_strings} {quantity_string}")

def third_quest():
    text_file = open("employee_list.txt", "r")
    small_salary = []
    sum_salary = 0
    value_people = 0
    for line in text_file:
        line_list = line.split()
        line_list[1] += "\n"
        if int(line_list[1]) < 20000:
            small_salary.append(line_list[0])
        sum_salary += int(line_list[1])
        value_people += 1
    sum_salary /= value_people
    print(f"Сотрудники с окладом ниже 20000:\n{small_salary}\nСредний оклад сотрудников: {int(sum_salary)}")

def fourth_quest():
    text_file = open("numbers_list.txt", "r")
    new_text_file = open("new_numbers_list.txt", "w")
    for line in text_file:
        line_list = line.split("-")
        if int(line_list[1]) == 1:
            new_text_file.writelines(f"Один - {line_list[1]}")
        elif int(line_list[1]) == 2:
            new_text_file.writelines(f"Два - {line_list[1]}")
        elif int(line_list[1]) == 3:
            new_text_file.writelines(f"Три - {line_list[1]}")
        elif int(line_list[1]) == 4:
            new_text_file.writelines(f"Четыре - {line_list[1]}")
    text_file.close()
    new_text_file.close()

    academic_subjects = open("academic_subjects.txt", "r")
    dictionary_academic_subjects = dict()
    next_line = academic_subjects.readline()
    next_line_list = next_line.split()
    if len(next_line_list) == 3:
        dictionary_academic_subjects.update({next_line_list[0]: int(next_line_list[1])})
    elif len(next_line_list) == 5:
        next_line_list[1] = int(next_line_list[2]) + int(next_line_list[1])
        dictionary_academic_subjects.update({next_line_list[0]: next_line_list[1]})
    elif len(next_line_list) == 7:
        next_line_list[1] += int(next_line_list[2]) + int(next_line_list[1]) + int(next_line_list[3])
        dictionary_academic_subjects.update({next_line_list[0]: next_line_list[1]})

def fifth_quest():
    text_file = open("random_numb", "w")
    numb_list = [34, 43, 46, 87, 13, 0, 45]
    for el in numb_list:
        text_file.writelines(str(el))
        text_file.writelines(" ")
    text_file.close()
    text_file = open("random_numb.txt", "r")
    sum_random_numbers = 0
    new_text_file = []
    for line in text_file:
        new_text_file = line.split()
    for el in new_text_file:
        sum_random_numbers += int(el)
    print(sum_random_numbers)

def sixth_quest():
    lessons = open("academic.txt", "r")
    dictionary_academic_subjects = dict()
    for line in lessons:
        next_line_list = line.split()
        if len(next_line_list) == 3:
            sum_quantity_lessons = int(next_line_list[1])
            next_line_list.pop(1)
            next_line_list.insert(1, int(sum_quantity_lessons))
            dictionary_academic_subjects.update({next_line_list[0]: int(next_line_list[1])})
        elif len(next_line_list) == 5:
            sum_quantity_lessons = int(next_line_list[1]) + int(next_line_list[3])
            next_line_list.pop(1)
            next_line_list.insert(1, sum_quantity_lessons)
            dictionary_academic_subjects.update({next_line_list[0]: next_line_list[1]})
        print(dictionary_academic_subjects)

def seventh_quest():
    firm_file = open("firm_list.txt", "r")
    firm_list = list()
    in_firm_list = dict()
    average_profit = 0
    for line in firm_file:
        next_line_list = line.split()
        if next_line_list[2] > next_line_list[3]:
            profit_firm = int(next_line_list[2]) - int(next_line_list[3])
            in_firm_list.update({next_line_list[0]: profit_firm})
            average_profit += profit_firm // 8
        all_firm_profit = dict(average_profit=average_profit)
    firm_list.append(in_firm_list)
    firm_list.append(all_firm_profit)
    with open("json_file.json", "w") as write_f:
        json.dump(firm_list, write_f)

