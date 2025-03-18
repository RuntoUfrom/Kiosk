drinks = ["Ice Americano","Cafe Latte"]
prices = [2000,3000]
amounts = [0,0]
total_price = 0
#order_list = ''
while True:
    menu = input(f"1) {drinks[0]} {prices[0]}won 2) {drinks[1]} {prices[1]}won  3) Exit")
    if menu =="1":
        print(f"{drinks[0]}  ordered. price is {prices[0]}")
        total_price+=prices[0]
        amounts[0] += 1
        #order_list += drinks[0] + '\n'
    elif menu == "2":
        print(f"{drinks[1]} ordered. price is {prices[1]}")
        total_price+=prices[1]
        amounts[0] += 1
        #order_list += drinks[1] + '\n'
    elif menu =="3":
        print("finish order")
        break
    else:
        print(f"{menu} menu is not exist. ")

#print(order_list)
print(f"{drinks[0]} {prices[0]} {amounts[0]} {prices[0] * amounts[0]}")
print(f"{drinks[1]} {prices[1]} {amounts[1]} {prices[1] * amounts[1]}")
print(f"total price is {total_price}")
