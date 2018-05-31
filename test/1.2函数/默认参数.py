#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 默认参数必须指向不变对象
def fn(a=None):
    if a == None:
        a = []
    a.append( 'apple' )
    print( a )
fn()
fn()
fn()