import numpy as np
import random
import re
# board: 1-10, A-J
# pieces with size: carrier-5 battleship-4 destroyer-3 submarine-3 patrol boat-2

# Battlefields
grid_user = np.array([[':)','A','B','C','D','E','F','G','H','I','J'],
             ['01', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['02', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['03', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['04', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['05', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['06', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['07', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['08', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['09', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['10', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
grid_guess = np.array([[':)','A','B','C','D','E','F','G','H','I','J'],
             ['01', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['02', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['03', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['04', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['05', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['06', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['07', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['08', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['09', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['10', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])
grid_pc = np.array([[':)','A','B','C','D','E','F','G','H','I','J'],
             ['01', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['02', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['03', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['04', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['05', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['06', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['07', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['08', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['09', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['10', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])

def position():
    plane = ['vertical','horizontal']
    ship_size = [5,4,3,3,2]
    letter = ['C','B','D','S','P'] 
    rd_x = random.randint(1,10)
    rd_y = random.randint(1,10)
    rd_direction = random.choice(plane)
    
    for index, size in enumerate(ship_size, 0):
        rd_z = random.randint(size+1,11)
        cords = rd_z-size 
        # if rd_direction == plane[0]:
        #     if np.char.isalpha(grid_pc[cords:rd_z,rd_y]).all() == False:
        #         grid_pc[cords:rd_z,rd_y] = letter[index]
        #     else:
        #         while np.char.isalpha(grid_pc[cords:rd_z,rd_y]).all() == True:
        #             grid_pc[cords:rd_z,rd_y] = letter[index]
        # elif rd_direction == plane[1]:
        #     if np.char.isalpha(grid_pc[rd_x,cords:rd_z]).all() == False:
        #         grid_pc[rd_x,cords:rd_z] = letter[index]
        #     else:
        #         while np.char.isalpha(grid_pc[rd_x,cords:rd_z]).all() == True:
        #            grid_pc[rd_x,cords:rd_z] = letter[index]
        if rd_direction == plane[0]:
            grid_pc[cords:rd_z,rd_y] = letter[index]
        else:
            grid_pc[rd_x,cords:rd_z] = letter[index]       
    print(grid_pc)
position()
# position(5,'C')
# position(4,'B')
# print(grid_pc)
# who starts
#choice_start = input('Decide who goes first: user or pc\n').lower()

# pc boat placement


# pc target user



# cleaning and outputting
# array_string1 = np.array_str(grid_user)
# array_string2 = np.array_str(grid_guess)
# array_string3 = np.array_str(grid_pc)
# grid_user_cleaned = re.sub(r"[['\]]", "", array_string1) # Remove brackets and quotes
# grid_guess_cleaned = re.sub(r"[['\]]", "", array_string2) # Remove brackets and quotes
# grid_pc_cleaned = re.sub(r"[['\]]", "", array_string3) # Remove brackets and quotes
# print('This is your battlefield!\n'
#       'Pieces: carrier     = C\n        battleship  = B\n        destroyer   = D\n'
#       '        submarine   = S\n        patrol_boat = P\n'
#       , grid_user_cleaned,'\n')
# print('This is your guesses!\nH for hit, M for miss and * for sunk\n', grid_guess_cleaned)
# print(grid_pc_cleaned)