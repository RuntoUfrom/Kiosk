drinks = ["Ice Americano","Cafe Latte"]
prices = [2000,3000]

while True:
    menu = input(f"1) {drinks[0]} {prices[0]}won 2) {drinks[1]} {prices[1]}won  3) Exit")
    if menu =="1":
        print(f"{drinks[0]}  ordered. price is {prices[0]}")
    elif menu == "2":
        print(f"{drinks[1]} ordered. price is {prices[1]}")
    elif menu =="3":
        print("finish order")
        break
    else:
        print(f"{menu} menu is not exist. ")