#Sorting in increasing order
# This program works fine but the problem is that this problem works slow
# So not accepted on CodeChef
final = []

A = []
t = int(input())
i = int(0)
while i < t:
    N = int(input())
    A.append(N)
    i += 1

l = len(A)
while l!=0:
    temp = A[0]
    k = int(0)
    while k < len(A)-1:
        if A[k+1] < A[k] and A[k+1] < temp:
            temp = A[k+1]
        elif A[k+1] < A[k] and A[k+1] > temp:
            temp = temp
        k += 1

    j = int(0)
    while j < len(A):
        if A[j] == temp:
            A.pop(j)
            l = l-1
        j += 1
    final.append(temp)

m = int(0)
while m<len(final):
    print(final[m])
    m += 1