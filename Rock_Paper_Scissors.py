import random

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
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
games = [rock, paper, scissors]
if choose == 0:
    print(games[0])
elif choose == 1:
    print(games[1])
else:
    print(games[2])
# print(games[choose])
numbers_game = len(games)
# print(numbers_game)
computer_number = random.randint(0, numbers_game - 1)
# print(computer_number)
computer_choose = games[computer_number]
print(f"Computer choose:\n {computer_choose}")
if choose >= 3 and choose < 0:
    print("You typed an invalid number, you lose!")
elif choose == computer_number:
    print("You Draw!")
elif choose == 0 and computer_number == 2:
    print("You Winnn!")
elif choose == 2 and computer_number == 0:
    print("You Lose!")
elif choose > computer_number:
    print("You Winnn!")
elif choose < computer_number:
    print("You Lose!")