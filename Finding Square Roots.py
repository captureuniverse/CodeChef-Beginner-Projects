import math

try:
    T = int(input())
    i = int(0)
    while i < T:
        N = int(input())
        N = math.sqrt(N)
        N = round(N)
        print(N)
        i += 1
except:
    pass