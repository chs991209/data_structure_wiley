# R-1.1
# Write a short Python function, is.multiple(n , m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.
import datetime
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


# R-1.30
def divide_by_two():
    integer_input = input('Enter a number larger than 2: ')
    if int(integer_input) > 2:
        # input = 2 ** k로 간주한다
        k = math.log2(int(integer_input))
    else:
        raise ArithmeticError('Invalid input: Enter a number larger than 2')

    return math.floor(k)


# print(divide_by_two())


# P-1.31
def make_change(charged, given):
    # charged, given은 실수여야 한다.
    count_change = 0
    if charged > given:
        raise ValueError('Charged must be greater than given')
    elif charged < given:
        change = round(given - charged, 2)
        # change는 소수점 이하 2자리여야 한다.
        tuple_modf = math.modf(change)
        # 달러 지폐 부분인 정수부만 더합니다.
        count_change += tuple_modf[1]

        if tuple_modf[0] == 0:
            return int(count_change)
        else:
            # 1, 5, 10, 25, 50 센트가 존재
            # 100센트는 1달러와 동일한 값이므로 달러와 같은 개수로 계산되므로 무시합니다.
            # 0.33과 같은 소수부를 정수 33으로 바꿉니다.
            int_under_dot = int(tuple_modf[0] * 100)
            # int_under_dot은 1 이상 99 이하입니다.
            # int_under_dot / 50 => 1 or 0
            print('First Int', int_under_dot)
            if int_under_dot // 50 == 1:
                count_change += 1
                int_under_dot -= 50  # 0 이상 49 미만입니다.

            # int_under_dot => 0 이상 49 미만입니다.
            if int_under_dot // 25 == 1:
                count_change += 1
                int_under_dot -= 25  # 0 이상 25 미만입니다.

            # int_under_dot = > 0 이상 25 미만입니다.
            if int_under_dot // 10 >= 1:
                count_change += int_under_dot // 10
                int_under_dot -= 10 * (int_under_dot // 10)  # 0 이상 10 미만입니다.
                print('Int_under_dot: ', int_under_dot)

            # int_under_dot = > 0 이상 10 미만입니다.
            if int_under_dot // 5 == 1:
                count_change += 1
                int_under_dot -= 5  # 0 이상 5 미만입니다.

            if int_under_dot != 0:
                count_change += int_under_dot

            return int(count_change)


# print(make_change(2.5, 4.83))


# P-1.32

# GIL을 활용하면 쉽게 만들 수 있다.
def calculator():
    while True:
        num1 = float(input('Enter a float'))
        operator = input('Enter an operator: ')
        num2 = float(input('Enter another float'))
        operator2 = input('Enter an operator: ')

        if operator == '+':
            result = num1 + num2
        if operator == '-':
            result = num1 - num2

        if operator.lower() == 'x' or operator.lower() == '*':
            result = num1 * num2

        if operator == '/':
            result = num1 / num2

        if operator2 == '=':
            print('Result is', result)
            break


# calculator()

# P-1.34
def repeat_sentences_simulate(sentence):
    start_time = time.time()
    random_sentence_indices = set()
    random_count = 0
    while random_count < 8:
        random_idx = random.randint(1, 100)
        if random_idx not in random_sentence_indices:
            random_sentence_indices.add(random_idx)
            random_count += 1

    lower_alphabets = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    upper_alphabets = [chr(code) for code in range(ord('A'), ord('Z') + 1)]
    # ascii_of_all_alphabets = upper_alphabets + lower_alphabets

    len_sentence = len(sentence)

    for i in range(1, 101):
        if i not in random_sentence_indices:
            print(f'Number {i}: {sentence}', flush=True)
        else:
            done = False
            while not done:
                lower_alphabets_copy = lower_alphabets[:]
                upper_alphabets_copy = upper_alphabets[:]
                random_index = random.randint(0, len_sentence - 1)
                random_string_el = sentence[random_index]
                if random_string_el.islower():
                    lower_alphabets_copy.remove(random_string_el)
                    random_lower_alpha = random.choice(lower_alphabets_copy)
                    if random_index == len_sentence - 1:
                        modified_sentence = sentence[:random_index] + random_lower_alpha
                    else:
                        modified_sentence = sentence[:random_index] + random_lower_alpha + sentence[random_index + 1:]
                    print(f'Number {i}: {modified_sentence}', flush=True)
                    done = True
                elif random_string_el.isupper():
                    upper_alphabets_copy.remove(random_string_el)
                    random_upper_alpha = random.choice(upper_alphabets_copy)
                    if random_index == len_sentence - 1:
                        modified_sentence = sentence[:random_index] + random_upper_alpha
                    else:
                        modified_sentence = sentence[:random_index] + random_upper_alpha + sentence[random_index + 1:]
                    print(f'Number {i}: {modified_sentence}', flush=True)
                    done = True
    end_time = time.time()
    print('The time has been spent: {} sec'.format(end_time - start_time))


# Test the function with the given sentence


# "I will never spam my friends again."

# repeat_sentences_simulate('I will never spam my friends again.')


# P-1.35
def birthday_paradox():
    def birthday_convert(birth_list, birth_month, birth_day):
        if birth_month > 9:
            if birth_day > 9:
                birth_list.append("%d%d" % (birth_month, birth_day))
            else:
                birth_list.append("%d0%d" % (birth_month, birth_day))

        else:
            if birth_day > 9:
                birth_list.append("0%d%d" % (birth_month, birth_day))
            else:
                birth_list.append("0%d0%d" % (birth_month, birth_day))

    birthday_duplication_dict = {'ppl_under24': 0, 'ppl_over23': 0}
    n = 1
    while n <= 20:
        # 사람 수가 바뀔 때마다 랜덤 생성 list 초기화
        birthday_list = []
        for k in range(5 * n):
            # 랜덤 월 생성 초기화
            random_birthmonth = random.randint(1, 12)
            if random_birthmonth in (1, 3, 5, 7, 8, 10, 12):
                random_birthday = random.randint(1, 31)
                birthday_convert(birthday_list, random_birthmonth, random_birthday)

            elif random_birthmonth in (4, 6, 9, 11):
                random_birthday = random.randint(1, 30)
                birthday_convert(birthday_list, random_birthmonth, random_birthday)

            else:
                random_birthday = random.randint(1, 29)
                if random_birthday > 9:
                    birthday_list.append("02%d" % random_birthday)
                else:
                    birthday_list.append("020%d" % random_birthday)
        print(birthday_list)
        if n >= 5:
            if len(birthday_list) == len(set(birthday_list)):
                birthday_duplication_dict['ppl_over23'] += 0
            else:
                birthday_duplication_dict['ppl_over23'] += 1

        else:
            if len(birthday_list) == len(set(birthday_list)):
                birthday_duplication_dict['ppl_under24'] += 0
            else:
                birthday_duplication_dict['ppl_under24'] += 1

        n += 1
    birthday_duplication_percentage_under24 = float(birthday_duplication_dict['ppl_under24'] / 4)
    birthday_duplication_percentage_over23 = float(birthday_duplication_dict['ppl_over23'] / 16)
    print(">>>Birthday duplicated at least two time test result"
          "\n>>>When number of ppl under 24: %f\n"
          ">>>When number of ppl over 23: %f" % (birthday_duplication_percentage_under24,
                                                 birthday_duplication_percentage_over23))
    if birthday_duplication_percentage_over23 > 0.5:
        print(">>>>>>Paradox has been proved")


# birthday_paradox()


# R-1.36
def check_duplicated_counts():
    words_list = input('Enter the words separated by whitespace:\n>>>' + ' ')
    words_split = words_list.split(' ')
    words_dict = {}
    for word in words_split:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    for key, value in words_dict.items():
        print("word: {}, count: {}".format(key, value))

    return True


# check_duplicated_counts()
