operation_mark = '-'
x = 0
y = 0


def init(a, b):
    global x
    global y
    x = a
    y = b


def calc():
    return x - y


# import addition
# import substraction
# # '1+2*5'
# # ['1', '+', '2', '*', '5' ] -> ['1', '+' , '10'] -> ['11']
# #   0    1    2
# return lst.pop()

# # flot(0)  float (2)

# operation = '+'
# ops = {
#     '+': addition,
#     '-': substraction
# }
# model_of_arithmetic_oper = ops[operation]

# model_of_arithmetic_oper.init(1,2)
# result  = model_of_arithmetic_oper.calc()
