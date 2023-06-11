
while True:
    a = int(input('Введите первое число '))

    b = int(input('Введите второе число '))

    operator = input('Введите действие: ')

    if operator == "+":
            print(a+b)
    elif operator == "-":
            print(a-b)
    elif operator == "*":
            print(a-b)
    elif operator == "/" and b != 0:
            print(a/b)
    else:
        print('Нет такого действия')
    break