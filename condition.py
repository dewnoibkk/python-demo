if 5 > 6:
    print('5 more than 6')
else:
    print('6 less than 5')

if 5 > 5:
    print('5 more than 6')
elif 5 == 5:
    print('5 equal 5')
else:
    print('6 less than 5')


age_input = input('Type your age: ')
age = int(age_input)
if age < 20:
    print('Young')
elif age >= 20 and age < 50:
    print('Adult')
else:
    print('Senior')

