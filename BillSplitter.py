from random import choice

guest_count = int(input('Enter the number of friends joining (including you):\n'))

print('Enter the name of every friend (including you), each on a new line:\n')

# Adding guests to dictionary and taking bill
dinner = {input(): 0 for _ in range(guest_count)}

final_bill = int(input('Enter the total bill value:\n'))

# Splitting bill evenly for all guests
for key in dinner:
    dinner[key] = round((final_bill / guest_count), 2)

# "Who is lucky?" feature
if input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower() == 'yes':
    lucky_guest = choice(list(dinner.keys()))
    print(f'{lucky_guest} is the lucky one!')
    for key in dinner:
        dinner[key] = round((final_bill / (guest_count - 1)), 2)
    dinner[lucky_guest] = 0
else:
    print('No one is going to be lucky')
print(dinner)
