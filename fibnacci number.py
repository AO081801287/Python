#Fibanacci series
n1=int(input('enter the number up to required:'))
f1=0
f2=1
for i in range(1,n1+1):
   s=f1+f2
   print(s)
   f1=f2
   f2=s
   
# using functions
def fib(n1):
   n1=int(input('enter the number up to required:'))
   f1 = 0
   f2 = 1
   if n1 < 0:
      print("Invalid input") 
   elif n1 == 0:
      return f1 
   elif n1 == 1:
      return f2
   else:
      for i in range(2,n1+1):
         s= f1 +f2
         print(s)
         f1 = f2 
         f2 = s
      return f2  

print(fib(1))



