str_1 = 'результат операции: 42'
str_2 = 'результат операции: 514'
str_3 = 'результат работы программы: 209'
str_4 = 'результат: 2'


def summarizing(string):
    colon_index = string.index(':')
    final_number = int((string[(colon_index + 1)::]).lstrip()) + 10
    return final_number


print(summarizing(str_1))
print(summarizing(str_2))
print(summarizing(str_3))
print(summarizing(str_4))
