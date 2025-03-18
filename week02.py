drinks = ["Ice Americano","Cafe Latte","watermelon juice"]
prices = [2000,3000,4900]
amounts = [0,0]
total_price = 0

def order_process(idx : int):
    global total_price
    print(f"{drinks[idx]}  ordered. price is {prices[idx]}")
    total_price += prices[idx]
    amounts[idx] += 1

menu_lists = ""
for k in range(len(drinks)):
    menu_lists += f"{k+1}) {drinks[k]} {prices[k]}won "
menu_lists = menu_lists + f"{len(drinks)+1})Exit "
while True:
    menu = input(menu_lists)
    if menu =="1":
        order_process(int(menu) -1)
    elif menu == "2":
        order_process(int(menu) - 1)
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
