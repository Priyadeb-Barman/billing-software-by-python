from tabulate import tabulate  # for make menu in tabular form
# welcome customer
print("Welcome to Spyder Restaurant!")
print("What would you like to have today, Sir/Madam?")
# stor menu in dictionary
menu = {
    "coffee": 10,
    "tea": 7,
    "rice-Chicken": 100,
    "fried Rice": 150,
    "naan": 40,
    "butter Chicken": 150,
    "bread": 20
}
# or you can use long method to convert the dictionary to list of tuples
table = list(menu.items())
# keylist = list(menu.keys())
# valuelist = list(menu.values())
# table = list(zip(keylist, valuelist))
print(tabulate(table, headers=["Item", " Price (INR)"], tablefmt="pretty"))  # print the menu in tabuler form
total_bill = 0  # initialize the total bill
while True:
    print("Please, select your meal, Sir/Madam :)")
    order = input().strip().lower()

    if order in menu:
        price = menu[order]
        print(f"good choice sir/madam!!! your order {order} is added :)")
        quentity = int(input("Please Enter quentity  :) "))
        bill = price * quentity
        total_bill += bill
        print(f"Your bill for {order} is {bill} INR.")

    else:
        print("We are extremly sorry sir/mam !!!you order is not available at this moment ")

    nextorder = input("Do you want enethink else sir/mam :),\n(Enter YES or NO)").strip().lower()
    if nextorder != "YES":
        break
print(f"thank you for your oder ! \n Your total bill is {total_bill} INR")
print("Have a Good Day , Sir/Madam !!\n Please visit again ! ")
