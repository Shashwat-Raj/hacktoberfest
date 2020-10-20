def is_leap(year):
    leap = False
    if year%4==0 and year%100==0 and year%400==0:
        return True
    elif year%4==0 and year%100==0 and year%400!=0:
        return leap
    elif year%4==0:
        return True
    else:
        return leap
year = int(input('Enter the Year'))
print(is_leap(year))
