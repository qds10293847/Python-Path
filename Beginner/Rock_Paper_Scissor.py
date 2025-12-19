import random
art = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)
''']
print('Welcome to Rock Paper Scissors')
# user chooses
user = int(input('What shall you play: 0 for Rock, 1 for Paper or 2 for Scissors?\n'))
print(art[user])
# pc randomly chooses
pc = random.randint(0,2)
rnd = art[pc]
print('Computer has chosen:\n' + rnd)
# check who wins
if user == pc:
    print('It\'s a Draw!')
elif (user == 0 and pc == 2) or (user == 1 and pc == 0) or user == 2 and pc == 1:
    print('You Win!')
else:
    print('You Lose!')