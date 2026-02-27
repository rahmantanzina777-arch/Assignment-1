#Check Even or Odd: Write a program to check if a given number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#Positive, Negative, or Zero: Determine if a number is positive, negative, or zero.
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#Vowel or Consonant: Write a program to check whether a character is a vowel or consonant.
ch = input("Enter a character: ").lower()

if ch in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
else:
    print("Consonant")


#Leap Year: Check if a given year is a leap year or not.
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


#Grade Evaluator: Given a score, print the grade (A, B, C, D, or F)based on predefined ranges.
score = int(input("Enter your score: "))

if score >= 80:
    print("Grade A")
elif score>=70 and score<80:
    print("Grade B")    
elif score>=60 and score<70:
    print("Grade C")
elif score>=40 and score<60:
    print("Grade D")
else:
    print("Grade F")


#Check Divisibility: Check if a number is divisible by both 5 and 11 or not.
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


#Max of Three Numbers: Find the largest of three numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


#Traffic Light: Given the color of a traffic light (red, yellow, green), print the action (stop, ready, go)

color = input("Enter traffic light color: ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("Running")