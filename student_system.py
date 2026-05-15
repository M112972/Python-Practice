#  Step 2: Program Introduction

print("Welcome to Smart Student Life Management System!")

student_name = input("Student Name : ")
student_id = input("Student ID : ")
daily_study_hours = float(input("Daily Study Hours : "))
monthly_pocket_money = int(input("Monthly Pocket Money : "))

# Step 3: Main Menu System

print("\n========== MAIN MENU ==========\n")

print("1. Class Attendance Tracker")
print("2. Study Session Manager")
print("3. Exam Result Checker")
print("4. Monthly Expense Tracker")
print("5. Daily Problem Solver")
print("6. Exit")



while True:

    main_menu = int(input("Enter any option : "))

# Step 4: Class Attendance Tracker

    if main_menu == 1:

        print("\n...Class Attendance Tracker......\n")

        total_class = int(input("Total Class : "))
        attended_classes = int(input("Attended classes : "))

        attendance_percentage = (attended_classes * 100) / total_class

        print(f"Attendance Percentage : {attendance_percentage}")

        if attendance_percentage >= 75:
            print("Eligible for exam")
            
            
        else:
            print("Not Eligible.")
            

        


#  Step 5: Study Session Manager

    elif main_menu == 2:

        print("...\n...Study Session Manager.......")

        subject_name = input("Subject Name : ")

        for session in range(1,4):
            print(f"Study session {session} completed.")

        ask = input("Do you complete all sessions?(yes/no)")

        if ask == "yes":
            print("Great consistency!")
        else:
            print("Try to improve tomorrow.")

# Step 6: Exam Result Checker

    elif main_menu == 3:

        print("\n...Exam Result Checker...\n")

        python = float(input("Enter Marks in Python : "))
        mathematics = float(input("Enter Marks in Mathematics : "))
        english = float(input("Enter Marks in English : "))
        
        total_marks = python + mathematics + english
        average = total_marks / 3

        print(f"Average : {average}")

        if average >= 80:
            Grade = "A"
            
        elif average >= 70 and average < 80:
            Grade = "B"
            
        elif average >= 60 and average < 70:
            Grade = "C"
            

        else:
            Grade = "F"
            print("Grade : Fail")
        
        print(f"Grade : {Grade}")
        
# Step 7: Monthly Expense Tracker
    
    elif main_menu == 4:

        print("\n...Monthly Expense Checker...\n")

        food_ex = float(input("Food Expense :"))
        int_ex = float(input("Internet Expense :"))
        tra_ex = float(input("Transport Expense :"))
        oth_ex = float(input("Other Expense :"))

        total_ex = food_ex + int_ex + tra_ex + oth_ex

        budget_pocket = float(input("Enter your Monthly budget : "))

        print(f"Total Expense Monthly : {total_ex}")

        if total_ex > budget_pocket:
            reamain_money_exce = total_ex - budget_pocket

            print(f"Budget limit crossed : {reamain_money_exce}")

        else:
            remain_money = budget_pocket - total_ex

            print(f"You managed your expenses well. You have : {remain_money}")

#  Step 8: Daily Problem Solver

    elif main_menu == 5:

        print("\n...Daily Problem Solver...\n")

        print("\n 1. Even or Odd Checker")
        print("\n 2. Largest Number Finder among three")
        print("\n 3. Simple Sum Calculator")

        number = int(input("Enter an option : "))

        if number == 1:
            
            num = int(input("Enter a number : "))

            if num % 2 == 0:
                print("The number is even")
            else:
                print("the number is odd.")

        elif number == 2:

            a = int(input("Enter A :"))
            b = int(input("Enter B :"))
            c = int(input("Enter C :"))

            if a >b :
                if a > c:
                    print("A is the largest.")
                else:
                    print("C is the largest.")

            elif b > a:
                if b > c:
                    print("B is the largest.")
                else:
                    print("C is the largest.")

            else:
                print("C is the largest.")

        elif number == 3:
            num1 = float(input("Enter first number :"))
            num2 = float(input("Enter second number :"))

            sum = num1 + num2

            print(f"Summation : {sum}")

        else:
            print("Error!! Please choose 1,2 or 3")
    
    elif main_menu == 6:
        print("Exit")
        break
    else:
        print("Error! Please Enter 1-6")


#Step 9: Countdown Timer (While Loop Practice)

print("\n##Count Down##\n")

count = 0
n = int(input("Enter a number : "))
print(n)
while n != 1:
    n = n -1
    count = count + 1
    print(n)
    
count = count + 1
print(f"Count Down : {count}")
print("Session finished successfully.")

#  Step 10: Final Summary Report

print("\n========== FINAL SUMMARY ==========\n")

print(f"Student Name : {student_name}")
print(f"Student ID   : {student_id}")
print(f"Attendance   : {attendance_percentage}")
print(f"Last Grdae   : {Grade}")
print(f"Monthly Exp  : {total_ex}")
print(f"Remain Bal   : {remain_money}")

print("Thank you! for using the system.")
            




        

    
   

