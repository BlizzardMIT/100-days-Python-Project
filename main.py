print("Tip calculator!")

bill = float(input("What is the total bill amount?\n$:"))
tip = int(input("How much tip would you like to give?\nPercent:"))
split = int(input("How many peopple to split the bill?\nPeople:"))

total = ("{:.2f}".format ((((bill * (tip/100)) + bill)  / split)))

print(f"Each person should pay: ${total}")
