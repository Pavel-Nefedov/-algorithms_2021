"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
 сделайте замеры и сделайте выводы, что выполняется быстрее и почему
 И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
 У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
 сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
 И укажите сложность ф-ций, которые вы используете для операций.
 Операцию clear() не используем.
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time

start_time = time.time()
"""Создание словаря и вставка значений в словарь"""
dict_sample  = {a: a for a in range(100000)}  # O(1)
print(type(dict_sample))

print(f"dict--- {time.time() - start_time} seconds ---")
#dict--- 0.010993242263793945 seconds ---

start_time = time.time()
"""
Получение значений из словаря, не знал как нужно сделать, поэтому 
записал их в другой список для возможности просмотра всех
"""
dict_receiving = [dict_sample.get(key) for key in range(10000)]

"""Удаление значений из словаря"""
dict_delete  = {dict_sample.pop(key) for key in range(10000)} # O(1)

"""Изменение значчений в словаре"""
for key in range(10000):
    dict_sample[key] = 'ugabuga' # o(1)
print(f"dict operations --- {time.time() - start_time} seconds ---")
#dict operations --- 0.004996776580810547 seconds ---

print('-' * 20)
print('-' * 20)


start_time = time.time()
"""Создание списка и ввставка значений в список"""
list_sample = [(a, a) for a in range(100000)]   # O(1)
print(type(list_sample))
print(f"list--- {time.time() - start_time} seconds ---")
#list--- 0.012992143630981445 seconds ---

start_time = time.time()
"""
Получение значений из списка, не знал как нужно сделать, поэтому 
записал их в другой список для возможности просмотра всех
"""
list_receiving = [list_sample[val] for val in range(10000)] # O(1)

"""Удаление значений из списка"""
for key in range(10000):
    list_sample.pop(key) # O(n)

"""Изменение значчений в списке"""
for key in range(10000):
    list_sample[key] = list_sample[key+1] # O(n)

print(f"list operations --- {time.time() - start_time} seconds ---")
# list operations --- 0.3967564105987549 seconds ---

"""
Вывод: операции со словарем выполняются намного быстрее и создание словаря происходит также быстрее,
но словари занимают большое количество памяти

"""