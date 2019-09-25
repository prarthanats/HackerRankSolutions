# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:09:57 2019
#Finding the percentage
@author: Dell
Explanation 0
Sample Input 
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

Sample Output 
26.50
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks.keys():
        data = 0.0
        for x in student_marks[query_name]:
            data = float(data) + float(x)
    else:
        pass
    average = float(data/3)
    print("%.2f" % round(average,2))
