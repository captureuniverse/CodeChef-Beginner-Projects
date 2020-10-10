try:
    T = int(input())    # No. of testcases
    i = int(0)
    while i<T:

        N = int(input())    # Define a number
        sum = int(0)        # Define a variable to calc sum
        while N!=0:         # Till N!=0
            sum += N%10     # Get the last digit using remainder and add it to sum
            N=int(N/10)     # Then update N for next iteration using division function
        print(sum)          # Print sum

        i+=1
except:
    pass

