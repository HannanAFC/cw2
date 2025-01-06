#Joel - added 9/12/24
income = int(input("Your annual income"))
if income <= 12570:
    tax = 0
elif income <= 50270:
    tax = (income - 12570) * 0.20
elif income <= 125140:
    tax = (50270 - 12570) * 0.20 + (income - 50270) * 0.40
else:
    tax = (50270 - 12570) * 0.20 + (125140 - 50270) * 0.40 + (income - 125140) * 0.45
takehome = income - tax
print("Your take-home pay is £",takehome)
