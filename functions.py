import time


# Прочитать все числа из файла
def get_numbers_from_file(filename):
    nums = []
    file = open(filename)
    for string in file:
        for number in string.split():
            nums.append(float(number))
    file.close()
    return nums


# получить минимальное число из списка
def get_min_value(nums):
    if not nums:
        return None
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num


# Получить максимальное число из списка
def get_max_value(nums):
    if not nums:
        return None
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


# Получить сумму всех чисел
def get_sum_array(nums):
    if not nums:
        return None
    summary = 0
    for num in nums:
        summary += num
    return summary


# Получить произведение всех чисел
def get_comp_array(nums):
    if not nums:
        return None
    composition = 1
    for num in nums:
        try:
            composition *= num
        except OverflowError:
            return None
    return composition


# Дополнительная функция - поиск минимального нечетного целого отрицательного числа
def get_min_odd_neg(nums):
    if not nums:
        return None
    min_num = nums[0]
    for num in nums:
        if num < 0:
            if num % 2 != 0:
                if num < min_num:
                    min_num = num
    if min_num < 0:
        if min_num % 2 != 0:
            return min_num

    return None


# Проверка времени выполнения всех фунцкий
def get_time_execution(filename):
    a = time.time()
    nums = get_numbers_from_file(filename)
    min_num = get_min_value(nums)
    max_num = get_max_value(nums)
    sum_nums = get_sum_array(nums)
    compose_nums = get_comp_array(nums)
    min_odd_neg = get_min_odd_neg(nums)
    b = time.time()
    return b - a
