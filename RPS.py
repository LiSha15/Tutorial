import random
print ("-------------Welcome------------")

user_score = 0
comp_score = 0
ties = 0

name = input ("Enter your User name here: ")
print("""
Winning Rules :
1. Paper vs Rock --> Paper
2. Rock vs Scissor --> Rock
3. Scissors vs Paper --> Scissor""")
print()
print("""
Choices are :
1. Paper
2. Rock 
3. Scissor""")
print()
print("-----User Choice-----")
print ()
choice = int (input("Enter your choice from 1-3: "))

print ()

while choice > 3 or choice < 1:
    choice = int (input("Enter valid number"))

if choice == 1:
    user_choice = "Paper"

elif choice == 2:
    user_choice = "Rock"

else:
    user_choice = "Scissor"

print ("The User's choice is",user_choice)
print()
print("-----Computer choice-----")
print()
print("Now it's computer's turn")
print()

computer = random.randint(1,3)

if computer == 1:
    comp_choice = "Paper"

elif computer == 2:
    comp_choice = "Rock"

else:
    comp_choice = "Scissor"

print("The Computer's choice is",comp_choice)

if ((comp_choice == "Paper" and user_choice == "Rock") or (comp_choice == "Rock" and user_choice == "Paper")):
    print("Paper wins")
    result = "Paper"

elif ((comp_choice == "Rock" and user_choice == "Scissor") or (comp_choice == "Scissor" and user_choice == "Rock")):
    print("Rock wins")
    result = "Rock"

else: 
    print("Scissor wins")
    result = "Scissor"

