prog_numb = int(input('Введите число, которое нужно угадать: '))


def guess(first_number):
    while True:
        user_number = int(input('Введите число для сравнения:'))
        if user_number != first_number:
            print('Попробуйте снова')
            continue
        elif user_number == first_number:
            print('Поздравляю! Вы угадали!')
            break


guess(prog_numb)
