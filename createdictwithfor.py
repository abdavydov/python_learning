aliens = []
for alien_number in range(30):
    new_alien = {'speed': 'slow', 'color': 'blue', 'points': '5'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print('aliens lenght is ' + str(len(aliens)))
