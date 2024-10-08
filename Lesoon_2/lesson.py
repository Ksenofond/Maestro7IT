'''
Cтруктуры данных:
1. Списки - List []
2. Кортежи - Tuple ()
3. Множества - Set {} "()"
4. Неизменяемое множество - Frozen Set {}
5. Словари - Dict {"": ""}

[✔] Изменяемые:
1. Списки - List []
2. Множества - Set ()
3. Словари - Dict {"": ""}

[✔] Неизменяемые:
1. Кортежи - Tuple ()
2. Неизменяемое множество - Frozen Set {}
'''

''' Работа со списками '''
# product_list = ['apple', 'orange', 'water', 'bread', 'milk'] # создаём продуктовую корзинку
# print(product_list)

# создание списка на русском
# продуктовая_корзинка = ['яблоко', 'апельсин', 'вода', 'хлеб', 'молоко']
# print(продуктовая_корзинка)

# добавление нового элемента в конец списка
# продуктовая_корзинка.append('10-ок яиц')
# print(продуктовая_корзинка)

# реверсирование списка (обратный порядок)
# продуктовая_корзинка.reverse()
# print(продуктовая_корзинка)

''' Работа с кортежами *Неизменяемый список '''
# tuple_1 = (1, 2, 3, 4, 5, 5.5, True)
# print(tuple_1)

''' Работа со множествами *Только уникальные значения '''
set_1 = {1, 1, 2, 2, 3, 4, 5, 5.5, 5.5, True, True, True, False, False}
set_1.add(7)
set_1.add(8)
set_1.add(9)
print(set_1)

''' Неизменяемое множество *Frozen Set {}'''
frozenset_1 = {1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8.8}
frozenset_1.add(9)
print(frozenset_1)

''' Работа со словарями
    "Ключ": "Значение"
    "Key": "Items"
'''
dict_1 = {
    "1": "яблоко",
    "2": "апельсин",
    "3": "вода",
    "4": "хлеб",
    "5": "молоко"
}

# dict_1.keys()
# dict_1.items()

# library = {
#     "Автор_1": "A",
#     "Автор_1": "B",
#     "Автор_2": "A",
#     "Автор_2": "B",
#     "Автор_3": "C"
# }

library = {
    # "Ключ": "Значение"
    "Гарри Поттер и философский камень": "Джоан Роулинг",
    "Гарри Поттер и Тайная комната": "Джоан Роулинг",
    "Гарри Поттер и кубок Огня": "Джоан Роулинг",
    "Гарри Поттер и Орден Феникса": "Джоан Роулинг",
    "Гарри Поттер и Принц-полукровка": "Джоан Роулинг"
}

print(library)


# TODO: Заметки
## Преподаватель: Дуплей Максим Игоревич
## Дата: 28.09.2024