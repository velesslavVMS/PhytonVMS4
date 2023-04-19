'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод. 
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль'''
n = int(input("Введите число кустов = "))
import random  
x = [ ]
for i in range (n): 
    x.append(random.randint(5,10))
print(x)
h = 0
for i in range(n+2):
    x.insert(0, x.pop())
    a = x[1]+x[2]+x[3]
    if a > h:
        h = a
print(f'наибольший урожай с 3-х соседних кустов = {h}')