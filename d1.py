### Day 1 — Variables & Basic Output
# > Topics: Storing values, `print()`, `type()`

# - [ ] 1. Store your name in a variable and print it.  
name = "Ketki"
print(name)
#   `💡 name = 'Ketki' then print(name)`

# - [ ] 2. Store your age in a variable and print it.  
#   `💡 age = 20`
age = '20'
print(age)

# - [ ] 3. Print the type of the value 42 using `type()`.  
#   `💡 print(type(42))`
print(type(42))


# - [ ] 4. Create two variables: `city` and `country`. Print both on one line.  
#   `💡 print(city, country)`

city = 'Mumbai'
country = 'India'
print(city,country)

# - [ ] 5. Store the number `3.14` in a variable called `pi`. Print it.  
#   `💡 pi = 3.14`

pi = 3.14
print(pi)

# - [ ] 6. Create a variable `is_student = True` and print it.  
#   `💡 Boolean type`

is_student = True
print(type(is_student))

# - [ ] 7. Print the types of: `'hello'`, `100`, `3.5`, and `True` — one per line.  
#   `💡 Use type() on each`
print(type('hello'))
print(type(100))
print(type(3.5))
print(type(True))

# - [ ] 8. Swap the values of two variables `a = 5` and `b = 10` and print both.  
#   `💡 a, b = b, a`

a = 5 
b = 10 
print(a,b)
a , b = b , a 
print(a,b)


name = "Ketki"
age = 20
city = "Mumbai"
print(f'My name is {name} I am {age} years old. I live in {city}')