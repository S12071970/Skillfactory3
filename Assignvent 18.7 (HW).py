import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Редактировать оценки
        5. Редактировать предметы
        6. Редактировать имя ученика
        7. Удалить оценку
        8. Удалить данные по предметам
        9. Удалить данные по ученикам
        10.Добавить ученика
        11.Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Редактировать оценки ')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
         print (students_marks[student][class_])
        n = int(input('Введите индекс оценки, которую хотите изменить: '))
        n1 = int(input('Введите новую оценку: '))
        students_marks[n] = n1
        print(students_marks[student][class_])
        print('Оценка изменена')
        print()

    elif command == 5:
        print('5. Редактировать предметы')
        class_ = input('Введите предмет:')
        if class_ in classes:
            new_class_ = input('Введите новый предмет:')
            classes.append(new_class_)
            print(f' Предмет{new_class_} добавлен')
            students_marks[student][new_class_] = students_marks[student][class_]
            classes.remove(class_)
            print(classes)
    else:
        print('ОШИБКА: неправильное наименование предмета')

    if command == 6:
        print('6. Редактировать имя ученика')
        student = input('Введите имя ученика:')
        if student in students:
            student_new = input('Введите новое имя ученика:')
            students.append(student_new)
            print(f'Ученик {student_new}добавлен')
            students_marks[student_new] = students_marks[student]
            students.remove(student)
        else:
            print('ОШИБКА: такого ученика нет в списке')

    elif command == 7:
        print('7. Удалить оценку')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            mark = int(input('Введите оценку, которую хотите удалить: '))
            if mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                print(f'Оценка {mark} ученика {student} по предмету {class_} удалена.')
            else:
                print(f'Оценка {mark} не найдена у ученика {student} по предмету {class_}.')

    elif command == 8:
        print('8. Удалить данные по предметам')
        student = input('Введите имя ученика для удаления предмета: ')
        class_ = input('Введите предмет для удаления: ')
        new_class_ = input('Новый предмет: ')
        if class_ in (students_marks[student]).keys():
            students_marks[student][new_class_] = students_marks[student][class_]
            del students_marks[student][class_]
            print(f'Измененные предметы: {students_marks}')
        else:
            print('Предмет не найден')

    elif command == 9:
        end_student = input('Введите ученика, которого хотите удалить: ')
        if end_student in students_marks:
            del students_marks[end_student]
            print(students_marks)
        else:
            print('Этого ученика в списке нет')

    elif command == 10:
        print('10. Добавить ученика')
        student = input('Введите имя ученика:')
        students_marks[student] = {
            'Математика': [],
            'Русский язык': [],
            'Информатика': [],
        }
        print('Новый ученик добавлен в список')

    elif command == 11:
        print('11. Выход из программы')
        break




