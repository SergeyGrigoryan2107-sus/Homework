#Задание1
'''start = int(input("Введите начальное число диапазона: "))
end = int(input("Введите конечное число диапазона: "))

if start <= end:
    total_sum = sum(range(start, end + 1))
else:
    total_sum = sum(range(end, start + 1))

print(f"Сумма чисел в диапазоне равна: {total_sum}")'''
#Задание 2
'''def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result = gcd(num1, num2)
print(f"Наибольший общий делитель равен: {result}")'''
#Задание 3
'''number = int(input("Введите число: "))
divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(f"Все делители числа {number}: {divisors}")'''
#задание 4
'''number = int(input("Введите число: "))
count = 0

for digit in str(abs(number)):
    count += 1

print(f"Количество цифр в числе: {count}")'''
#Задание 5
'''positive_count = negative_count = zero_count = even_count = odd_count = 0

for i in range(10):
    num = float(input(f"Введите число {i+1}: "))
    
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1
        
    if num.is_integer():  # Проверка, является ли число целым
        if int(num) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print("\nСтатистика:")
print(f"Положительные числа: {positive_count}")
print(f"Отрицательные числа: {negative_count}")
print(f"Нули: {zero_count}")
print(f"Четные числа: {even_count}")
print(f"Нечётные числа: {odd_count}")'''




