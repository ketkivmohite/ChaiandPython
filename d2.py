# ### Day 2 — Numbers & Arithmetic
# > Topics: int, float, arithmetic operators, integer division, modulus

# - [ ] 1. Add two numbers 15 and 27 and print the result.  
#   `💡 print(15 + 27)`
num1 = 15 
num2 = 27
print(num1 + num2)

# - [ ] 2. Find the remainder when 100 is divided by 7.  
#   `💡 Use % operator`
print(100 % 7)

# - [ ] 3. Calculate 2 to the power of 10 using Python.  
#   `💡 Use ** operator`
print(2 ** 10)

# - [ ] 4. Divide 17 by 3 using normal division and floor division. Print both.  
#   `💡 / gives float, // gives int`
print(17 / 3)
print(17 // 3)

# - [ ] 5. Store `price = 250` and `quantity = 4`. Calculate and print total cost.  
#   `💡 total = price * quantity`
price = 250 
quantity = 4 
total = price * quantity
print(total)

# - [ ] 6. Check if 156 is even or odd using the modulus operator.  
#   `💡 156 % 2 == 0 means even`
if 156 % 2 == 0:
    print("Even")
else:
    print("Odd")

# - [ ] 7. Convert 98.6°F to Celsius. Formula: `(F - 32) × 5/9`.  
#   `💡 Store result in a variable`
F = 98.6
print(f"Farheniet to Degree {(F -32)* 5/9}")

# - [ ] 8. Print the result of `(10 + 3) * 2 - 4 / 2`. Then add parentheses to change the answer.  
#   `💡 Operator precedence`
print(f'{(10 + 3) * 2 - 4 / 2}')

