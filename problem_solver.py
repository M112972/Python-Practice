#Step 2: Program Introduction
print("Welcome to Daily Life Problem Solver Toolkit")

#Step 3: Menu System
while True:
    print("....\n...Options.......")

    print("1. Calculate sum of two numbers")
    print("2. Check even or odd")
    print("3. Find maximum of three numbers")

    option = int(input("Please choose any option:"))

#Step 4: Sum Calculator
    if option == 1:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))

        sum = num1 + num2

        print(f"Summation: {sum}")

    
#Step 5: Even or Odd Checker 
    elif option == 2:
        num = int(input("Enter the num:"))

        if num % 2 == 0:
            print("The number is Even.")
        
        else:
            print("The number is Odd.")

# Step 6: Maximum Finder
    elif option == 3:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))

        if a>b:
            if a>c:
                print("Max Number: a.")
            else:
                print("Max Number: c.")
            
        elif b>a:
            if b>c:
                print("Max Number: b.")
            else:
                print("Max Number: c")

        else:
            print("c is the largest")

    else:
        print("Invalid number.")

#Step 7: Repeat Program Using Loop (Challenge Part)

    again = input("\nDo you want to solve another problem? (yes/no): ")

    if again == "no":
        print("Thanks for using the toolkit!")
        break
        
        

