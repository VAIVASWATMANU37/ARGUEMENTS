def total_calc(amount):
    tip = int(input("ENTER THE PERCENTAGE YOU WANT TO PAY: "))
    tip_amt = (tip / 100) * amount
    total = amount + tip_amt
    return total
Amt = int(input("ENTER THE AMOUNT YOU PAID: "))
TOTAL = total_calc(Amt)
print("YOUR TOTAL AMOUNT WILL BE:", TOTAL)