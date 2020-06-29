import random


# Словарь городов
main_cities = [['Москва', 0], ['Санкт-Петербург', 1], ['Новосибирск', 2], ['Екатеринбург', 3], ['Казань', 4],
          ['Нижний Новгород', 5], ['Челябинск', 6], ['Омск', 7], ['Самара', 8], ['Ростов-на-Дону', 9],
          ['Уфа', 10], ['Красноярск', 11], ['Воронеж', 12], ['Пермь', 13], ['Волгоград', 14], ['Краснодар', 15]]

secondary_cities = [[name, 16] for name in ['Томск', 'Петрозаводск', 'Ставрополь', 'Ярославль', 'Владивосток',
                    'Комсомольск-на-Амуре', 'Белгород', 'Оренбург', 'Ижевск', 'Магнитогорск', 'Томск', 'Кемерово',
                    'Тюмень', 'Астрахань', 'Нижний Тагил', 'Архангельск', 'Тамбов', 'Вологда', 'Мурманск', 'Хабаровск']]


# Переменные для ведения статистики ответов
count = 0
count_correct = 0

# Основной цикл программы
while True:
    print('Какие три из перечисленных городов России имеют наибольшую численность населения?\n '
          'Запишите в ответ цифры в порядке возрастания, под которыми указаны эти города.')

    # Перемешиваем словари
    random.shuffle(main_cities)
    random.shuffle(secondary_cities)

    # Формируем вопрос
    formed_case = [main_cities[0], main_cities[1], main_cities[2],
                   secondary_cities[0], secondary_cities[1], secondary_cities[2]]
    random.shuffle(formed_case)

    # Привязываем нумерацию
    for i in range(1, 7):
        formed_case[i-1].append(str(i))

    # Выводим вопрос
    print(f'''
    1){formed_case[0][0]}
    2){formed_case[1][0]}
    3){formed_case[2][0]}
    4){formed_case[3][0]}
    5){formed_case[4][0]}
    6){formed_case[5][0]}
    ''')

    # Запрашиваем ответ
    answer = input()

    # Распределяем города по населению
    formed_case.sort(key=lambda x: x[1])

    # Проверяем ответ
    if ''.join(city[2] for city in formed_case)[:-3][::-1] == answer:
        count_correct += 1
        print('Верно!\n')
    else:
        print('Неверно! Правильный ответ: ' + ''.join(city[2] for city in formed_case)[:-3][::-1] + '\n')

    count += 1
          
    # Удаляем привязку позиции
    for j in range(0, 6):
        formed_case[j].pop()


    # Вывод статистики
    print(f'Решено/Верных: {count}/{count_correct}')

