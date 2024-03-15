# R-1.1
# Write a short Python function, is.multiple(n , m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.
import math
import random


def is_multiple(n, m):
    if n == 2 * m:
        return True
    elif n % m == 0:
        return 'n = mi'
    else:
        return False


# var_a = 10
# var_b = 5

# print(is_multiple(var_a, var_b))


# R-1.2

# k is an integer
def is_even(k):
    return not abs(k) & 1


# print(is_even(0))


# R-1.3

def minmax(data):
    if len(data) == 1:
        return data[0], data[0]

    min_val = max_val = data[0]
    for num in data[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val


# sort()는 O(n^2)의 시간 복잡도를 가지고 있으므로, 정렬이 불필요하므로
# operator 비교 이후에 바로 값을 min_val, max_val로 할당하는 것이 좋다
# min or max로 할당하는 것은 상수 1, data의 길이를 n이라 하면 O(n)의 시간 복잡도를 가진다.

# print(minmax([1, 2, 3, 4, 5]))
#
# print(minmax([1, 2]))


# R-1.4

def sum_of_squares(n):
    """
        smaller_int = 1
        sum_squares = 0
        while smaller_int < n:
            sum_squares += smaller_int * smaller_int
            smaller_int += 1

        return sum_squares
    """
    return (n - 1) * n * (2 * n - 1) // 6


# print(sum_of_squares(1))


# R-1.5

def sum_of_squares2(n):
    return sum(k * k for k in range(0, n))


# print(sum_of_squares(4))


# R-1.6

def sum_of_odd_squares(n):
    sum_of_square = 0
    for k in range(1, n, 2):
        sum_of_square += k ** 2

    return sum_of_square


# print(sum_of_odd_squares(1))


# R-1.7

def sum_of_odd_squares_comprehension(n):
    return sum(k ** 2 for k in range(1, n, 2))


# print(sum_of_odd_squares_comprehension(3))


# R-1.8

# s[j] == s[j-n]


# R-1.9

for k in range(50, 90, 10):
    print(k, end=', ')

# R-1.10
print()
for k in range(-8, 10, 2):
    print(k, end=', ')

# R-1.11
print()
print([2 ** k for k in range(0, 9)])


# R-1.12

def random_one_element(iterable_object):
    random_index = random.randrange(0, len(iterable_object))
    return iterable_object[random_index]


print(random_one_element([1, 2, 3]))


# C-1.13

# 함수 시작 reverse_list_of_integer(integer_list):
#     배열의 가장 마지막 index로 향합니다.
#
#


# C-1.14

def check_distict_odd_numbers(integer_sequence):
    """
        odd_numbers_count = 0
        odd_number = None
        index = 0
        while index < len(integer_sequence):
            if integer_sequence[index] % 2 == 1:
                if odd_number != integer_sequence[index]:
                    odd_number = integer_sequence[index]
                    odd_numbers_count += 1
                    if odd_numbers_count == 2:
                        return True
            index += 1

        return False
    """
    odd_numbers_set = set()
    for number in integer_sequence:
        if number % 2 == 1:
            odd_numbers_set.add(number)
            if len(odd_numbers_set) == 2:
                return True

    return False


# print(check_distict_odd_numbers([1, 2, 1]))

# C-1.15

def check_elements_distinct(integer_sequence):
    """
        distinct_elements_set = set()
        for number in integer_sequence:
            if number not in distinct_elements_set:
                distinct_elements_set.add(number)
            else:
                return False

        return True

        :param integer_sequence:
        :return: Boolean
    """
    distinct_elements_set = set()
    for number in integer_sequence:
        if not distinct_elements_set.add(number):
            return False

    return True


# print(check_elements_distinct([1, 2, 3, 3]))


# C-1.16

print('No.')

# C-1.17
import time

print('No.', end='', flush=True)
time.sleep(1)
print('\r      ', end='', flush=True)
print(
    '\rThe for() reads the element of the data, but the process assigned the value of data element to the object value, '
    'but does not approach to the data itself to change the original data element')


def scale(data, factor):
    for i in range(0, len(data)):
        data[i] = data[i] * factor
    return data


# print(scale([1, 2, 3, 4, 5], 2))

# C-1.18
def generate_sequence():
    return [n * (n + 1) for n in range(0, 10)]


print(generate_sequence())


# C-1.19


def generate_alphabets():
    return [chr(n) for n in range(ord('a'), ord('z') + 1)]


print(generate_alphabets())


# C-1.20


def random_one_element_with_int(iterable_object):
    for i in range(len(iterable_object)):
        random_number = random.randint(0, len(iterable_object) - 1)

        iterable_object[random_number], iterable_object[i] = (iterable_object[i], iterable_object[random_number])

    return iterable_object


print(random_one_element_with_int([k for k in range(0, 100)]))


# C-1.21

def reverse_input():
    list_of_lines = []
    is_done = False
    while is_done is False:
        try:
            line = input('Enter Anything: ')
            list_of_lines.append(line)

        except EOFError as e:
            is_done = True
            break
    if is_done is True:
        list_of_lines.reverse()
        for line in list_of_lines:
            print(line)


# reverse_input()


# C-1.22

def products_to_float(a, b):
    c = []
    for i in range(len(a)):
        c.append(float(a[i] * b[i]))

    return c


# print(products_to_float([1, 2, 3], [3, 2, 1]))


# C-1.23

def overflow_exception(list_a):
    try:
        list_a[len(list_a)] = 123

    except IndexError:
        print("Don't try buffer overflow attacks in Python!")


# overflow_exception([1, 2, 3])


# C-1.24


# def count_vowels(string_data):
#     amount_vowels = 0
#     for string in string_data.lower():
#         if ord(string) in (97, 101, 105, 111, 117):
#             amount_vowels += 1
#
#     return amount_vowels

def count_vowels(string_data):
    amount_vowels = 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    for char in string_data.lower():
        if char in vowels:
            amount_vowels += 1

    return amount_vowels


# print(count_vowels('AASBS'))


# import string

def eliminate_non_alphabetic(s):
    """
    def eliminate_non_alphabetic(s):
        return ''.join([char for char in s if (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or ord(char) == 32)])

    def eliminate_non_alphabetic(s):
        punctuations = set(string.punctuation)
        return ''.join([char for char in s if char not in punctuations or char == ' '])
    """
    return ''.join(char for char in s if char.isalpha() or char.isspace())


print(eliminate_non_alphabetic('Hi, My name is'))


def check_equation_int():
    list_input = []
    for k in range(3):
        int_input = input("Enter a number: ")
        if type(int(int_input)) is not int:
            raise TypeError
        list_input.append(int_input)

    c = int(list_input[2])
    b = int(list_input[1])
    a = int(list_input[0])
    if c in (a + b, b - a, a * b):
        return True

    return False


# print(check_equation_int())


def norm(v, p=2):
    if p == 2:
        return sum([vector ** p for vector in v]) ** 0.5
    else:
        # p가 홀수이면 sum()의 리턴 값이 음수일 때 1/p 승을 계산하지 못하므로 abs()를 호출해서 데이터를 0 이상의 수로 전환해야 한다.
        return sum([abs(vector) ** p for vector in v]) ** (1 / p)




# print(norm([3, 3, 3], 3))
# print(81 ** (1/3))


# P-1.29
import time

def random_string(strings):
    start_time = time.time()
    random_strings = []
    is_done = False
    factorial_num = math.factorial(len(strings))
    while is_done is False:
        shuffled = strings[:]  # Copy the list to shuffle independently
        random.shuffle(shuffled)
        if shuffled not in random_strings:
            random_strings.append(shuffled)
        if len(random_strings) == factorial_num:
            print('It\'s done')
            is_done = True
    end_time = time.time()
    print('\nTime taken for: ', end_time - start_time)
    return random_strings


# print(random_string(['c', 'a', 't', 'd', 'o', 'g']))


