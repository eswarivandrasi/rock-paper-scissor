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
import random
numbers=int(input("what do you choose? type 0 for rock,1 for paper,2 for scissor"))
computer_chose=random.randint(0,2)
if computer_chose>numbers:
    print("you lose!")
elif computer_chose<numbers:
    print("you win!")
else:
    print("draw")