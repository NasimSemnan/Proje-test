mahsol = {}
usertedad = int(input("enter tedad :"))
for i in range(usertedad):
    usermahsol = input("enter mahsol :")
    tedadmahsol = int(input("enter tedad :"))
    mahsol[usermahsol] = tedadmahsol
    print(f"{usermahsol},{tedadmahsol}")
while True:
    userpay = input("che mahsoli mikhahi :")
    tedadpay = int(input("enter tedad pay :"))

    if userpay in mahsol:
        if mahsol[userpay] >= tedadpay:
            mahsol[userpay] -= tedadpay
            print(
                f"pardakht anjam shod {userpay}: {mahsol[userpay]}")
        else:
            print("nist mojodi")
    else:
        print("mahsol nist ")
    # edame bede ya na
    more = input("mikhahi bekhari bazam edeme midi  (yes/no): ")
    if more.lower() != "yes":
        print(" welcom finish! 🛍️")
        break
