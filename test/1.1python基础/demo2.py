#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a = 7//2
print(a)
print('{0:.3f}'.format(13/3))
print(13 % 3)

print(25.5 % 5)
print(-25.5 % 5)
print(5 ^ 3)
print(3 == 3)
print(3 == '3')

x = False
# 短路计算
print(x and y)
x1 = True
print(x1 or y1)

width = 3
height = 4
area = width * height
print('area is', area)
print(type(width))

print(range(5))
print(list(range(5)))


def say_hello():
    print('heollo')


say_hello()


def say(name, times=1):
    print( name * times )

say('hello')
say('hello ',3)

def def1( a, *list, **dic ):
    print(a)
    # list.push(7)
    for val in list:
        print( val )
    for val in dic:
        print( val )

def1( 1, 2, 3, c=4, d=5 )

def print_max( x, y):
    '''This is document.
    文档111
    c=1'''
    x = int(x)
    y = int(y)

    if( x > y ):
        print( x )
    else:
        print( y )

print_max(2,3)
print( print_max.__doc__ )
