def get_expression():
    return input('Введите число или арифметическое выражение: ')


def get_operation_mark():
    return input('Введите операцию ("=" - завершить): ')


def print_result(value, is_final=False):
    if is_final:
        print('='*40)
        print('Результат:'.upper(), value)
    else:
        print('Промежуточный результат:', value)


def print_expression_result(value):
    print('\tРезультат выражения:', value)


def print_zerodivision_error():
    print('Ошибка: Деление на ноль')
