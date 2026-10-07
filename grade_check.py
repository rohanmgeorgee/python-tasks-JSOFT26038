# Program to display grade based on 10th mark

marks = float(input("Enter your 10th mark (0-100): "))

if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: F (Failed)")