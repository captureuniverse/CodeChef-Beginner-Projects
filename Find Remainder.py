try:
    T = int(input())            #No. of testcases
    i = int(0)
    while i < T:
        A,B = input().split()   #Input two numbers with spaces
        A = int(A)
        B = int(B)
        print(A%B)              #Print their remainder
        i += 1                  # Upate i for next looping
except:
    pass


