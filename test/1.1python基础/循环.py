#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

num = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in arr:
    num = num + x
# print( num )
# print( list(range(5)) )
num1 = list(range(11))
del num1[0]
# for x in num1:
# print(x)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello,'+x+'!')

num2 = 10
while num2 > 0:
    num2 = num2 - 1
    if num2 % 2 == 0:
        continue
    print(num2)
print('{0:.3f}'.format(1.0/3))
print('{0:_^1}'.format('hello'))
print('你好{name},今天的天气是{weather}'.format(name='离岛', weather='晴天'))

s = '''awdjnaiwdbjuqabwdubauybvwduyagwdaw'''
print(s)
