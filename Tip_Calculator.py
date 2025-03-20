print("Welcome to the tip calculator!")

#This is the total amount of the bill
bill = float(input("What was the total bill? $"))

#User will input the amount they would like to tip
tip = int(input("What percentage tip would you like to give? 20 25 30 "))

#How many people are splitting the bill
people = int(input("How many people to split the bill? "))

#This will calculater the tip and add it to the bill
tip_total = tip / 100 * bill + bill

#This takes the total bill plus the tip added and divides it among the people
print(f"Each person should pay: ${tip_total / people:.2f}")