#LeapYear.py
year=int(input('请输入年份:'))
if (year%400==0) or (year%4==0 and year%100!=0):
    print('Yes!')
else:
    print('No!')
