import functions


def main():
    print('Введите команду.\nopen - открыть таблицу, print - печать БД, addByID - добавить студента по ID,\n'
          'addByFIO - добавить студента по ФИО, del - удалить данные студента, get - получить данные студента,\n'
          'show - показать все доступные ID, edit - редактировать данные студента, var - раздать вариант,\n'
          'send - отправить учителю, save - сохранить таблицу,\n'
          'backup - открыть последнее сохранение, end - завершить работу.')
    while True:
        choice = input()
        if choice == 'open':
            functions.open_table()
        elif choice == 'create':
            functions.create_table()
        elif choice == 'print':
            functions.print_data_base()
        elif choice == 'addByID'.lower():
            functions.add_student_by_id()
        elif choice == 'addByFIO'.lower():
            functions.add_student_by_fio()
        elif choice == 'del':
            functions.del_student()
        elif choice == 'get':
            functions.get_student()
        elif choice == 'show':
            functions.show_id()
        elif choice == 'edit':
            functions.edit_student()
        elif choice == 'var':
            functions.give_variant()
        elif choice == 'send':
            functions.testing_table()
        elif choice == 'save':
            functions.save_table()
        elif choice == 'backup':
            functions.backup()
        elif choice == 'end':
            break
        else:
            print('Такой команды не существует')


if __name__ == '__main__':
    main()