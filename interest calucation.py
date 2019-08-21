#interest calculation

money=int(input('enter principal amount:'))
rate=float(input('enter the rate of interst per 100:'))
time=int(input('enter time period in months:'))
interest=money*rate*time/100  # formula=P*T*R/100;  P= Principal Amount, T=TimePeriod, R=Rate Of Interest
print('interest amount',interest,'\n','total amount',money,'+',interest,'=',money+interest)
