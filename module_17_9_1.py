# 0. Ввод данных

arr = input('Введите последовательность чисел через пробел: ')
num = int(input('Введите любое число: '))

# 1. Преобразование введённой последовательности в список

arr = list(map(int, arr.split()))

# 2. Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)

def ins_sort(array):  # Используется алгоритм сортировки вставками
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array

sorted_arr = ins_sort(arr)
print(f'Отсортированный список: {sorted_arr}')

# 3. Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу.

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] < element and element <= array[middle + 1]:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

if num <= sorted_arr[0]:
    print(f'Введенное число меньше, чем наименьшее число в списке, либо им является')
elif num >= sorted_arr[-1]:
    print(f'Введенное число больше, чем наибольшее число в списке, либо им является')
else:
    res = binary_search(sorted_arr, num, 0, len(sorted_arr))
    print(f'Элемент в списке, который меньше заданного числа: {arr[res]}, его индекс: {res}\n'
          f'Элемент в списке, который больше заданного числа: {arr[res+1]}, его индекс: {res+1}')