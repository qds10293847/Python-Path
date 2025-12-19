import matplotlib.pyplot as plt

# measurement input
meters_or_feet = input('What is your prefered unit of measurement? Meters or Feet?\n').lower()
# variable numbers
# meters
gravity_ms = 9.81
hatsan_mod85_muzzle_velocity_ms = 245
total_distance_meters = 50
# feet
gravity_fps = 32.17
hatsan_mod85_muzzle_velocity_fps = 800
total_distance_feet = 164.042
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
# if meters or feet
if meters_or_feet == 'meters':
    bullet_drop(hatsan_mod85_muzzle_velocity_ms, gravity_ms, total_distance_meters)
elif meters_or_feet == 'feet':
    bullet_drop(hatsan_mod85_muzzle_velocity_fps, gravity_fps, total_distance_feet)
else:
    print('You have entered the wrong parmeter!')
# plotting bullet drop

