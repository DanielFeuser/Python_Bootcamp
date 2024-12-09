import random
from turtledemo.nim import computerzug

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock,paper,scissors]
print("Wellcome to Rock/Paper/Scissors game!!!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user_choice >=0 and user_choice <=2:
    print(choices[user_choice])
computer_choice = random.randint(0,2)
print("Computer choice:\n",choices[computer_choice])

if user_choice >=3 or user_choice <0:
    print("You typed an invalid number. You lose!")

elif user_choice == 1 and computer_choice == 0:
    print("You Win")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
elif user_choice == 0 and computer_choice ==2:
    print("You Win")
elif computer_choice == user_choice:
    print("Draw")
else:
    print("You lose")