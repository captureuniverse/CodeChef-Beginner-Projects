try:
    T  = int(input())
    i = int(0)
    while i < T:
        N = input()
        N = list(N)

        def CountFour(listName):
            j = int(0)
            count = 0
            while j < len(listName):
                if listName[j] == "4":
                    count += 1
                j += 1
            return(count)

        count_four = CountFour(N)
        print(count_four)
        i += 1
except:
    pass