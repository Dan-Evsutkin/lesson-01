def is_yer_leap(year):
    if(year % 4 == 0):
        print('Year', year, True)
    else:
        print('Year', year, False)

is_yer_leap(2023)