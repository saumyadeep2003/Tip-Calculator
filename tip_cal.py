print("Welcome to tip calculator")
bill = float(input("Enter the total bill amount?\n$"))
tip = float(input("Enter the tip percentage?\n"))
people = int(input("Enter the number of people?\n"))

final_tip = round((tip/100 * bill + bill)/people)
print(f"Each person should pay ${final_tip}")
