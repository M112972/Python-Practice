#Step-2:Program Introduction

name = input("Enter your name:")

print("Welcome to Daily Life Tracker Program ",name,"!")

#----------------------------------------
#Step-3:User Information Section

name = input("Enter your name:")
hours = int(input("Total Available Hours:"))
Daily_Budget = float(input("Total Daily Budget:"))

print("\n-------User Information-------")
print("Name", name)
print("Daily available hours",hours)
print("Daily Budget",Daily_Budget)

#----------------------------------------

# Step 4: Daily Activity Input

python = float(input("Spend for studying python:"))
practice = float(input("Spend for practicing code:"))
other = float(input("Spend for other activities:"))

Total_Planned_Hours = python + practice + other

print("\n-----Total Activity Hours Planned For The Day-------")
print("Studying Python:",python)
print("Practicing Coding:",practice)
print("Other Activities:",other)
print("Total Acivity Hours Planned for the Today:",Total_Planned_Hours )

#----------------------------------------

# Step 5: Expense Input(hrs)

food = float(input("Expensing hours for eating food:"))
transport =float(input("Expensing hours for transportation:"))
other = float(input("Expensing hours for other:"))

Total_Expense = food + transport + other

print("\n-----Total Expense Hours Planned For The Day-------")
print("Food expense:", food)
print("Transportation expense:", transport)
print("Other expense:", other)
print("Total Expense:", Total_Expense)

#----------------------------------------

#Step 6: Time Planning Check

if Total_Planned_Hours > Total_Expense:
    print("You have planned more hours than available.")

else:
    print("Your daily plan is realistic.")

#----------------------------------------

#Step 7: Budget Check(optinal)

if Total_Expense > Daily_Budget:
    print("You have exceeded your daily budget.")
else:
    print("You are within your daily budget.")


#-----------------------------------------
    
#Step 8: Final Summary Output(optinal)

Remaining_Budget = Daily_Budget - Total_Planned_Hours

print("\n------Final Summary Output--------")

print("User Name:", name)
print("Total Planned Hours:",Total_Planned_Hours)
print("Available Hours:",hours)
print("Total Expense:", Total_Expense)
print("Remaining budget:", Remaining_Budget)