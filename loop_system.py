# Step 2: Program Introduction
print("Welcome to Smart Task Repetition System")

# Step 3: Task Input
task_input = "Study Python"
repeat = int(input("How many times do they want to repeat this task today:"))

# Step 4: Using for Loop

for task in range(1, repeat+1):
    print(f"Task {task} {task_input} completed")

# Step 5: Countdown Using while Loop

countdown = int(input("Enter the Countdown:"))
n = int(input("Enter N:"))

while countdown <= n and countdown != 0:
    print(countdown)
    countdown = countdown -1

# Step 6: Nested Loop (Advanced Practice)

for session in range(2):
    if session == 0:
        session_name = "Morning"
    else:
        session_name = "Evening"

    for task in range(1,4):
        print(f"{session_name} Task {task}")


# Step 7: Infinite Loop Test (Learning Purpose)

counter = 1

while counter <= 5:
    print("Loop Running...", counter)
    counter = counter + 1


# Step 8: Final Output Summary

print("\n------ Final Summary ------")
print("Task Name:", task_input)
print("Repetitions Completed:", repeat)
print("Countdown Finished Successfully")