def tip_calc():
    price = input("Enter total price of meal: ")
    tip_percentage = input("Enter tip percentage: ")
    tip = float(price) * (float(tip_percentage)/100)
    print("Tip to be payed: ", tip)


tip_calc()