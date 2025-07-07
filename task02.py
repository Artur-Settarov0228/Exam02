
def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount <= balance:
        return balance-amount
    else:
        return "yetarli mablag' yetarli emas "
    
def check_balance(balance):
    print(f"joriy balance : {balance} som")


balance = 10000
print(f"boshlangin balance {balance}")

amal = input("Amallarni  kiriting: (deposit / withdraw / check balance): ").lower()

if amal=="deposit":
    amount = int(input("Miqdorni kiriting:"))
    balance = deposit(balance, amount)
    print(f"yangi balance : {balance} som ")
elif amal == "withdraw":
    amount = int(input("miqdorni kiriting :"))
    natija = withdraw(balance , amount)
    if isinstance(natija, int):
        balance = natija
        print(f"yangi balans : {balance}")
elif amal =="check_balance":
    check_balance(balance)
else:
    print("error error  error error error (*_*)")



   