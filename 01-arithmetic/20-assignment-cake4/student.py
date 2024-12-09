def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    x1 = eggs / eggs_per_cake
    x2 = flour / flour_per_cake
    x3 = butter / butter_per_cake
    x4 = sugar / sugar_per_cake
    return min(x1, x2, x3, x4)