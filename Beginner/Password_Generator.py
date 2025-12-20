import random
# Variables
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','`','~',',','<','.','>','/','?',';',':','\'','\"','\\','|','[','}',']','{']
# User inputs
abc = int(input('How many letters do you want in your password?: '))
nbr = int(input('How many numbers do you want in your password?: '))
sym = int(input('How many symbols do you want in your password?: '))
# function to get random elements from variables
choices = []
def random_choice(input, var_list):
    for item in var_list:
        if input > 0:
            choices.append(random.choice(var_list))
            input -= 1
    return choices
# Creating and returning password
random_choice(abc, letters)
random_choice(sym, symbols)
random_choice(sym, symbols)
random.shuffle(choices)
end_result = ''
for item in choices:
    end_result += item
print(f'Your new password is: {end_result}') 
