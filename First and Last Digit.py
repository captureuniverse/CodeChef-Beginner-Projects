try:
    T = int(input())
    i = int(0)
    while i < T:

        N = int(input())

        def First_Digit(n):
            while n >= 10:
                n = n/10
            return int(n)

        def Last_Digit(n):
            return n%10

        last_digit = Last_Digit(N)
        first_digit = First_Digit(N)
        sum = first_digit+last_digit
        print(sum)

        i += 1
except:
    pass