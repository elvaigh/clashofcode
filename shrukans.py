import sys
import math

m,a,n = [int(i) for i in raw_input().split()]

if (m*n*(n+1)/2 - a) <0:
    print 0
else:
    print m*n*(n+1)/2 - a
