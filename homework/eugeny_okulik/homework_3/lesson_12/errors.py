def calc(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Nolga bolish mumkun emas')
        return('Fail')

print(calc(int(input('raqam')), int(input('raqam'))))
print('hello! guys')