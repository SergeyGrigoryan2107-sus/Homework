def counting_sort_by_digit(arr, exp):
    """
    Вспомогательная функция для сортировки массива по указанному разряду.
    :param arr: исходный массив
    :param exp: показатель степени десятки (экспонента), определяющая разряд
    """
    output = [0] * len(arr)
    count = [0] * 10  # Всего 10 возможных цифр (0–9)

    # Подсчёт частоты появления каждой цифры в разряде
    for i in range(len(arr)):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Преобразование частот в индексы для вывода
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Собираем отсортированный массив
    for i in range(len(arr) - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Копируем отсортированные элементы обратно в оригинальный массив
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Главная функция поразрядной сортировки.
    :param arr: входной массив чисел
    """
    # Находим максимальное число для определения максимальной разрядности
    max_num = max(arr)

    # Экспонента представляет собой степень десятки, соответствующую текущему разряду
    exp = 1
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

# Пример использования
numbers = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(numbers)
print("Отсортированный массив:", numbers)




