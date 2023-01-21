# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. 60 -> 2, 2, 3, 5

N = int(input('Введите число: '))
div = 2
while N > 1:
     if N % div == 0:
         print(div)
         N = N/div
     else:
         div += 1

# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.Пример:1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»Ответ. Закончилось: «Бурёнка»

def read_file():
     data_assortiment = []
     data_stock = []
     with open('assortiment mor.txt', 'r', encoding='utf-8') as file:
         data_assortiment = file.readlines(1)
         data_stock = file.readlines(2)

     return data_assortiment, data_stock


def convert_to_set(data):
     tmp = []
     for item in data:
         if '\n' in item:
             item = item.replace('\n', '')
             tmp += item.split(', ')
         else:
             tmp += item.split(', ')

     data = set(tmp)
     return data


assortiment, stock = read_file()
assortiment = convert_to_set(assortiment)
stock = convert_to_set(stock)
result = assortiment.difference(stock)
print(result)

# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.3 -> 3.142

N = int(input('Введите число - точность вычисления Пи: '))
print(round(sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(100)), N))


# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.1. 5x^2 + 3x2. 2. 3x^2 + x + 83. Результат: 8x^2 + 4x + 8

def read_file(track):
     data = []
     with open(track, 'r') as file:
         data = file.read().split()
         data = list(map(str, data))
     return data


def parse_item(object_from_list):
     tmp = []
     for item in object_from_list:
         for i in range(len(item)):
             if item[i] == 'x' and not item[i - 1].isdigit():
                 tmp.append("1")
                 tmp.append(item[i])
             else:
                 tmp.append(item[i])
     return tmp


def sum_of_multi(date1, date2):
     while len(date1) != len(date2):
         if len(date1) > len(date2):
             date2.append("0")
         else:
             date1.append("0")

     answer = ''
     for i in range(len(date1)):
         if date1[i].isdigit() and date2[i].isdigit() and date1[i - 1] != '^':
             answer += str(int(date1[i]) + int(date2[i]))
         elif date1[i].isdigit() and date1[i - 1] == '^':
             answer += date1[i]
         elif date1[i] == '0' or date2[i] == '0':
             if date1[i] == '0':
                 answer += date2[i]
             elif date2[i] == '0':
                 answer += date1[i]
         else:
             answer += date1[i]

     return answer


def write_file(data):
     with open('answer.txt', 'a', encoding='utf-8') as file:
         file.write(f"Сумма многочленов = {data}")


track_to_file1 = 'File1_to_Task5'
track_to_file2 = 'File2_to_Task5'
result = sum_of_multi(parse_item(read_file(track_to_file1)), parse_item(read_file(track_to_file2)))
write_file(result)
print(f"Сумма многочленов = {result}")








