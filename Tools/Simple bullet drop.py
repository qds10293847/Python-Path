# measurement input
meters_or_feet = input('What is your prefered unit of measurement? Meters or Feet?\n').lower()

# variables
# gravity = [9.81,32.17]
# hatsan_mod85_muzzle_velocity = [245,800]
# total_distance = [50,164.042]

# bullet drop function
def bullet_drop(muzzle_velocity, gravity, max_distance):
    t = []
    b_drop = []
    height = []
    for distance in range(0, max_distance, 2):
        t = distance / muzzle_velocity
        b_drop.append((gravity * 0.5) * (t ** 2))
        for t_drop in b_drop:
            height.append((12 - t_drop))
    print(height)



