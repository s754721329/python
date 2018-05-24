#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# import sys
# import demo2

# bbq = demo2
# print( sys )
# for val in sys.argv:
#     print( val )

# print( __name__ )
# bbq.print_max(2,3)
# print( dir(bbq) ) 
shopList = [ 'apple', 'pear', 'banana' ,'orange' ,'mango']
print( len( shopList ) )
shopList.sort()
print( shopList )

# print( infor.items(0) )
# for key,value in infor.items():
#     print( 'key:(),value:()'.format(key,value) )

s1 = set([1,2,3])
s2 = set([2,3,4])
print( s1 & s2 )

list1 = [1,2,3,4,4,5]
s3 = set(list1)
print( s3 )

s4 = set([1,2,2,3,4])
print( s4 )

print( hex(128947812393) )