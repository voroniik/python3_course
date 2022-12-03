# print('hello world')
# a = 5
# print(a*5)
# print(1, 2, 3, 4)
# print(1, 2, 3, 4, sep=' ')
# print(1, 2, 3, 4, sep='')
# print(1, 2, 3, 4, sep=',')
# print(1, 2, 3, 4, sep='*')
# print(1, 2, 3, 4, sep='###')
#
# print('5'+ '3')
# a = input()
# b = a[0:3].upper()
# c = a[-3:].upper()
# d = a[3:-3].lower()
# print(b,d,c, sep = "")
# r = int(input().upper())
# g = int(input().upper())
# b = int(input().upper())
# print('#'+ hex(r).replace('x','').lstrip('O').rjust(2, '0').upper(), hex(g).replace('x','').upper(), hex(b).replace('x','').upper(), sep = '')
#
# r = int(input())
# g = int(input())
# b = int(input())
# print('#'+ hex(r).strip('OX').rjust(2, '0').upper(), hex(g).replace('x','').upper(), hex(b).replace('x','').upper(), sep = '')
#
# a = hex(1)
# b = hex(2)
# c = hex(3)
# print(a+b+c)


#fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
#print(fib(31))
# n = int(input())
# sum = 0
# for i in range(0, n):
#     number = int(input())
#     sum += number
# print(sum)

# gender = {
#     'm': 'Дорогой',
#     'f': 'Дорогая',
# }
# a = [
#     ['Семён', 'Семёнов', 32.56, 'm'],
#     ['Зоя', 'Иванова', 378, 'f'],
#     ['Катерина', 'Петрова', 65, 'f'],
# ]
# for name, mid_name, balance, g in a:
#     text = f"""{gender[g]} {name} {mid_name},
# баланс Вашего лицевого счёта составляет {balance} руб."""
#     print(text)
# n = input()
# age = input()
# text = f'''Hello {name.upper()}.You are {age} years old.'''
# print(text)

# print(f'''Hello {input().upper()}.You are {int(input) + 77} years old.''')
# print(f'''{input().title()}, вам исполнится 77 лет в {int(input()) + 77}''')
#
# a = int(input())
# b = a // 60
# c = a % 60
# print(f'''{a} сек - это {b} мин. {c} сек.''')
#
# a = int(input())
# print(f'''{a} сек - это {a//60} мин. {a%60} сек.''')
#
# a, b = map(int,input().split())
# print(f'''Разрешение экрана: {a} x {b}.\nОбщее количество пикселей = {a * b}.''')
#
# a = int(input())
# b = int(input())
# print(f'''{a} / {b} = {a/b}\n{a} // {b} = {a//b}\n{a} % {b} = {a%b}''')


#print(f'''{(a := int(input()))} / {(b:= int(input()))} = {a/b}\n{a} // {b} = {a//b}\n{a} % {b} = {a%b}''')

# a, b = float(input()), int(input())
# print(f'''Current dollar rate is {a}. You want to buy {b} dollars\nYou must pay {a * b}''')

a, b = float(input('Введите курс доллара ')), int(input('Введите нужное количество долларов '))
print(f'''Current dollar rate is {a}. You want to buy {b} dollars\nYou must pay {a * b}''')