# "Try и Except".
def add_everything_up(a, b):
    try:
        return a + b
    except TypeError as exc:
        # print(f'Ошибка несоответствия типов: {exc}, складываем строки.')
        return str(a) + str(b)


# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# Вывод в консоль:
# 123.456строка
# яблоко4215
# 130.456
