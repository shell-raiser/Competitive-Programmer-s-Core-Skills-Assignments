# -*- coding: utf-8 -*-

import sys
import numpy as np
A = np.ones([5000])
def main():
    x, y, z = map(int, input().split())
    result = -1
    A[0] = 0
    sizeit1 = 1
    sizeit2 = 2

    for i in range(1,2500):
        A[sizeit1] = ((A[sizeit1 - 1] + x))
        sizeit1 += 2
        A[sizeit2] = ((A[sizeit2 - 1] - y))
        sizeit2 += 2   
    
    if z in A:
        print(np.where(A==z)[0][0])
    else:
        print(-1)

    # result = np.where(A == z)
        
    # if result[0] ==  :
    #     print(-1)
    # else:
    #     print(result[0][0])

main()