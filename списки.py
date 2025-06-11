import random

# Генерация случайного списка целых чисел длиной 20
random_list = [random.randint(-10, 10) for _ in range(20)]
print("Исходный список:", random_list)

# Определение минимального и максимального значений
minimum_value = min(random_list)
maximum_value = max(random_list)

# Подсчет количеств разных видов элементов
num_negatives = sum(1 for x in random_list if x < 0)
num_positives = sum(1 for x in random_list if x > 0)
num_zeros = sum(1 for x in random_list if x == 0)

# Вывод результатов
print(f"\nМинимальное значение: {minimum_value}")
print(f"Максимальное значение: {maximum_value}\n")
print(f"Количество отрицательных элементов: {num_negatives}")
print(f"Количество положительных элементов: {num_positives}")
print(f"Количество нулей: {num_zeros}")

