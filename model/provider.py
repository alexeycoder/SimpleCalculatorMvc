from model import addition, substraction, multiplication, division

__operations = {
    addition.operation_mark: addition,
    substraction.operation_mark: substraction,
    multiplication.operation_mark: multiplication,
    division.operation_mark: division
}

__operations_marks = list(__operations.keys())
__expression_valid_symbols = __operations_marks + list('()')

# __most_priority_operations_marks = {
#     multiplication.operation_mark, division.operation_mark}

# __second_priority_operations_marks = {
#     addition.operation_mark, substraction.operation_mark}

__operations_marks_by_priority = [
    {multiplication.operation_mark, division.operation_mark},
    {addition.operation_mark, substraction.operation_mark}
]


def get_operations_marks() -> list[str]:
    return __operations_marks


def get_operations_marks_by_priority():
    return __operations_marks_by_priority


# def get_most_prior_marks() -> list[str]:
#     return __most_priority_operations_marks


# def get_second_prior_marks() -> list[str]:
#     return __second_priority_operations_marks


def get_expression_valid_symbols() -> list[str]:
    return __expression_valid_symbols


def get_operation_by_mark(mark):
    assert mark in get_operations_marks(), f'Операция "{mark}" не определена.'
    return __operations[mark]
