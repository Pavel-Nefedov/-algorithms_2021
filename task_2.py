"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
user_number = int(input('Введите число: '))

def nums(user_number, even=0, odd=0):

    if user_number == 0:
        return print('четных - ', even, 'нечетных - ', odd)

    else:
        first_number = user_number % 10
        user_number = user_number // 10
        if first_number % 2 == 0:
            even += 1
        else:
            odd += 1
        return nums(user_number, even, odd)

nums(user_number)
