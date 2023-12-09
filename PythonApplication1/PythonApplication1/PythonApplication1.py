"""
АВТОТЕСТЫ  PYTHON 2 СЕМИНАР 
"""
"""
import random

n = 10
items = [random.randint(0, 1) for _ in range(n)]
print(items)


coins = [1, 0, 0, 1, 1]

countZero = 0;
countOne = 0;

for i in range(len(coins)):
    if coins[i] == 0:
        countZero += 1
    if coins[i] == 1:
        countOne += 1

if countZero < countOne:
    print(countZero)
else:
    print(countOne)
"""

"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.


s = 4
p = 4
X = 0
Y = 0

def get_divisors(number):
    result = {1, number}
    for divisors in range(2, number // 2 + 1):
        if number % divisors == 0:
            result.add(divisors)
    return sorted(result)

divisors_array = get_divisors(p)
print(divisors_array)

for i in range(1, len(divisors_array) // 2 + 2):
    print(divisors_array[i - 1])
    print(divisors_array[-i])
    if divisors_array[i - 1] + divisors_array[-i] == s:
        X = divisors_array[i - 1]
        Y = divisors_array[-i]
        break;
        
print (X, Y)
"""

"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


n = 15
degree = 0
result = 0

while result < n:
    result = 2 ** degree
    if result > n:
        break;    
    print(result)
    degree += 1
"""

"""
АВТОТЕСТЫ  PYTHON 3 СЕМИНАР
"""
"""
list_1 = [1, 2, 3, 4, 5]
print(list_1)
k = 3
print(f"k = {k}")
print(list_1.count(k))
"""

"""
import sys

list_1 = [1, 2, 3, 4, 5]
k = 6

i_min = 0
min_diff = sys.maxsize
print(list_1)
difference = 0
i = 0

while i < len(list_1):
      difference = k - list_1[i]
      if abs(difference) < min_diff:
        i_min = i
        min_diff = difference
      i += 1
      
print(list_1[i_min])
"""

"""
eng = 'qwertyuiopasdfghjklzxcvbnm'
rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
                 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}

k = 'ящерица'

if k[0].lower() in eng:
    summa = 0
    for letter in k:
         for key, value in list_English.items():
             if letter.upper() in value:
                 summa += key
    print(summa)
else:
    if k[0].lower() in rus:
        summa = 0
        for letter in k:
            for key, value in list_Russian.items():
                if letter.upper() in value:
                    summa += key
    print(summa)
"""

"""
СЕМИНАР 4. СЛОВАРИ, МНОЖЕСТВА И ПРОФИЛИРОВАНИЕ
"""

"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()

Решение:

word = 'a a a b c a a d c d d'
word = word.split()
count_letter = {}

for i in word:
    if i not in count_letter:
        count_letter[i] = 1
        print(f"{i}", end=' ')
    else:
        count_letter[i] += 1
        print(f"{i}_{count_letter[i] - 1}", end=' ')
"""

"""
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure. So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13

Решение:

text = "She sells sea shells on the sea shore The shells \
that she sells are sea shells I'm sure. So if she sells sea \
shells on the sea shore I'm sure that the shells are sea \
shore shells"

words = text.lower().replace('.', ' ').split()

print(len(set(words)))
"""

"""
АВТОТЕСТЫ  PYTHON 4 СЕМИНАР
"""

"""
var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5'

st1 = set(var2.split())
st2 = set(var3.split())
result = st1 & st2

for _ in sorted(result):
    print(_, end=' ')    
"""

"""
arr = [5, 8, 6, 4, 9, 2, 7, 3]
max_sum = 0
sum_of_three_beds = 0

for i in range(len(arr)):
    sum_of_three_beds = arr[i-2] + arr[i-1] + arr[i]
    if sum_of_three_beds > max_sum:
        max_sum = sum_of_three_beds

print(max_sum)
"""

"""
СЕМИНАР 5. РЕКУРСИЯ И АЛГОРИТМЫ
"""

"""
n = 5

def fibonaci(n):
    if n == 0:
        return 0
    if n <= 2:
        if n in [1, 2]:
            return 1
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)
    
"""

"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1



a = [1, 3, 3, 3, 4]

maximum = max(a)
minimum = min(a)

for i in a:
    if a[i] == maximum:
        a[i] = minimum
        
print(a)

b = [2, 8, 3, 3, 4]

max1 = max(b)
min1 = min(b)

for i in b:
    if b[i] == max1:
        b[i] = min1
        
print(b)
"""

"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes


def is_simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print('Input your number: ')
user_number = int(input())

print('Number is prime' if is_simple(user_number) else "Number isn't prime")
"""


"""
ЗАДАЧА ПРО 100 ДВЕРЕЙ
"""

"""
Есть 100 дверей. Изначально все закрыты. Каждую секунду двери меняют свое состояние в зависимости от того, 
делится ли номер двери на текущую секунду нацело.
Сколько дверей будут открыты через 100 секунд?


doors = [0] * 99
perfect_roots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
opened_doors = 0

for i in range(len(doors)):  
    if i in perfect_roots:
        doors[i*i - 1] = 1
        opened_doors += 1
        print(f"Number of opened door is {i*i}")
        
print(f"Total opened doors after 100 seconds is {opened_doors}")
"""
        

"""
Задача №37. Решение в группах

Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3

def my_reverse_func(n):
    if n == 1:
        return input()
    string = input()
    return my_reverse_func(n - 1) + ' ' + string

print("Количество элементов в последовательности: ")
user_string = int(input())
print("Введите числа последовательности через Enter: ")
print(f"Развернутая последовательность: {my_reverse_func(user_string)}")
"""

"""
АВТОТЕСТЫ  PYTHON 5 СЕМИНАР
"""

"""
def f(a, b):
    if b == 0:
        return 1
    return f(a, b-1) * a

print(f(2, 4))
"""

"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

Функция не должна ничего выводить, только возвращать значение.


def sum(a, b):    
    if a <= 0:
        return b   
    return sum(a - 1, b + 1)

print(sum(4, 5))
"""

"""
СЕМИНАР 6. ПОВТОРЕНИЕ СПИСКОВ
"""

"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод:
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1 

Вывод:
3 3 2 12


answer = []
print("Введите размер массива N: ")
n = int(input())
list_n = [0]*n
print(f"Введите {n} элементов массива N: ")
for i in range(n):
    list_n[i] = int(input())
 
print("Введите размер массива M: ")
m = int(input())
list_m = [0]*m
print(f"Введите {m} элементов массива M: ")
for i in range(m):
    list_m[i] = int(input())
 
print("Не повторяющиеся числа: ")
if n >= m:
    for i in list_n:
        if i not in list_m:
            answer.append(i)
else:
    for i in list_m:
        if i not in list_n:
            answer.append(i)
            
print(*answer)
"""

"""
Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод: 
5
1 2 3 4 5
Вывод:
0

Ввод:
5
1 5 1 5 1
Вывод:
2


count = 0
print("Введите размер массива N: ")
n = int(input())
list_n = [0]*n
print(f"Введите {n} элементов массива N: ")
for i in range(n): list_n[i] = int(input())

for i in range(1, len(list_n) - 1):
    if list_n[i] > list_n[i-1] and list_n[i] > list_n[i+1]:
        count += 1
        
print(count)
"""

"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:
1 2 3 2 3
Вывод:
2


#print("Введите размер массива N: ")
#n = int(input())
#list_n = [0]*n
list_n = [1, 2, 3, 2, 3, 3, 3]
count = 0
#print(f"Введите {n} элементов массива N: ")
#for i in range(n): list_n[i] = int(input())

for i in range(len(list_n) - 1):
    for j in range(i + 1, len(list_n)):
        if list_n[i] == list_n[j]:
            count += 1

print(count)


from collections import Counter

list_n = [1, 2, 3, 2, 3, 3, 3]
count = 0

cnt = dict(Counter(list_n))
print(cnt)


for n in cnt.values():
    count += (n * (n-1)) // 2
    
print(count)
"""

"""
Задача №45. Решение в группах
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод: 
300 
Вывод:
220 284


def get_divisors_sum(number):
    result = [1]
    for divisors in range(2, number // 2 + 1):
        if number % divisors == 0:
            result.append(divisors)
    return sum(result)

print("Ищем все пары дружественны чисел от 0 до k.\
Введите значение k, не превышающее 100.000.\
в противном случае k будет присвоено значение 100.000")
k = int(input())
if k > pow(10, 4):
    k = 10000
st = set()
for number in range(k + 1):
    kandidat = get_divisors_sum(number)
    if get_divisors_sum(kandidat) == number and kandidat != number:
        st.add(tuple(sorted((number, kandidat))))

for _ in st:
    print(*_)
"""

"""
АВТОТЕСТЫ  PYTHON 6 СЕМИНАР
"""

"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.


list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

for i in range(len(list_1)):
    if list_1[i] >= min_number and list_1[i] <= max_number:
        print(i)
"""

"""
Заполните массив элементами арифметической прогрессии. 
Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.


a1 = 5 # -1, 2, 5
d = -1 # -5, 3, -1
n = 10 # 2, 4, 10
cx = 2
next_one = 0

list_progress = [a1]

print(list_progress[0])
while cx <= n:  
    next_one = list_progress[0] + (cx - 1) * d    
    list_progress.append(next_one) 
    print(list_progress[cx - 1])
    cx += 1 
"""

"""
СЕМИНАР 7. ФУНКЦИИ ВЫСШЕГО ПОРЯДКА
"""

"""
transformation = lambda i: i
values = [2, 3, 5, 7]
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
"""

"""
Задача №49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

1 СПОСОБ
def find_farthest_orbit(orbits):
    maximum = 1
    idx = 0
    for i in range(len(orbits)):
        lst = list(orbits[i])
        if lst[0] * lst[1] > maximum and lst[0] != lst[1]:
            maximum = lst[0] * lst[1]
            index = i
    return orbits[index]
    
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]  
print(find_farthest_orbit(orbits))
   
