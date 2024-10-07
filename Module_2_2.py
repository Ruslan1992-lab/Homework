#Ввод трех целых чисел
first = int(input('Put the first number:'))
second = int(input('Put the second number:'))
third = int(input('Put yhe third numder:'))

#Проверка на равенство
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)