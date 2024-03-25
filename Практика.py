################################
# Задание 1
# fruit_tuple = ("apple", "banana", "orange", "pineaple"
#                "grapes", "apple" )
# fruit_name = input("Please enter a fruit name: ")

# print(f"You fruit: {fruit_name}, exist in our tuple: {fruit_tuple.count(fruit_name)}")

################################
# Задание 2 Добавьте к заданию 1 подсчет количества раз, когда 
# название фрукта является частью элемента. Например: 
# banana, apple, bananamango, mango, strawberry-banana.
# В примере выше banana встречается три раза.

# fruit_tuple = ("apple", "banana", "orange", "bananamango"
#                "mango", "strawberry-banana", "apple", "orange" )
# fruit_name = input("Please enter a fruit name: ")

# print(f"You fruit: {fruit_name}, exist in our tuple: {fruit_tuple.count(fruit_name)}")

# fruit_like_part = 0

# for fruit in fruit_tuple:
#     if fruit_name in fruit: 
#         fruit_like_part += 1

# print(fruit_like_part)

################################
# Задание 3
# Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0 
# до N раз). Пользователь вводит с клавиатуры название 
# производителя и слово для замены. Необходимо заменить 
# в кортеже все элементы с этим названием на слово для 
# замены. Совпадение по названию должно быть полным.

# manufacturer = ('lada', 'Mersedes', 'Haval', 'Cherry', 'BMW', 'Lada', 'Tesla')
# new_auto = input ("Enter new auto name: ")
# replace_auto = input("Enter auto name for replacement: ")

# updated_tuple = tuple(new_auto if auto == replace_auto else auto for auto in manufacturer)

# print(f"Updated auto tuple: {updated_tuple}")

################################
# Есть кортеж с целыми числами. Нужно вывести статистику
# по количеству цифр в элементах кортежа. Например:
# ■ Одна цифра — 3 элемента;
# ■ Две цифры — 4 элемента;
# ■ Три цифры — 5 элементов.

# this_dict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1985,
#     "colors": ["red", "white", "green"]
    
# }
# print(this_dict, len(this_dict))
# print(this_dict["model"])

# this_dict = dict(model="Mustang", year = 1964)
# print(this_dict, type(this_dict))
# print(this_dict.items())


#РЕШЕНИЕ
# integer_tuple = (1, 2, 22, 33, 44, 111, 222, 333, 444, 3, 55, 555)

# result_dict ={}

# for num in integer_tuple:
#     num_lenght = len(str(num))
#     if num_lenght in result_dict:
#         result_dict[num_lenght] += 1
#     else:
#         result_dict[num_lenght] = 1

# print(result_dict)
# print(result_dict.items())

# for length, count in result_dict.items():
#     print(f"■ {length} цифра  — {count} элемента")


