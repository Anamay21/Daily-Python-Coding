print("Welcome to the Tip Calculator.")
total_bill = float(input("Enter the total bill: $"))
tip = int(input("Enter the tip percentage you would like to give (10, 12 or 15): "))
people = int(input("How many people to split the bill: "))
result = round((total_bill + (total_bill * (tip/100))) / people, 2)
print(f"Each person should pay: ${result}")
