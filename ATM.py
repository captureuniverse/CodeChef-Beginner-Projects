try:
    withdraw, balance = input().split()
    withdraw = int(withdraw)
    balance = float(balance)
    if withdraw>balance-0.50 or withdraw%5!=0:
        print(balance)
    else:
        print(balance-withdraw-0.50)
except:
    pass