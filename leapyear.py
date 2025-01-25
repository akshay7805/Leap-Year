year=int(input("Enter the year- "))
if (year%4==0) and (year%100!=0) or (year%400==0):
    '''if year divisible by 4 and not divisible by 100 it is leap year or it 
    also divisible by 400'''
    print(f'{year} is leap year!')
else:
    print(f'{year} is not leap year!')    