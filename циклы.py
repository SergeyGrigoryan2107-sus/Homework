# задание 2
'''start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
print("Все числа диапазона:")
for num in range(start, end + 1):
    print(num, end=" ")
print()  # Новый строка для разделения блоков вывода
print("Все числа диапазона в убывающем порядке:")
for num in range(end, start - 1, -1):
    print(num, end=" ")
print()  # Новый строка для разделения блоков вывода
print("Все числа, кратные 7:")
for num in range(start, end + 1):
    if num % 7 == 0:
        print(num, end=" ")
print()  # Новый строка для разделения блоков вывода
count_multiples_5 = 0
for num in range(start, end + 1):
    if num % 5 == 0:
        count_multiples_5 += 1
print(f"Количество чисел, кратных 5: {count_multiples_5}")'''
#Задание 1

# Ввод границ диапазона
'''start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for num in range(start, end + 1):
    if num % 7 == 0:
        print(num)'''
#Задание 3
# Ввод границ диапазона
'''start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)'''

