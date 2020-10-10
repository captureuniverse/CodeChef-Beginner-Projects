try:
    t = int(input())    #No. of lines for inputing one number in each line
    i = int(0)
    list_of_nums = []
    while i<t:
        temp = int(input())
        list_of_nums += [temp]
        i += 1
    sorted_list = sorted(list_of_nums)
    j = int(0)
    while j<len(sorted_list):
        print(sorted_list[j])
        j += 1
except:
    pass