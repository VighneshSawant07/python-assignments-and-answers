num = int(input("Enter number to find its factorial : "))
fact = 1
for i in range(2,num+1):
     fact*=i
print("The factorial of the given number is " + str(fact))
