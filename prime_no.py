print("This is prakash...")

#code to check a prime number:

num=int(input("Enter a number:"))
temp=0
for i in range(2,num):
    if (num%i==0):
        temp=temp+1

if (temp>0):
    print("not a prime number")

else:
    print(num,"is a prime no")
