#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def fn( *arr ):
    num = 0
    for n in arr:
        num = num + n * n
    return num
    
print( fn( 1,2,3,4 ) )
print( fn( 2,3,4,5 ) )

ary = ( 3,4,5,6 )
print( fn( ary[0],ary[1],ary[2] ) )


# 命名关键字参数
def fn1( a, b, **c ):
    print( a )
    print( b )
    print( c )

fn1( 'aa','bb',city='beijing',name='18' )