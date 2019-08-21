#single Table
n=int(input('enter the required table number:'))
m=int(input('enter the required maximun multiples:'))
for i in range(1,m+1):
      s=i*n
      print(n,'*',i,'=',s)
      
#MultipleTables
n=int(input('enter the required table number:'))
m=int(input('enter the required maximun multiples:'))
for i in range(1,n+1):
   for s in range(1,m+1):
      print(i,'*',s,'=',i*s)
   print('\n')

# Row wise Tables
n=int(input('enter the required table number:'))
m=int(input('enter the required maximun multiples:'))
for s in range(1,m+1):
   for i in range(1,n+1):
      print(i,'*',s,'=',i*s, end='\t\t')
   print('\n')

