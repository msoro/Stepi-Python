'''
Задача 1
a = int(input())
b = int(input())
c = int(input())

p = (a + b + c)/2
s = (p*(p-a)*(p-b)*(p-c))**0.5
print (s)
'''

'''
x = int(input())
#(−15,12]∪(14,17)∪[19,+∞) 
if (12 >= x > -15):
    print('True')
elif 17 > x > 14:
    print('True')
elif x >= 19:
    print('True')
else:
    print('False')
'''

'''
print('Input two numbers and operator (+, -, /, *, mod, pow, div):')
a = float(input())
b = float(input())
s = str(input())

if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)    
elif s == '/':
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
elif s == 'mod':
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')
elif s == 'pow':
    print(a ** b)
elif s == 'div':
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')
else:
    print('Wrong operator')
'''

'''
#Вычисление площадей
t = str(input())
if t == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print(s)
elif t == 'прямоугольник':
    a = float(input())
    b = float(input())
    s = (a*b)
    print(s)
elif t == 'круг':
    r = float(input())
    s = 3.14*(r**2)
    print(s)
else:
    print('Неопознанный формат')
'''

'''
#Min/Max/Rest
a = int(input())
b = int(input())
c = int(input())

if c >= b >= a:
    print(c)
    print(a)
    print(b)
elif b >= c >= a:
    print(b)
    print(a)
    print(c)  
elif a >= b >= c:
    print(a)
    print(c)
    print(b)
elif b >= a >= c:
    print(b)
    print(c)
    print(a)   
elif a >= c >= b:
    print(a)
    print(b)
    print(c)  
else: #c > a > b
    print(c)
    print(b)
    print(a)     
'''


# n-программистов
n = int(input())
if 20 >= n >= 1:
    if n == 1:
        print(str(n) + ' программист')
    elif 4 >= n >= 2:
        print(str(n) + ' программиста')
    elif 20 >= n >= 5:
        print(str(n) + ' программистов')
    
else:
    print('Превышено длпустимое число программистов')

    

