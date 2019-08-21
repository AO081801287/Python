# Maximum Minimum And Average of N Numbers
l1=[]  # empty list
n1=int(input('how many numbers you want:'))
sum=0
for i in range(0,n1):
   values=int(input('enter numbers:'))
   l1.append(values)  # appending values in list
   sum+=values 
   avg=sum/n1
print('Maximum element in the list is',max(l1))   # Max value
print('Minimum element in the list is :',min(l1))  # Min Value
print('Average of',n1, 'numbers is',avg)             # Avg  of n numbers

