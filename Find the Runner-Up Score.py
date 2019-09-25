# -*- coding: utf-8 -*-
## Find the Runner-Up Score!


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    Scores = sorted(scores)
    maxScore = Scores[n-1]
    z =[]
    for x in Scores:
        if x < maxScore:
            z.append(x)
    zk = len(z)
    maxSc = z[zk-1]
    print(maxSc)
    
    
#    
#Input (stdin)
#5
#2 3 6 6 5
#Expected Output
#5