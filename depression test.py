# Importing the required libraries
import time
import sys
# Displaying the instructions
print("Please answer the following questions with a number from 0 to 3, depending on how often it occurs to you")
print("0 = never, 1 = several days, 2 = half the time, and 3 = almost every day.\n")

# Checking for invalid inputs
def check():
    if answer<0:
        print('invalid answers, please choose a number between 0 to 3')
        sys.exit()
    if answer>3:
        print('invalid answers, please choose a number between 0 to 3')
        sys.exit()
        
# Declaring the questions
questions = ["Little interest or pleasure in doing things?", 
             "Feeling down, depressed, or hopeless?", 
             "Trouble falling or staying asleep, or sleeping too much?", 
             "Feeling tired or having little energy?", 
             "Poor appetite or overeating?", 
             "Feeling bad about yourself - or that you are a failure or have let yourself or your family down?", 
             "Trouble concentrating on things, such as reading the newspaper or watching television?", 
             "Moving or speaking so slowly that other people could have noticed. Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?", 
             "Thoughts that you would be better off dead or of hurting yourself in some way?"]

# Declaring the score variable
score = 0

# Looping through the questions
for i, question in enumerate(questions):
    answer = int(input(f"{i+1}. {question} "))
    score += answer

# Displaying the results
print(f"\nYour total score is {score}.")
if score < 5:
    print("You have minimal symptoms of depression.")
elif score < 10:
    print("You have mild symptoms of depression.")
elif score < 15:
    print("You have moderate symptoms of depression.")
else:
    print("You have severe symptoms of depression.")
    
    
    
