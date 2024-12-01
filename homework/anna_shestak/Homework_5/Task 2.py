
str_1 = 'результат операции: 42'
str_2 = 'результат операции: 514'
str_3 = 'результат работы программы: 9'

result_1 = str_1.index(':')
result_2 = str_2.index(':')
result_3 = str_3.index(':')

num_1 = int((str_1[(result_1+1)::]).lstrip()) + 10
num_2 = int((str_2[(result_2+1)::]).lstrip()) + 10
num_3 = int((str_3[(result_3+1)::]).lstrip()) + 10

print(num_1)
print(num_2)
print(num_3)
