def coins(amount):
    coins5 = amount // 5
    left = amount - (coins5 * 5)
    coins2 = left // 2
    left2 = left - (coins2 * 2)
    coins1 = left2
    return coins5 + coins2 + coins1