try:
    T = int(input())        # Variable for testcases
    k = int(0)              # Variable for looping through testcases
    while k<T:              # Loop for testcases
        N = int(input())    # Define a variable for integer
        result = int(1)     # Define a variable for final result
        i = 1
        while i <= N:       # Loop for multiplying from 1 to N
            result *= i     # Multiply one by one
            i += 1          # Increase i by 1 for multiplying by next number
        print(result)       # Print final result
        k += 1              # Next testcase
except:
    pass
