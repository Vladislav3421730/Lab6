import pymysql

try:
    connection = pymysql.Connection(
        host="localhost",
        port=3306,
        user="bestuser",
        password="bestuser",
        database="pydb"
    )
    print("Successfully connected")
except Exception as ex:
    print("No Connection")

def view_table():
    with connection.cursor() as cursor:
        view_table = 'SELECT * FROM `users`'
        cursor.execute(view_table)
        allusers = cursor.fetchall()
        for el in allusers:
            print(el)


while (True):
    print("1-Добавить новое значение")
    print("2-Удалить")
    print("3-Редактировать")
    print("4-Вывести")
    print("5-Сортировка")
    print("6-Выйти из программы")
    choice = int
    try:
        choice = int(input("Введите номер операции:  "))
    except ValueError:
        print("Неверно ввдён номер операции")
        continue
    if choice <= 0 or choice > 6:
        print("Вы ввели неверное значение")
        continue
    if (choice == 1):
        name = input("Введите имя:  ")
        password = input("Введите пароль:  ")
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO `users` (name,password) VALUES (%s,%s)"
            val = (name, password)
            cursor.execute(insert_query, val)
            connection.commit()
            print(f"Значения {name} и {password} были успешно добавлены в базу данных")
    elif (choice == 2):
        view_table()
        choice_id = int
        try:
            choice_id = int(input("Введите id пользователя, которого вы хотите удалить: "))
        except ValueError:
            print("Вы ввели невереное id")
            continue
        try:
            with connection.cursor() as cursor:
                delete_table = "DELETE FROM `users` WHERE id='%d'" % (choice_id)
                cursor.execute(delete_table)
                connection.commit()
                print(f"Значение с id {choice_id} было успешно удалено")
        except Exception as ex:
            print("Вы ввели неверное значение")
            continue
    elif (choice == 3):
        view_table()
        choice_edit_id=int
        try:
            choice_edit_id=int(input("Введите id пользователя, которого вы хотите изменить: "))
        except ValueError:
            print("Вы ввели неверное значение id: ")
            continue
        name=input("Введите новое имя")
        password=input("Введите новый пароль: ")
        try:
            with connection.cursor() as cursor:
                delete_table = "UPDATE `users` SET name='%s', password='%s' where id='%d'" % (name,password,choice_edit_id)
                cursor.execute(delete_table)
                connection.commit()
                print(f"Значение с id {choice_edit_id} было успешно отредактировно")
        except Exception as ex:
            print("Вы ввели неверное значение id")
            continue

    elif (choice == 4):
        view_table()
    elif (choice == 5):
        view_table()
        print("Как вы хотите отсортировать пользователей?")
        print("1- По алфавиту")
        print("2- По алфавиту (но в обратном порядке)")
        choice_sort = int(input("Ваш выбор: "))
        if choice_sort == 1:
            try:
                with connection.cursor() as cursor:
                    sort_query = 'SELECT * FROM `users` ORDER BY name ASC'
                    cursor.execute(sort_query)
                    sorted_users = cursor.fetchall()
                    for user in sorted_users:
                        print(user)
            except Exception as ex:
                print("Сортировка не удалась")
                continue
        elif choice_sort == 2:
            try:
                with connection.cursor() as cursor:
                    sort_query = 'SELECT * FROM `users` ORDER BY name DESC'
                    cursor.execute(sort_query)
                    sorted_users = cursor.fetchall()
                    for user in sorted_users:
                        print(user)
            except Exception as ex:
                print("Сортировка не удалась")
                continue
        else:
            print("Вы ввели неверное значение выбора")
            continue
    elif (choice == 6):
        print("Connection was closed")
        connection.close()
        break
