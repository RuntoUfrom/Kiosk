drinks = ["Ice Americano","Cafe Latte","watermelon juice"]
prices = [2000,3000,4900]
amounts = [0,0]
total_price = 0

menu_lists = ""
for k in range(len(drinks)):
    menu_lists += f"{k+1}) {drinks[k]} {prices[k]}won "
menu_lists = menu_lists + f"{len(drinks)+1})Exit "
while True:
    menu = input(menu_lists)
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
for i in range(len(drinks)):
    if amounts[i]>0:
        print(f"{drinks[i]} {prices[i]} {amounts[i]} {prices[i] * amounts[i]}")

print(f"total price is {total_price}")
