# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:55:34 2019
@author: Dell
"""
def ap(a,b):
    x = 0
    zz = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]>b[j]:
                x = x+1
                print(a[i],b[j],x)
                i = i+1
                j=j+1
            elif a[i]<b[j]:
                zz= zz+1
                print(a[i],b[j],zz)
                i = i+1
                j=j+1
        return x,zz


a = [5,6,7]
b = [3,3,10]
zk = ap(a,b)

        