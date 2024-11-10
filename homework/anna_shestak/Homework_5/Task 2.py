
str_1 = 'результат операции: 42'
str_2 = 'результат операции: 514'
str_3 = 'результат операции: 9'

result_1 = str_1.index('42')
result_2 = str_2.index('514')
result_3 = str_3.index('9')

num_1 = int(str_1[result_1::]) + 10
num_2 = int(str_2[result_2::]) + 10
num_3 = int(str_3[result_3::]) + 10

print(num_1)
print(num_2)
print(num_3)
