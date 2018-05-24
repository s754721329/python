#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# print('111')
# print(r'''111
# 222
# 333''')
# print '333'
# name = input('bbq')
# bbq
# print(name)
a = 100
if a == 100:
    print('true')
else:
    print('false')
print(10 / 3)
print(a//3)
print(a % 3)
# print( 'Hello, \'Adam\'' )
# print('包含中文aaa')
print('Hello, %s' % 'world')
print('%.4d-%03d' % (3, 1))
print('%.3f' % 3.1415926)
print( 'Age: %s Gender: %s' % (25, True) )
print( '{0}的成绩提升了{1:.1f}%'.format('小明',17.155) )
# print( (85-72)/72*100 )
b = (85-72)/72*100
print( '浮点数格式化%.1f%%' % b )

arr = ['a','b','c']
arr.insert( 2,'d' )
print( arr )
print( len( arr ) )

arr1 = (1,)
arr2 = (1)
print( arr1 )
print( arr2 )

# s = input('birth:')
# numS = int(s)

# if numS<2000:
#     print('00前')
# else:
#     print('00后')

height1 = input('身高(m):')
weight1 = input('体重(kg):')
print( type(height1) )
print( type(weight1) )
height2 = float(height1)
weight2 = float(weight1)
print( type(height2) )
print( type(weight2) )
num1 = weight2/(height2*height2)
num2 =  '%.2f' % num1 
num = float(num2)
print(type(num2))
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
if num<=18.5:
    print('过轻')
elif num<=25:
    print('正常')
elif num<=28:
    print('过重')
elif num<=32:
    print('肥胖')
else:
    print('严重肥胖')

