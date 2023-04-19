'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.'''
import random  
n1 = int(input ("Введите количество элементов 1-го списка: "))
nums1 = [ ]
for i in range (n1): 
    nums1.append(random.randint(1,10))
print(nums1)
import random  

n2 = int(input ("Введите количество элементов 2-го списка: "))
nums2 = [ ]
for i in range (n2): 
    nums2.append(random.randint(1,10))
print(nums2)
num1 =set(nums1)
num2 =set(nums2)

num3 = num1.intersection(num2)
print(num3)
n1 = sorted(num3)
print(n1)
print(" ".join(map(str,n1)))