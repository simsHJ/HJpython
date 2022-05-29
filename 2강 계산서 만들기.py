print("Welcome to the tip calculator!")

money = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
split = int(input("How many people to split the bill?"))

tips = (tip / 100) + 1
final_money = (money * tips) / split
final_money_1 = round(final_money,2)

print(f"Each person should pay: {final_money_1}")