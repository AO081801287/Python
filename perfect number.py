'''n1 = int(input("Enter any number: "))
#l1=[]
sum = 0
for i in range(1, n1):
    if(n1 % i == 0):
       # values=int(input('enter numbers:'))
        #l1.append(values)
        sum = sum + i
if (sum == n1):
    print(n1,'is a Perfect number!')
else:
    print(n1, 'is not a Perfect number!')
'''
# decimal to binary

num1 = int(input('enter any number:'))
# printing original number 
print ("The original number is : " + str(num1)) 
  
# using bin() + list comprehension 
# decimal to binary number conversion  
result = [int(i) for i in bin(num1)[2:]] 
  
# printing result  
print ("The converted binary list is : " +  str(result)) 

