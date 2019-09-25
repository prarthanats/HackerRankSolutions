# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:10:24 2019

@author: Dell
"""

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count

n= 9
ar = [10,20,20,10,10,30,50,10,20]
10
1 1 3 1 2 1 3 3 3 3
result = sockMerchant(n, ar)