def tip_calculator():
    amount = float(input(f"Enter total price: "))
    tip = input(f"Enter tip percentage (default=20): ")
    if tip == '':
        tip2 = 20
    else:
        tip2 = float(tip)
    pay = amount * (tip2/100)
    gvh = amount + pay
    finalpay = round(gvh)
    print(f"You have to pay {finalpay}")