try:
    T = int(input())
    i = int(0)
    while i < T:
        N = int(input())    # No. of cupcakes
        L = []              # List of leftover cupcakes where index+1 is the no. of packages
        j = int(1)
        while j < N+1:
            #temp = int(N%j)
            #L+=[temp]  # Getting leftover cupcakes in list L
            L.insert(j,int(N%j))
            j += 1
        temp = sorted(L)    # Sorted List of L
        max_left = temp[len(temp)-1] #Getting maximum leftover cupcakes
        max_package = int()
        for l in range(0,len(L)):
            if L[l] == max_left:
                max_package = l+1
        print(max_package)
        i += 1

except:
    pass