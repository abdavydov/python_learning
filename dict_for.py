user_0 = {
    'username': 'exti',
    'first_name': 'anton',
    'last_name': 'davydov',
    }
#print(user_0['username'])
for key, value in user_0.items():
    print('\nKey = ' + key)
    print('Value = ' + value.title())

for key in user_0.keys():
    print('Dictionary key is ' + key)

for value in user_0.values():
    print('Dictionary value is ' + value)
