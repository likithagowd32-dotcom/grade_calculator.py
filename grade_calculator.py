# Grade Calculator Program

marks = int(input("Enter your marks (0-100): "))

# Check for invalid marks
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

else:
    # Grade calculation
    if marks >= 90 and marks <= 100:
        grade = "A"
        print("Grade: A")
        if marks >= 95:
            print("Message: Outstanding Performance!")
        else:
            print("Message: Excellent work!")

    elif marks >= 75 and marks <= 89:
        grade = "B"
        print("Grade: B")
        print("Message: Very Good!")

    elif marks >= 60 and marks <= 74:
        grade = "C"
        print("Grade: C")
        print("Message: Good, but you can improve.")

    elif marks >= 40 and marks <= 59:
        grade = "D"
        print("Grade: D")
        print("Message: Needs Improvement.")

    else:
        grade = "Fail"
        print("Grade: Fail")
        print("Message: Better luck next time.")
