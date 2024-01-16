"""
У списку цілих, заповненому випадковими числами обчислити:

■ Суму негативних чисел;

■ Суму парних чисел;

■ Суму непарних чисел;

■ Добуток елементів з кратними індексами 3;

■ Добуток елементів між мінімальним та максимальним елементом;

■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
"""

# import random
# numbers = [random.randint(-10, 10) for _ in range(20)]
# print(numbers)
#
# #Суму негативних чисел
# sum_negative = sum(num for num in numbers if num < 0)
# print(sum_negative)
#
# #Суму парних чисел
# sum_even = sum(num for num in numbers if num % 2 == 0)
# print(sum_even)
#
# #Суму непарних чисел
# sum_odd = sum(num for num in numbers if num % 2 != 0)
# print(sum_odd)
#
# #Добуток елементів з кратними індексами 3
# product_multiple_of_3 = 1
# for num in range(0, len(numbers), 3):
#     product_multiple_of_3 *= numbers[num]
#     print(product_multiple_of_3)
#
# #Добуток елементів між мінімальним та максимальним елементом
# min_value, max_value = min(numbers), max(numbers)
# min_index, max_index = numbers.index(min_value), numbers.index(max_value)
#
#
# if min_index < max_index:
#     product_between_min_max = 1
#     for num in numbers[min_index + 1:max_index]:
#         product_between_min_max *= num
# else:
#     product_between_min_max = 1
#     for num in numbers[max_index + 1:min_index]:
#         product_between_min_max *= num
# print(product_between_min_max)
#
# #Суму елементів, що знаходяться між першим та останнім позитивними елементами.
#
# first_positive_index = None
# last_positive_index = None
#
# for i, num in enumerate(numbers):
#     if num > 0 and first_positive_index is None:
#         first_positive_index = i
#
# for i in range(len(numbers) - 1, -1, -1):
#     if numbers[i] > 0 and last_positive_index is None:
#         last_positive_index = i
#
# sum_between_first_last_positive = 0
#
# if first_positive_index is not None and last_positive_index is not None and first_positive_index < last_positive_index:
#     for i in range(first_positive_index + 1, last_positive_index):
#         sum_between_first_last_positive += numbers[i]
#
# print(f"The sum of elements between the first and the last positive elements: {sum_between_first_last_positive}")
#
#

"""
Є список цілих, заповнений випадковими числами. 

На підставі даних цього масиву потрібно:

■ Створити список цілих, що містить лише парні числа з першого списку;

■ Створити список цілих, що містить лише непарні числа з першого списку;

■ Створити список цілих, що містить лише негативні числа з першого списку;

■ Створити список цілих, що містить лише позитивні числа з першого списку.
"""

import random
random_numbers = [random.randint(-10, 10) for _ in range(10)]
print(random_numbers)

#Створити список цілих, що містить лише парні числа з першого списку;
even_numbers = [num for num in random_numbers if num % 2 == 0]
print(even_numbers)

#Створити список цілих, що містить лише непарні числа з першого списку;
odd_numbers = [num for num in random_numbers if num % 2 != 0]
print(odd_numbers)

#Створити список цілих, що містить лише негативні числа з першого списку;
negative_numbers = [num for num in random_numbers if num < 0]
print(negative_numbers)

#Створити список цілих, що містить лише позитивні числа з першого списку
positive_numbers = [num for num in random_numbers if num > 0]
print(positive_numbers)