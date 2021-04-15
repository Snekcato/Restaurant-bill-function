def bill(subtotal):
    total=int(subtotal*1.10)
    return total

ana=bill(10)
juan=bill(15)
sarah=bill(25)

print("The total for table 3 is :", str(ana+juan+sarah)) ," dollars"
