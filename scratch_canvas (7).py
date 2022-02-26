year = int(input('type a year'))
if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
    print('it is a leap year')
else:
    print('not a leap year')
