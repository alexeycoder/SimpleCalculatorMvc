from model import provider as pr

__expr_raw_str: str = None
__result_cache: float = None


def __normalize_expression_str(expr_str: str):
    normalized_str = ''.join(expr_str.split()).replace(',', '.')
    for symb in pr.get_expression_valid_symbols():
        normalized_str = normalized_str.replace(symb, f' {symb} ')
    return normalized_str


def __normalized_expression_string_to_list(normalized_expr_str):
    def to_suitable_value(x):
        try:
            return float(x)
        except ValueError:
            return x

    expr_lst = normalized_expr_str.split()
    expr_lst = list(map(to_suitable_value, expr_lst))
    return expr_lst


def __first_occurence_index(lst: list, value, from_index=0, backward=False):
    """Ищет индекс первого вхождения указанного значения в списке.
    Возвращает None, если указанного значения не обнаружено вовсе.\n
    from_index -- начальная позиция поиска,\n
    backward -- вести поиск в обратном направлении.
    """
    last_index = len(lst) - 1
    assert 0 <= from_index <= last_index, \
        "Недопустимое значение аргумента from_index."

    enumer = lst
    start_index = from_index
    if backward:
        enumer = reversed(enumer)
        start_index = last_index - from_index
    enumer = enumerate(enumer)
    found_index = next((i for i, v in enumer
                        if i >= start_index and v == value), None)
    if backward and found_index:
        return last_index - found_index
    return found_index


def __wrap_subexpressions(expr_lst: list):
    fo_close_idx = __first_occurence_index(expr_lst, ')')
    if fo_close_idx is None:
        return expr_lst

    if fo_close_idx == 0:
        expr_lst.pop(0)
        return __wrap_subexpressions(expr_lst)

    bo_open_idx = __first_occurence_index(
        expr_lst, '(', fo_close_idx - 1, backward=True)
    if bo_open_idx is None:
        expr_lst.pop(fo_close_idx)
        return __wrap_subexpressions(expr_lst)

    subexpr_lst = expr_lst[bo_open_idx+1:fo_close_idx]
    for _ in range(fo_close_idx-bo_open_idx):
        expr_lst.pop(bo_open_idx)

    expr_lst[bo_open_idx] = subexpr_lst
    return __wrap_subexpressions(expr_lst)


def __solve_subexpression(subexpr_lst: list) -> float:
    def perform_operation(mark_index):
        op_mark = subexpr_lst[mark_index]
        op = pr.get_operation_by_mark(op_mark)
        op.init(subexpr_lst[mark_index-1], subexpr_lst[mark_index+1])
        res = op.calc()
        index_for_res = mark_index - 1
        subexpr_lst.pop(index_for_res)
        subexpr_lst.pop(index_for_res)
        subexpr_lst[index_for_res] = res

    def next_operation() -> bool:
        assert len(subexpr_lst) > 0, "Входящий список не должен быть пустым."
        if len(subexpr_lst) == 1:
            return False

        for marks_set in pr.get_operations_marks_by_priority():
            for i in range(len(subexpr_lst)-1):
                item = subexpr_lst[i]
                if item in marks_set:
                    perform_operation(i)
                    return True
        return False

    while next_operation():
        pass

    return subexpr_lst[0]


def __solve_complex_expression(expr_lst):
    for i in range(len(expr_lst)):
        item = expr_lst[i]
        if isinstance(item, list):
            expr_lst[i] = __solve_complex_expression(item)

    return __solve_subexpression(expr_lst)


def init(expression_str: str):
    global __expr_raw_str
    global __result_cache
    __expr_raw_str = expression_str
    __result_cache = None


def calc():
    if __result_cache:
        return __result_cache

    normalized_str = __normalize_expression_str(__expr_raw_str)
    expr_raw_lst = __normalized_expression_string_to_list(normalized_str)
    expr_tree = __wrap_subexpressions(expr_raw_lst)
    result = __solve_complex_expression(expr_tree)
    return result
