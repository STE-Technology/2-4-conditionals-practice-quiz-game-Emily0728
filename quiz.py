"""
File: quiz.py
Author: Emily Leal
Date: 2024-03-05
Description: created a multiple choice quiz
"""
print("Multiple-Choice Quiz Game")
print("")

# print questions and choices
print("what is the capital of Canada? \
      \n (a) Montreal \
      \n (b) Ottawa \
      \n (c) Toronto ")
score = 0
print(" ")

# user inputs answer and outputs whether it is correct or not
user_input1 = input("> ")
if user_input1 == "a":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print(" ")

#prints second set of questions with answers
print("What is the longest river in the world? \
       \n (a) Yangtze river \
       \n (b) Nile River \
       \n (c) Amazon River")
print(" ")

# prints if the users answer is correct or incorrect
user_input2 = input("> ")
if user_input2 == "b":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print(" ")

# prints third multiple choice question
print("which animal is the smallest? \
      \n (a) hummingbird\
      \n (b) bunny \
      \n (c) cat")
print(" ")

# prints if the users answer is correct or incorrect
user_input3 = input("> ")
if user_input3 == "a":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
print(" ")


# prints user total score out of 3 and their percentage
print("Quiz Complete!")
print("You answered " + str(score) + " out of 3 questions correctly. Your score is " + str(round((score/3) * 100,2)) + "%")



