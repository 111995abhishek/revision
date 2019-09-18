#year=2019
#if year%4==0:
 #   if year%100!=0:
  #      leap=True
#elif year%4==0:
 #   if year%100==0:
  #  elif year%400==0:

   # leap=True
#else:
 #   leap=False
# Python Program to Check Leap Year using If Statement

year=2019
n=0
while n<=20:
    if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        print("%d is a Leap Year" % year)
    else:
        print("%d is Not the Leap Year" % year)
    break
    year=year+1

print(year)





