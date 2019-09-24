# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:00:27 2019

@author: Dell
"""

marksheet=[]
scorelist=[]
c= []

import operator
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]  
        list1 = sorted(marksheet, key=operator.itemgetter(1))
        minimum = list1[0]
        zz = []
        for items in list1:
            if (items[1]) <= (minimum[1]):
                minimum = items

            else:
                zz.append(items)
        zzk = []
        mini = zz[0]
        for items in zz:
            if (items[1]) <= (mini[1]):
                mini = items
                zzk.append(mini)
        zk = sorted(zzk, key=operator.itemgetter(0))
        for k in zk:
            for j in k:
                if isinstance(j, str):
                    print(j)
                else:
                    pass
             
5
Prashant
52.22
Kush
52.223
Kant
52.222
Kanti
52.2222
Harshit
52.22222
