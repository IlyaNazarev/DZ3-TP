import functions
from functools import reduce

file1 = "1.txt"
file2 = "2.txt"
file3 = "3.txt"
file4 = "4.txt"
file5 = "5.txt"

nums1 = functions.get_numbers_from_file(file1)
nums2 = functions.get_numbers_from_file(file2)
nums3 = functions.get_numbers_from_file(file3)
nums4 = functions.get_numbers_from_file(file4)
nums5 = functions.get_numbers_from_file(file5)
print(functions.get_min_odd_neg(nums1),
      functions.get_min_odd_neg(nums2),
      functions.get_min_odd_neg(nums3),
      functions.get_min_odd_neg(nums4),
      functions.get_min_odd_neg(nums5))


# Тестирование функции нахождения минимума
def test_min_value_1(array=nums1):
    assert functions.get_min_value(array) == -95718.0


def test_min_value_2(array=nums2):
    assert functions.get_min_value(array) == -100000.0


def test_min_value_3(array=nums3):
    assert functions.get_min_value(array) == -99490.0


def test_min_value_4(array=nums4):
    assert functions.get_min_value(array) == -99985.0


def test_min_value_5(array=nums5):
    assert functions.get_min_value(array) == -100000.0


# Тестирование функции нахождения максимума
def test_max_value_1(array=nums1):
    assert functions.get_max_value(array) == 95922.0


def test_max_value_2(array=nums2):
    assert functions.get_max_value(array) == 99968.0


def test_max_value_3(array=nums3):
    assert functions.get_max_value(array) == 97312.0


def test_max_value_4(array=nums4):
    assert functions.get_max_value(array) == 99984.04039


def test_max_value_5(array=nums5):
    assert functions.get_max_value(array) == 99998.0


# Тестирование функции нахождения суммы чисел
def test_sum_value_1(array=nums1):
    assert functions.get_sum_array(array) == 377770.0


def test_sum_value_2(array=nums2):
    assert functions.get_sum_array(array) == 6800713.0


def test_sum_value_3(array=nums3):
    assert functions.get_sum_array(array) == -300290.8321499999


def test_sum_value_4(array=nums4):
    assert functions.get_sum_array(array) == 65257609.80405004


def test_sum_value_5(array=nums5):
    assert functions.get_sum_array(array) == 681099319.7084807


# Тестирование функции нахождения произведения чисел
def test_compose_value_1(array=nums1):
    assert functions.get_comp_array(array) == float('-inf')


def test_compose_value_2(array=nums2):
    assert functions.get_comp_array(array) == float('-inf')


def test_compose_value_3(array=nums3):
    assert functions.get_comp_array(array) == float('-inf')


def test_compose_value_4(array=nums4):
    assert functions.get_comp_array(array) == float('inf')


def test_compose_value_5(array=nums5):
    assert functions.get_comp_array(array) == float('-inf')


# Тестирование функции нахождения проиведения чисел
def test_get_min_odd_value_1(array=nums1):
    assert functions.get_min_odd_neg(array) == -95045.0


def test_get_min_odd_value_2(array=nums2):
    assert functions.get_min_odd_neg(array) == -99955.0


def test_get_min_odd_value_3(array=nums3):
    assert functions.get_min_odd_neg(array) == -98947.0


def test_get_min_odd_value_4(array=nums4):
    assert functions.get_min_odd_neg(array) == -99985.0


def test_get_min_odd_value_5(array=nums5):
    assert functions.get_min_odd_neg(array) == -99997.0


# Проверка времени выполнения всех фунцкий
def test_time_exec_value_1():
    print(f"Все функции были выполнены за {functions.get_time_execution(file1)} секунд, размер файла - {len(nums1)} чисел")


def test_time_exec_value_2():
    print(f"Все функции были выполнены за {functions.get_time_execution(file2)} секунд, размер файла - {len(nums2)} чисел")


def test_time_exec_value_3():
    print(f"Все функции были выполнены за {functions.get_time_execution(file3)} секунд, размер файла - {len(nums3)} чисел")


def test_time_exec_value_4():
    print(f"Все функции были выполнены за {functions.get_time_execution(file4)} секунд, размер файла - {len(nums4)} чисел")


def test_time_exec_value_5():
    print(f"Все функции были выполнены за {functions.get_time_execution(file4)} секунд, размер файла - {len(nums5)} чисел")

