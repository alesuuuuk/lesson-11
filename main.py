# task 1
int_arr = [3, 5, 2, 6, 7, 9, -6, -2]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# def dubutok_int_arr(numbers_arr):
#     start_number = 1
#     for i in numbers_arr:
#         start_number *= i
#
#     return start_number
# print(dubutok_int_arr(int_arr))
#
# # task 2
#
# def min_int_arr(numbers_arr):
#     print(min(numbers_arr))
# min_int_arr(int_arr)
#
# # task 3
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def count_primes_in_list(num_list):
#     count = 0
#     for num in num_list:
#         if is_prime(num):
#             count += 1
#     return count
#
# # Приклад використання:
#
# result = count_primes_in_list(int_arr)
# print("Кількість простих чисел у списку: ", result)

# task 4
# def remove_element_from_list(lst):
#     count_removed = 0
#
#     while True:
#         target = input("Введіть число, яке потрібно видалити (або введіть 'exit' для виходу): ")
#
#         if target.lower() == 'exit':
#             break
#
#         try:
#             target = int(target)
#         except ValueError:
#             print("Некоректний ввід. Введіть число або 'exit' для виходу.")
#             continue
#
#         if target in lst:
#             lst.remove(target)
#             count_removed += 1
#             print(f"Елемент {target} видалено зі списку.")
#             print(f"Список після видалення: {int_arr}")
#         else:
#             print(f"Елемент {target} не знайдено у списку.")
#     print(f"Кількість видалених елементів: {removed_count}")
#     print(f"Список після видалення: {int_arr}")
#     return count_removed
#
#
# removed_count = remove_element_from_list(int_arr)


degreed_arr = []
def degree_fun(power, numbers):
    for i in numbers:
        degreed_arr.append(i**power)
    print(degreed_arr, " - новий список з елементами підянтими до ступеня ", power)




while True:
    try:
        choice = input("Введіть ступіть на який я підвищу усі елементи в списку (або введіть 'exit' для виходу): ")
        if choice == "exit":
            break
        else:
            degree_fun(int(choice), int_arr)
    except ValueError:
        print("Некоректний ввід. Введіть число або 'exit' для виходу")
# task 5

# similar_numbers_arr = []
# def similar_numbers(num_arr_one, num_arr_two):
#     for i in num_arr_one:
#         if i in num_arr_two:
#             similar_numbers_arr.append(i)
#     print(similar_numbers_arr, " - усі подібні числа в двох списках")
#     return similar_numbers_arr
# similar_numbers(int_arr, numbers)