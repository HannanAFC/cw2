#Joel - added 9/12/24
#placeholder inputs for testing, in monthly because easier
income=int(input("What is your monthly income"))
cat=input("What is your national insurance category?")
#determining ni from category and income
if income <= 1048:
    ni=0
elif income > 1048 and income <= 4189 and cat in ["A","F","H","M","N","V"]:
    ni=(income-1048) * 0.08
elif income > 1048 and income <= 4189 and cat in ["J","L","D","Z"]:
    ni=(income-1048) * 0.02
elif income > 1048 and income <= 4189 and cat in ["C","K","S"]:
    ni=0
elif income > 1048 and income <= 4189 and cat in ["B","E","I"]:
    ni=(income-1048) * 0.0185
elif income > 4189 and cat in ["A","B","D","E","F","H","I","J","L","M","N","V","Z"]:
    ni=(income-1048) * 0.02
elif income > 4189 and cat in ["C","K","S"]:
    ni=0
#failsafing
elif cat not in ["A","B","D","E","F","H","I","J","L","M","N","V","Z","C","L","S"]:
    print("Enter valid National Insurance category")
    ni = None
#returning result
if ni is not None:
    takehome=(income - ni)
    print (takehome)
