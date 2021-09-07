#python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # your code
    maxnow = a[0]
    maxcount = 0
    maxpos = []

    for i in range(n):
        temp = a[i]
        if temp > maxnow:
            maxnow = a[i]
            maxcount = 1
            maxpos = []
            maxpos.append(i)
        elif temp == maxnow:
            maxcount += 1
            maxpos.append(i)

    

    if maxcount > 2:
        a.pop(maxpos[2])
    elif maxcount == 1:
        a.pop(maxpos[0])



    #print(str(result))
    print (" ".join(map(str, a)))



if __name__ == '__main__':
    main()