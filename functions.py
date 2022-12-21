import random

lines = []
students = {}

def open_table():
    with open('students.txt', 'r', encoding='UTF-8') as fr, open('data_base.txt', 'w') as fw:
        fw.write(''.join(fr.readlines()))
    with open('data_base.txt', 'r') as file:
        for row in file:
            row1 = row.strip().split()
            lines.append(row1)
    for student in lines:
        students[student[0]] = [student[1], student[2], student[3], student[4]]

def print_data_base():
    for key in students:
        print(*students[key])
    with open('data_base.txt', 'w') as file:
        for key, value in students.items():
            file.write('{} {}\n'.format(key, ' '.join(value)))

def unique_student(surname, name, patronymic):
    for i in students:
        flag = True
        if surname == students[i][0] and name == students[i][1] and patronymic == students[i][2]:
            flag = False
            break
        else:
            flag = True
    return flag


def del_student():
    i = int(input('Введите ID студента '))
    id = str(i)
    if id in students:
        print(f'Студент {students[id][0]} {students[id][1]} {students[id][2]} удалён из БД')
        del students[id]
    else:
        print('Студента с таким ID не существует')
    with open('data_base.txt', 'w') as file:
        for key, value in students.items():
            file.write('{} {}\n'.format(key, ' '.join(value)))

def add_student_by_id():
    i = int(input('Введите номер '))
    surname, name, patronymic = '', '', ''
    id = str(i)
    if id in students:
        print('Студент с таким ID уже существует')
    else:
        s, n, p = [i for i in input('Введите фамилию ').split()], \
                                    [i for i in input('Введите имя ').split()], [i for i in input('Введите отчество ').split()]
        surname, name, patronymic = ''.join(s), ''.join(n), ''.join(p)
        if unique_student(surname, name, patronymic):
            students.update(id = [surname, name, patronymic, '0'])
            students[id] = students.pop('id')
            students[id][3] = str(random.randint(1, 100))
            with open('data_base.txt', 'w') as file:
                for key, value in students.items():
                    file.write('{} {}\n'.format(key, ' '.join(value)))
        else:
            print('Студент с таким ФИО уже существует')


def add_student_by_fio():
    s, n, p = [i for i in input('Введите фамилию ').split()], \
              [i for i in input('Введите имя ').split()], [i for i in input('Введите отчество ').split()]
    surname, name, patronymic = ''.join(s), ''.join(n), ''.join(p)
    id = random.randint(1, 1000)
    if id in students:
        while id in students:
            id = random.randint(1, 1000)
    id = str(id)
    if unique_student(surname, name, patronymic):
        students.update(id = [surname, name, patronymic, '0'])
        students[id] = students.pop('id')
        students[id][3] = str(random.randint(1, 100))
        with open('data_base.txt', 'w') as file:
            for key, value in students.items():
                file.write('{} {}\n'.format(key, ' '.join(value)))
    else:
        print('Студент с таким именем уже существует')


def get_student():
    id = input('Введите ID студента ')
    if id in students:
        print(*students[id])
    else:
        print('Студент с таким ID не существует')

def show_id():
    for key in students:
        print(key)

def edit_student():
    id = input('Введите ID студента ')
    surname, name, patronymic = '', '', ''
    if id in students:
        print(*students[id])
        choice = input('Что вы хотите изменить? ф - фамилия, и - имя, о - отчество, в - всё ')
        if choice == 'ф':
            s = [i for i in input('Введите фамилию ').split()]
            surname = ''.join(s)
            students[id][0] = surname
            print('Фамилия успешно изменена')
        elif choice == 'и':
            n = [i for i in input('Введите имя ').split()]
            name = ''.join(n)
            students[id][1] = name
            print('Имя успешно изменено')
        elif choice == 'о':
            p = [i for i in input('Введите отчество ').split()]
            patronymic = ''.join(p)
            students[id][2] = patronymic
            print('Отчество успешно изменено')
        elif choice == 'в':
            s, n, p = [i for i in input('Введите фамилию ').split()], \
                      [i for i in input('Введите имя ').split()], [i for i in input('Введите отчество ').split()]
            surname, name, patronymic = ''.join(s), ''.join(n), ''.join(p)
            if unique_student(surname, name, patronymic):
                students[id][0], students[id][1], students[id][2] = surname, name, patronymic
                print('ФИО студента успешно изменены')
            else:
                print('Студент с таким именем уже существует')
        else:
            print('Введите другую букву')
    else:
        print('Студента с таким ID не существует')
    with open('data_base.txt', 'w') as file:
        for key, value in students.items():
            file.write('{} {}\n'.format(key, ' '.join(value)))

def give_variant():
    lst = [str(i) for i in range(1, 100)]
    for id in students:
        if id != 'ID':
            students[id][3] = random.choice(lst)
    print('Варианты успешно выданы')
    with open('data_base.txt', 'w') as file:
        for key, value in students.items():
            file.write('{} {}\n'.format(key, ' '.join(value)))

def testing_table():
    with open('testing table.txt', 'w') as file:
        for key in students:
            file.write(f'{key} {students[key][3]}\n')
    print('Таблица отправлена учителю')

def save_table():
    with open('saved.txt', 'w', encoding='UTF-8') as file:
        for key, value in students.items():
            file.write('{} {}\n'.format(key, ' '.join(value)))
    print('Таблица успешно сохранена')

def backup():
    with open('saved.txt', 'r', encoding='UTF-8') as fr, open('data_base.txt', 'w') as fw:
        fw.write(''.join(fr.readlines()))
    with open('data_base.txt', 'r') as file:
        for row in file:
            row1 = row.strip().split()
            lines.append(row1)
    for student in lines:
        students[student[0]] = [student[1], student[2], student[3], student[4]]