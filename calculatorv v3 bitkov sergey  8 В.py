a = int(input('a = '))
b = int(input('b = '))
print('выберите знак')
d = input()
if d == '+':
    print('a + b =', a + b)
elif d == '-':
    print('a - b =', a - b)
elif d == '*':
    print('a * b =', a * b)
elif d == '/':
    print('a / b =', a / b)
elif d == '**':
    print('a ** b =', a ** b)
print('Хотите продолжить, если хотите, введите ДА, если нет, введите НЕТ')
c = input()
while c == 'да' or 'ДА':
    a = int(input('a = '))
    b = int(input('b = '))
    print('выберите знак')
    d = input()  
    if d == '+':
        print('a + b =', a + b)
    elif d == '-':
         print('a - b =', a - b)
    elif d == '*':
        print('a * b =', a * b)
    elif d == '/':
        print('a / b =', a / b)
        if b == 0:
            print('операция невозможна')
    elif d == '**':
        print('a ** b =', a ** b)
        print('Хотите продолжить, если хотите, введите ДА, если нет, введите НЕТ')
        e = input()
        if e == 'ДА' or 'да':
            a = int(input('a = '))
    b = int(input('b = '))
    print('выберите знак')
    d = input()  
    if d == '+':
        print('a + b =', a + b)
    elif d == '-':
         print('a - b =', a - b)
    elif d == '*':
        print('a * b =', a * b)
    elif d == '/':
        print('a / b =', a / b)
    elif d == '**':
        print('a ** b =', a ** b)
if c == 'нет' or 'НЕТ':
    print('Досвидания')
    
