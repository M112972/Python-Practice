#Step-2:Print:"Welcome to Smart Eligibility & Performance Checker"

print("Welcome to Smart Eligibility & Performance Checker")

#-----------------------------------------------------------------

#Step 3: User Input Section

Name = input("Enter Your Name:")
Age = int(input("Enter your Age:"))
Exam_Score = int (input("Enter your Score:"))
Mothly_Income = int (input("Enter your Monthly Income:"))

#-----------------------------------------------------------------

#Step 4:Age Eligibility Check

if Age < 18:
    print("You are not eligible due to age restrictions.")
else:
    print("Age requirement passed.")

#-----------------------------------------------------------------

#Step 5: Score Evaluation (Using elif)

if Exam_Score > 100 or Exam_Score < 0:
    print("Sorry! Please enter a valid score")

elif Exam_Score >= 90:
    Grade = "A"

elif Exam_Score >= 75 and Exam_Score <= 89:
    Grade = "B"

elif Exam_Score >= 60 and Exam_Score <= 74:
    Grade = "C"

else:
    Grade = "Fail"

#-----------------------------------------------------------------

#Step 6: Step 6: Financial Support Check

if Mothly_Income < 0:
    print("Your Income is invalid")

elif Mothly_Income < 20000 and Exam_Score >= 75:
    Scholarship_Status = "Eligible for scholarship support."

else:
    Scholarship_Status = "Not eligible for Scholarship." 

#-----------------------------------------------------------------

#Step 7: Nested Condition (Advanced)

if Age >= 18:
    if Exam_Score >= 60:
        print("You Passed The Program")
    
    else:
        print("You Failed the Program")

else:
    print("You are not eligi")


print(".\n...Final Output Summary......")

print("Name:", Name)
print("Age:", Age)
print("Score:", Exam_Score)
print("Grade", Grade)
print("Scholarship_Status:", Scholarship_Status)