2 СПОСОБ
def find_farthest_orbit2(orbits):
    filtered_orbits = list(filter(lambda orbit: orbit[0] != orbit[1], orbits))
    squares = list(map(lambda orbit : orbit[0] * orbit[1], filtered_orbits))
    max_square = max(squares)
    result = list(filter(lambda orbit: orbit[0] * orbit[1] == max_square, filtered_orbits))
    return result[0]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit2(orbits))
 
3 СПОСОБ
def find_farthest_orbit3(orbits):
    filtered_orbits = list(filter(lambda orbit: orbit[0] != orbit[1], orbits))
    return max(filtered_orbits, key = lambda orbit : orbit[0] * orbit[1])

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit3(orbits))
"""

"""
АВТОТЕСТЫ  PYTHON 7 СЕМИНАР
"""

"""
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. 
В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.


stroka = 'мо-локо и мёд'
#stroka = 'пара-ра-рам'
vowels = 'уеыаоэяиюё'

phrases = stroka.split()
count_vowels_arr = []
count_words = 0
vowels_sum = 0
for word in phrases:
    count_words += 1
    count_vowels = 0    
    for letter in word:    
        if letter in vowels:
            count_vowels += 1
    count_vowels_arr.append(count_vowels)
    vowels_sum += count_vowels

if count_words == 1:
    print('Количество фраз должно быть больше одной!')    
if vowels_sum / count_vowels == count_words and count_words != 1:
    print('Парам пам-пам')
elif count_words != 1:
    print('Пам парам')   
 """   


"""
Напишите функцию print_operation_table(operation, num_rows, num_columns), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: бинарной операцией называется любая операция, 
у которой ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")    
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))

print_operation_table(lambda x, y: x * y, 3, 3)    
"""



