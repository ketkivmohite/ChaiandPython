# 6. Factorial Character 
# Probelm : Compute the factorial of a number using a while loop 
# factorial (5!)= 5*4*3*2*1

n = int(input("Enter the number of the factorial you want : "))

factorial = 1 

while n > 0 :
    factorial = factorial * n 
    n = n -1 

print(factorial)

