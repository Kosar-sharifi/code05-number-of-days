days = int(input('enter number:'))
number_of_years = days // 365
number_of_weeks = (days - 365) // 7
number_of_days = (days - 365) % 7
print('number_of_years =', number_of_years)
print('number_of_weeks =', number_of_weeks)
print('number_of_days =',number_of_days)