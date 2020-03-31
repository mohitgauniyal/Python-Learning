def money(m):
    if m >= 10:
        print("Hurray! you can buy a coffee")
    else:
        print("You can't buy a coffee")


money(1)


def alcohol(age, money):
    if age >= 18 and money >= 60:
        print("You can buy an Alcohol.")
    elif age <= 18 and money >= 60:
        print("You are not eligible to buy an Alcohol.")
    elif age >= 18 and money <= 60:
        print("You don't have enough money.")
    else:
        print("You don't have money and you are not eligible.")


print("\n")
alcohol(19, 61)
alcohol(18, 59)
alcohol(17, 67)
alcohol(16, 18)
