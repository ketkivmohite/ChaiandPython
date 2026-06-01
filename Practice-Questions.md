# 🍵 Chai aur Python — 30-Day Beginner Practice Plan

> Based on the **Chai aur Code** Python series by Hitesh Choudhary  
> 8 questions per day · 240 questions total · Difficulty levels up every week

---

## How to use this
- Solve **8 questions every day** — no skipping!
- Each question has a hint. Try without it first.
- Check off questions as you finish using `- [x]`
- By Day 30 you'll have built a complete CLI project from scratch

---

## 📊 Progress Tracker

| Week | Days | Topic Focus | Level |
|------|------|-------------|-------|
| Week 1 | 1–7 | Variables, Numbers, Strings, Input, Mutability, Conditionals | 🟢 Beginner |
| Week 2 | 8–14 | Loops, Lists, Tuples, Dictionaries | 🟢 Beginner |
| Week 3 | 15–21 | Functions, Scope, Closures, OOP Basics | 🔵 Intermediate |
| Week 4 | 22–30 | Problem Sets, Error Handling, Files, Modules, Capstone | 🔴 Advanced |

---

## Week 1 — Foundations

### Day 1 — Variables & Basic Output
> Topics: Storing values, `print()`, `type()`

- [ ] 1. Store your name in a variable and print it.  
  `💡 name = 'Ketki' then print(name)`

- [ ] 2. Store your age in a variable and print it.  
  `💡 age = 20`

- [ ] 3. Print the type of the value 42 using `type()`.  
  `💡 print(type(42))`

- [ ] 4. Create two variables: `city` and `country`. Print both on one line.  
  `💡 print(city, country)`

- [ ] 5. Store the number `3.14` in a variable called `pi`. Print it.  
  `💡 pi = 3.14`

- [ ] 6. Create a variable `is_student = True` and print it.  
  `💡 Boolean type`

- [ ] 7. Print the types of: `'hello'`, `100`, `3.5`, and `True` — one per line.  
  `💡 Use type() on each`

- [ ] 8. Swap the values of two variables `a = 5` and `b = 10` and print both.  
  `💡 a, b = b, a`

---

### Day 2 — Numbers & Arithmetic
> Topics: int, float, arithmetic operators, integer division, modulus

- [ ] 1. Add two numbers 15 and 27 and print the result.  
  `💡 print(15 + 27)`

- [ ] 2. Find the remainder when 100 is divided by 7.  
  `💡 Use % operator`

- [ ] 3. Calculate 2 to the power of 10 using Python.  
  `💡 Use ** operator`

- [ ] 4. Divide 17 by 3 using normal division and floor division. Print both.  
  `💡 / gives float, // gives int`

- [ ] 5. Store `price = 250` and `quantity = 4`. Calculate and print total cost.  
  `💡 total = price * quantity`

- [ ] 6. Check if 156 is even or odd using the modulus operator.  
  `💡 156 % 2 == 0 means even`

- [ ] 7. Convert 98.6°F to Celsius. Formula: `(F - 32) × 5/9`.  
  `💡 Store result in a variable`

- [ ] 8. Print the result of `(10 + 3) * 2 - 4 / 2`. Then add parentheses to change the answer.  
  `💡 Operator precedence`

---

### Day 3 — Strings Basics
> Topics: String creation, indexing, slicing, `len()`

- [ ] 1. Store `'Chai aur Python'` in a variable. Print its length.  
  `💡 Use len()`

- [ ] 2. Print the first character and last character of the string `'Python'`.  
  `💡 s[0] and s[-1]`

- [ ] 3. Slice `'Hello World'` to print only `'World'`.  
  `💡 s[6:]`

- [ ] 4. Print `'Python'` reversed using slicing.  
  `💡 s[::-1]`

- [ ] 5. Concatenate `first_name = 'Hitesh'` and `last_name = 'Choudhary'` with a space between.  
  `💡 first_name + ' ' + last_name`

- [ ] 6. Repeat the string `'chai '` three times and print it.  
  `💡 Use * operator on string`

- [ ] 7. Check if `'code'` is present inside the string `'chai aur code'`.  
  `💡 Use the 'in' keyword`

- [ ] 8. Print every other character from the string `'Programming'`.  
  `💡 Use step in slicing: s[::2]`

---

### Day 4 — String Methods
> Topics: `upper`, `lower`, `strip`, `replace`, `split`, `find`, `count`

- [ ] 1. Convert `'hello world'` to uppercase and `'PYTHON'` to lowercase.  
  `💡 .upper() and .lower()`

- [ ] 2. Remove extra spaces from `'   chai aur code   '` and print.  
  `💡 .strip()`

- [ ] 3. Replace `'bad'` with `'good'` in the string `'This is a bad example'`.  
  `💡 .replace()`

- [ ] 4. Split `'apple,banana,mango,grape'` by comma into a list.  
  `💡 .split(',')`

- [ ] 5. Find the position of `'code'` in `'chai aur code'`.  
  `💡 .find()`

- [ ] 6. Count how many times `'a'` appears in `'banana'`.  
  `💡 .count('a')`

- [ ] 7. Check if the string `'Python3'` starts with `'Python'` and ends with `'3'`.  
  `💡 .startswith() and .endswith()`

- [ ] 8. Join the list `['Chai', 'aur', 'Python']` into a single string with spaces.  
  `💡 ' '.join(list)`

---

### Day 5 — String Formatting & Input
> Topics: f-strings, `input()`, type conversion

- [ ] 1. Ask the user for their name and greet them: `'Hello, [name]!'`  
  `💡 Use input() then print`

- [ ] 2. Ask for two numbers from the user and print their sum.  
  `💡 Convert input to int using int()`

- [ ] 3. Use an f-string to print: `'My name is X and I am Y years old.'`  
  `💡 f'My name is {name}...'`

- [ ] 4. Ask for a temperature in Celsius. Convert to Fahrenheit and print using f-string.  
  `💡 F = C * 9/5 + 32`

- [ ] 5. Ask for a number. Print whether it is positive, negative, or zero.  
  `💡 if / elif / else`

- [ ] 6. Format a float to 2 decimal places using f-string. E.g. `price = 99.9999`.  
  `💡 f'{price:.2f}'`

- [ ] 7. Ask the user for their birth year. Calculate and print their age.  
  `💡 age = 2025 - int(birth_year)`

- [ ] 8. Ask for a string. Print its length, uppercase version, and first character.  
  `💡 Combine input + string methods`

---

### Day 6 — Mutable vs Immutable
> Topics: `id()`, int/str are immutable, list is mutable

- [ ] 1. Assign `a = 5`. Print `id(a)`. Then do `a = a + 1`. Print `id(a)` again. Are they same?  
  `💡 id changes for immutable types`

- [ ] 2. Assign `x = 'hello'`. Try `x[0] = 'H'`. What error do you get? Write it as a comment.  
  `💡 TypeError — strings are immutable`

- [ ] 3. Create a list `nums = [1,2,3]`. Print `id(nums)`. Append 4. Print `id(nums)` again.  
  `💡 id stays the same — lists are mutable`

- [ ] 4. Assign `a = b = [1, 2, 3]`. Append 99 to `a`. Print `b`. Why did `b` change?  
  `💡 Both point to same list in memory`

- [ ] 5. Fix the above problem using `b = a.copy()`. Show that `b` no longer changes.  
  `💡 .copy() creates a new list`

- [ ] 6. Print the type and id of: `100`, `'hello'`, `[1,2]`, `(1,2)`. Observe the pattern.  
  `💡 Use type() and id() together`

- [ ] 7. Reassign a string variable: `s = 'chai'`, then `s = 'code'`. Print `id` both times.  
  `💡 New object created each time`

- [ ] 8. Create two separate lists `[1,2,3]` and `[1,2,3]`. Are their ids same? Why not?  
  `💡 Lists are always new objects`

---

### Day 7 — if / elif / else
> Topics: Conditional statements, comparison operators, logical operators

- [ ] 1. Check if a number is positive, negative, or zero.  
  `💡 if n > 0 / elif n < 0 / else`

- [ ] 2. Ask for a number. Print `'Even'` or `'Odd'`.  
  `💡 n % 2 == 0`

- [ ] 3. Check if a year is a leap year. (Divisible by 4, not 100, unless also 400.)  
  `💡 Nested conditions`

- [ ] 4. Given marks out of 100, print grade: A(90+), B(75+), C(60+), D(45+), F.  
  `💡 Use elif chain`

- [ ] 5. Ask for two numbers. Print which is larger, or `'Equal'` if same.  
  `💡 Use if / elif / else`

- [ ] 6. Check if a person can vote: `age >= 18` and `is_citizen == True`.  
  `💡 Use 'and' logical operator`

- [ ] 7. Ask for a number 1–7. Print the corresponding day name (1=Monday etc.).  
  `💡 Use elif chain or match-case`

- [ ] 8. Check if a triangle is valid: sum of any two sides must be greater than the third.  
  `💡 Three conditions with 'and'`

---

## Week 2 — Collections & Loops

### Day 8 — for Loops
> Topics: `for` loop, `range()`, iterating over strings and lists

- [ ] 1. Print numbers 1 to 10 using a for loop.  
  `💡 for i in range(1, 11)`

- [ ] 2. Print the multiplication table of 7.  
  `💡 for i in range(1, 11): print(7*i)`

- [ ] 3. Print each character of the string `'Python'` on a new line.  
  `💡 for ch in 'Python'`

- [ ] 4. Sum all numbers from 1 to 100 using a for loop.  
  `💡 total += i in the loop`

- [ ] 5. Print all even numbers from 2 to 20.  
  `💡 range(2, 21, 2) or check i%2==0`

- [ ] 6. Count how many vowels are in the string `'chai aur python'`.  
  `💡 Check if ch in 'aeiou'`

- [ ] 7. Print numbers 10 down to 1 (countdown) using a for loop.  
  `💡 range(10, 0, -1)`

- [ ] 8. Print a simple pattern of stars: 5 rows where row `i` has `i` stars.  
  `💡 Nested: for i in range(1,6): print('*'*i)`

---

### Day 9 — while Loops
> Topics: `while` loop, `break`, `continue`

- [ ] 1. Print numbers 1 to 5 using a while loop.  
  `💡 n = 1; while n <= 5`

- [ ] 2. Keep asking user to enter a number until they enter 0. Then stop.  
  `💡 while True + break`

- [ ] 3. Print all numbers 1–20 except multiples of 3 using `continue`.  
  `💡 if n%3==0: continue`

- [ ] 4. Build a simple login: keep asking for password until correct (max 3 attempts).  
  `💡 attempts counter + while loop`

- [ ] 5. Find the first number greater than 100 that is divisible by 13.  
  `💡 while loop starting from 101`

- [ ] 6. Print the digits of 12345 one by one using while loop (no string conversion).  
  `💡 Use % 10 and // 10`

- [ ] 7. Ask user to keep entering words. Stop when they type `'quit'`. Print total words entered.  
  `💡 counter + while True`

- [ ] 8. Print the sum of digits of any number the user enters.  
  `💡 Repeatedly take num%10 and num//10`

---

### Day 10 — Lists Basics
> Topics: Creating lists, indexing, `append`, `remove`, `len`, loops

- [ ] 1. Create a list of 5 fruits. Print the first and last item.  
  `💡 fruits[0] and fruits[-1]`

- [ ] 2. Add `'mango'` to the end of your fruits list.  
  `💡 .append()`

- [ ] 3. Remove `'banana'` from the list. Print the updated list.  
  `💡 .remove()`

- [ ] 4. Print all items in a list using a for loop.  
  `💡 for item in list`

- [ ] 5. Find the length of the list and print the middle element.  
  `💡 Use len() and integer division`

- [ ] 6. Create a list of 5 numbers. Print the largest and smallest.  
  `💡 max() and min()`

- [ ] 7. Ask the user to enter 5 numbers. Store them in a list and print the sum.  
  `💡 Use append() in a loop`

- [ ] 8. Reverse the list `[1, 2, 3, 4, 5]` and print it.  
  `💡 .reverse() or slicing [::-1]`

---

### Day 11 — Lists Intermediate
> Topics: Sorting, slicing, list methods, list comprehension intro

- [ ] 1. Sort the list `[3,1,4,1,5,9,2,6]` in ascending and descending order.  
  `💡 .sort() and .sort(reverse=True)`

- [ ] 2. Slice the list `[10,20,30,40,50,60]` to get only `[20,30,40]`.  
  `💡 list[1:4]`

- [ ] 3. Create a new list of squares of numbers 1–10 using list comprehension.  
  `💡 [x**2 for x in range(1,11)]`

- [ ] 4. Filter only even numbers from `[1,2,3,4,5,6,7,8]` using list comprehension.  
  `💡 [x for x in lst if x%2==0]`

- [ ] 5. Find the index of `'banana'` in `['apple','banana','mango']`.  
  `💡 .index()`

- [ ] 6. Count how many times `5` appears in `[1,5,3,5,7,5,2]`.  
  `💡 .count(5)`

- [ ] 7. Merge two lists `[1,2,3]` and `[4,5,6]` into one without using `+`.  
  `💡 .extend() or list unpacking`

- [ ] 8. Remove duplicates from `[1,2,2,3,3,3,4]` without using `set()`.  
  `💡 Loop and check 'if item not in new_list'`

---

### Day 12 — Tuples
> Topics: Creating tuples, immutability, packing/unpacking, when to use tuples

- [ ] 1. Create a tuple of 5 colours. Print the first and last.  
  `💡 colours = ('red','blue',...)`

- [ ] 2. Try to change the first element of a tuple. Write down the error you get.  
  `💡 TypeError: tuple does not support item assignment`

- [ ] 3. Unpack `(name, age, city) = ('Hitesh', 30, 'Mumbai')` and print each.  
  `💡 Tuple unpacking`

- [ ] 4. Find the length of a tuple and check if `'green'` is in it.  
  `💡 len() and 'in'`

- [ ] 5. Convert a tuple `(1,2,3)` to a list, add 4, then convert back to tuple.  
  `💡 list() and tuple()`

- [ ] 6. Create a tuple of coordinates `(lat, lon) = (19.07, 72.87)`. Print nicely with f-string.  
  `💡 f'Lat: {lat}, Lon: {lon}'`

- [ ] 7. Count how many times `'a'` appears in `('a','b','a','c','a')`.  
  `💡 .count()`

- [ ] 8. Store student info as a tuple `(name, marks, grade)`. Print all fields unpacked.  
  `💡 name, marks, grade = student`

---

### Day 13 — Dictionaries Basics
> Topics: Creating dicts, accessing, adding, updating, deleting keys

- [ ] 1. Create a dictionary with `name`, `age`, and `city`. Print each value.  
  `💡 person['name']`

- [ ] 2. Add a new key `'email'` to the dictionary.  
  `💡 person['email'] = '...'`

- [ ] 3. Update the age to 25 in the dictionary.  
  `💡 person['age'] = 25`

- [ ] 4. Delete the `'city'` key from the dictionary.  
  `💡 del person['city']`

- [ ] 5. Check if key `'name'` exists in the dictionary.  
  `💡 'name' in person`

- [ ] 6. Print all keys, then all values, then all key-value pairs.  
  `💡 .keys(), .values(), .items()`

- [ ] 7. Use `.get()` to access a key that doesn't exist — without getting an error.  
  `💡 .get('phone', 'Not found')`

- [ ] 8. Loop through the dictionary and print: `'key → value'` for each pair.  
  `💡 for k, v in person.items()`

---

### Day 14 — Dictionaries Intermediate
> Topics: Nested dicts, dict comprehension, practical use

- [ ] 1. Create a nested dict: a student with `name`, `marks = {maths:90, science:85}`. Print maths marks.  
  `💡 student['marks']['maths']`

- [ ] 2. Create a word frequency counter for the sentence `'chai aur chai aur python'`.  
  `💡 Loop + dict.get(word, 0) + 1`

- [ ] 3. Use dict comprehension to create `{1:1, 2:4, 3:9, 4:16, 5:25}`.  
  `💡 {x: x**2 for x in range(1,6)}`

- [ ] 4. Given a list of names, create a dict mapping each name to its length.  
  `💡 {name: len(name) for name in names}`

- [ ] 5. Merge two dictionaries `d1 = {'a':1}` and `d2 = {'b':2}` into one.  
  `💡 d1.update(d2) or {**d1, **d2}`

- [ ] 6. Sort a dictionary by its values and print. `scores = {'Ali':88, 'Bob':73, 'Ria':95}`.  
  `💡 sorted(d.items(), key=lambda x: x[1])`

- [ ] 7. Create a phone book. Allow user to add 3 contacts then search by name.  
  `💡 Dict + input() + .get()`

- [ ] 8. Count how many students scored above 80 in `{'A':92,'B':74,'C':85,'D':61,'E':90}`.  
  `💡 Loop through .values()`

---

## Week 3 — Functions, Scope & OOP

### Day 15 — Functions Basics
> Topics: `def`, parameters, `return`, calling functions

- [ ] 1. Write a function `greet(name)` that prints `'Hello, [name]!'`  
  `💡 def greet(name): print(...)`

- [ ] 2. Write a function `add(a, b)` that returns the sum of two numbers.  
  `💡 return a + b`

- [ ] 3. Write a function `is_even(n)` that returns `True` if n is even, `False` otherwise.  
  `💡 return n % 2 == 0`

- [ ] 4. Write a function that takes a list and returns the largest number.  
  `💡 Use max() or a loop`

- [ ] 5. Write a function `celsius_to_fahrenheit(c)` and call it with 3 different values.  
  `💡 return c * 9/5 + 32`

- [ ] 6. Write a function that takes a string and returns it reversed.  
  `💡 return s[::-1]`

- [ ] 7. Write a function `count_vowels(s)` that returns the count of vowels.  
  `💡 Loop + check 'if ch in aeiou'`

- [ ] 8. Write a function `greet_all(names)` that takes a list and greets each person.  
  `💡 Loop inside the function`

---

### Day 16 — Functions Intermediate
> Topics: Default args, `*args`, `**kwargs`, return multiple values

- [ ] 1. Write `greet(name, greeting='Hello')` with a default argument. Call both ways.  
  `💡 greet('Hitesh') and greet('Hitesh','Namaste')`

- [ ] 2. Write a function `add(*args)` that accepts any number of numbers and returns their sum.  
  `💡 for n in args: total += n`

- [ ] 3. Write `print_info(**kwargs)` that prints each key-value pair passed to it.  
  `💡 for k,v in kwargs.items()`

- [ ] 4. Write a function that returns both the minimum and maximum of a list.  
  `💡 return min(lst), max(lst)`

- [ ] 5. Write a function `multiply(a, b=2)`. Call it with one arg and with two args.  
  `💡 Default parameter`

- [ ] 6. Write a function that accepts `*args` and prints how many arguments were passed.  
  `💡 len(args)`

- [ ] 7. Write a function `profile(**kwargs)` that builds and returns a dict from keyword args.  
  `💡 return kwargs`

- [ ] 8. Write a calculator function `calc(a, b, op='+')` that handles `+,-,*,/` using the `op` parameter.  
  `💡 if op == '+': return a+b ...`

---

### Day 17 — Scope & Closures
> Topics: Local, global, nonlocal, closures

- [ ] 1. Create a global variable `count=0`. Write a function that tries to print it (no modification).  
  `💡 Just reading global works fine`

- [ ] 2. Try incrementing a global variable inside a function without `'global'`. What happens?  
  `💡 UnboundLocalError`

- [ ] 3. Fix the above using the `global` keyword.  
  `💡 global count; count += 1`

- [ ] 4. Write a nested function. Show that the inner function can read the outer function's variable.  
  `💡 Enclosing scope`

- [ ] 5. Write `make_adder(n)` that returns a function which adds `n` to its input.  
  `💡 def adder(x): return x + n; return adder`

- [ ] 6. Create two adders: `add5 = make_adder(5)` and `add10 = make_adder(10)`. Test both.  
  `💡 Each closure remembers its own n`

- [ ] 7. Write `make_counter()` that returns a function. Each call increments and returns a count.  
  `💡 Use nonlocal count`

- [ ] 8. Show that two counters from `make_counter()` are independent (different state).  
  `💡 c1 = make_counter(); c2 = make_counter()`

---

### Day 18 — OOP: Classes & Objects
> Topics: `__init__`, `self`, instance variables, methods

- [ ] 1. Create a `Dog` class with `name` and `breed`. Create 2 dog objects and print their details.  
  `💡 class Dog: def __init__(self, name, breed)`

- [ ] 2. Add a method `bark()` to `Dog` that prints `'[name] says: Woof!'`  
  `💡 def bark(self): print(...)`

- [ ] 3. Create a `Rectangle` class with `width` and `height`. Add an `area()` method.  
  `💡 return self.width * self.height`

- [ ] 4. Add a `perimeter()` method to `Rectangle`.  
  `💡 return 2*(self.width + self.height)`

- [ ] 5. Create a `BankAccount` class with `balance`. Add `deposit()` and `withdraw()` methods.  
  `💡 self.balance += amount`

- [ ] 6. Add a check in `withdraw()` that prints `'Insufficient funds'` if balance is too low.  
  `💡 if amount > self.balance`

- [ ] 7. Add `__str__` to `BankAccount` so `print(account)` shows `'Balance: ₹[amount]'`.  
  `💡 def __str__(self): return ...`

- [ ] 8. Create 3 `BankAccount` objects with different balances. Print all using a loop.  
  `💡 Store in a list, loop with print()`

---

### Day 19 — OOP: Inheritance
> Topics: Inheritance, `super()`, method overriding

- [ ] 1. Create `Animal` class with `name` and a `speak()` method that prints `'Some sound'`.  
  `💡 Base class`

- [ ] 2. Create `Dog` and `Cat` classes that inherit from `Animal`. Override `speak()`.  
  `💡 class Dog(Animal): def speak()...`

- [ ] 3. Use `super().__init__()` in `Dog` to call `Animal`'s constructor.  
  `💡 super().__init__(name)`

- [ ] 4. Create a list of mixed `Animal` objects. Loop and call `speak()` on each.  
  `💡 Polymorphism in action`

- [ ] 5. Add a class variable `species` to `Animal`. Access it from `Dog`.  
  `💡 Animal.species or self.species`

- [ ] 6. Create `Student(Person)` where `Person` has `name` and `age`. `Student` adds `student_id`.  
  `💡 Use super().__init__()`

- [ ] 7. Override `__str__` in `Student` to print all three fields.  
  `💡 def __str__(self): return f'...'`

- [ ] 8. Check if a dog object is an instance of both `Dog` and `Animal`.  
  `💡 isinstance(dog, Animal)`

---

### Day 20 — Decorators
> Topics: What decorators are, `@decorator` syntax, writing your own

- [ ] 1. Write a function `say_hello()` and assign it to a variable. Call it via the variable.  
  `💡 Functions are objects: greet = say_hello`

- [ ] 2. Write a function that takes another function as argument and calls it.  
  `💡 def runner(func): func()`

- [ ] 3. Write a function that returns another function (a factory).  
  `💡 def outer(): def inner(): ... return inner`

- [ ] 4. Write a decorator `my_logger(func)` that prints `'Calling [func name]'` before calling func.  
  `💡 def wrapper(): print(...); func(); return wrapper`

- [ ] 5. Apply `my_logger` to a function using `@my_logger` syntax.  
  `💡 @my_logger above the function def`

- [ ] 6. Write a decorator `uppercase_result` that converts a function's string return to uppercase.  
  `💡 return wrapper() where wrapper returns func().upper()`

- [ ] 7. Write a `timer` decorator that prints how long a function took to run.  
  `💡 import time; start = time.time()`

- [ ] 8. Apply the `timer` decorator to a function that counts to 1,000,000 in a loop.  
  `💡 @timer above the function`

---

### Day 21 — Mixed Practice (Week 3 Review)
> Topics: Functions + OOP + Decorators combined

- [ ] 1. Write a function that uses `*args` to accept student names and returns them sorted.  
  `💡 return sorted(args)`

- [ ] 2. Build a `Counter` using closures (no `class` keyword) — `make_counter(start=0)`.  
  `💡 nonlocal + closure`

- [ ] 3. Create a `Shape` base class. `Rectangle` and `Circle` inherit it. Both have `area()`.  
  `💡 Polymorphism practice`

- [ ] 4. Write a decorator `@validate_positive` that raises `ValueError` if any arg is negative.  
  `💡 Check args inside wrapper`

- [ ] 5. Write a `Student` class with a `classmethod` `from_string('Name,Age,Grade')`.  
  `💡 Split the string inside classmethod`

- [ ] 6. Add a `@staticmethod validate_grade(g)` to `Student` that checks if grade is A–F.  
  `💡 return g in 'ABCDF'`

- [ ] 7. Write a function that takes a list of dicts and returns sorted by a given key.  
  `💡 sorted(lst, key=lambda x: x[key])`

- [ ] 8. Combine: write an OOP-based todo list with `add()`, `complete()`, and `list()` methods.  
  `💡 Use a list of dicts internally`

---

## Week 4 — Problem Sets & Capstone

### Day 22 — Conditionals Problem Set
> Topics: 10 conditional problems from the video — solved step by step

- [ ] 1. Write a program to check if a number is positive, negative, or zero.  
  `💡 3 branches with if/elif/else`

- [ ] 2. Find the largest among three numbers entered by the user.  
  `💡 Nested if or chained elif`

- [ ] 3. Check if a character entered is a vowel or consonant.  
  `💡 if ch.lower() in 'aeiou'`

- [ ] 4. A cinema charges: children(<12) ₹100, adults ₹200, seniors(>60) ₹150. Calculate ticket price.  
  `💡 elif chain on age`

- [ ] 5. Ask for a number. Print `'Fizz'` if divisible by 3, `'Buzz'` by 5, `'FizzBuzz'` by both.  
  `💡 Check both first: if n%3==0 and n%5==0`

- [ ] 6. Check if a number is divisible by both 4 and 6 but not 12.  
  `💡 n%4==0 and n%6==0 and n%12!=0`

- [ ] 7. Given a month number (1–12), print how many days it has (ignore leap year).  
  `💡 Use elif or a days dict`

- [ ] 8. A shop gives discount: >₹2000 gets 20%, >₹1000 gets 10%, else 5%. Print final price.  
  `💡 elif chain on amount`

---

### Day 23 — Loops Problem Set
> Topics: 10 loop problems from the video — solved step by step

- [ ] 1. Print all prime numbers between 1 and 50.  
  `💡 Nested loop: for each n check divisibility`

- [ ] 2. Print the Fibonacci series up to 10 terms.  
  `💡 a,b = 0,1 then a,b = b, a+b in loop`

- [ ] 3. Find the factorial of a number using a for loop.  
  `💡 result *= i in range(1, n+1)`

- [ ] 4. Reverse a number without converting to string (e.g. 1234 → 4321).  
  `💡 % 10 and // 10 in while loop`

- [ ] 5. Print this pattern: 1 / 1 2 / 1 2 3 / 1 2 3 4  
  `💡 Nested loops`

- [ ] 6. Find the sum of all numbers between 1–100 divisible by 3 or 5.  
  `💡 if n%3==0 or n%5==0: total+=n`

- [ ] 7. Count how many 3-digit numbers are palindromes (e.g. 121, 252).  
  `💡 str(n) == str(n)[::-1]`

- [ ] 8. Print a number guessing game: random secret number, user keeps guessing.  
  `💡 import random; while guess != secret`

---

### Day 24 — Functions Problem Set
> Topics: 10 function problems from the video — solved step by step

- [ ] 1. Write `is_palindrome(s)` — returns `True` if string reads same forwards and backwards.  
  `💡 return s == s[::-1]`

- [ ] 2. Write `flatten(nested_list)` that converts `[[1,2],[3,4]]` to `[1,2,3,4]`.  
  `💡 for sublist in lst: for item in sublist`

- [ ] 3. Write `gcd(a, b)` using Euclid's algorithm.  
  `💡 while b: a,b = b, a%b; return a`

- [ ] 4. Write a function that returns all factors of a number.  
  `💡 if n%i==0: factors.append(i)`

- [ ] 5. Write `power(base, exp)` recursively without using `**`.  
  `💡 return base * power(base, exp-1)`

- [ ] 6. Write a function that takes a sentence and returns the longest word.  
  `💡 words = s.split(); use max(key=len)`

- [ ] 7. Write `remove_duplicates(lst)` that preserves original order.  
  `💡 seen = []; if x not in seen: seen.append(x)`

- [ ] 8. Write a function that checks if two strings are anagrams of each other.  
  `💡 sorted(s1) == sorted(s2)`

---

### Day 25 — Error Handling
> Topics: `try`, `except`, `else`, `finally`, raising exceptions

- [ ] 1. Ask user for a number. Handle `ValueError` if they type letters instead.  
  `💡 try: int(input()) except ValueError`

- [ ] 2. Try dividing by zero and catch the `ZeroDivisionError`.  
  `💡 except ZeroDivisionError: print('Cannot divide')`

- [ ] 3. Access index 10 of a list with only 3 elements. Catch `IndexError`.  
  `💡 except IndexError`

- [ ] 4. Use the `else` block — it runs only when no exception occurred.  
  `💡 try/except/else: print('Success')`

- [ ] 5. Use `finally` to print `'Done'` whether exception happened or not.  
  `💡 finally block always runs`

- [ ] 6. Write a `safe_divide(a, b)` function that handles division by zero gracefully.  
  `💡 return None or a message`

- [ ] 7. Raise a `ValueError` yourself if someone passes a negative number to a function.  
  `💡 if n < 0: raise ValueError('...')`

- [ ] 8. Write a function that keeps asking for valid integer input until user provides one.  
  `💡 while True: try/except/break`

---

### Day 26 — File Handling
> Topics: Reading and writing files, `with open()`

- [ ] 1. Write `'Hello from Python!'` to a file called `hello.txt`.  
  `💡 open('hello.txt','w') + write()`

- [ ] 2. Read `hello.txt` and print its contents.  
  `💡 open('hello.txt','r') + read()`

- [ ] 3. Append a new line to `hello.txt` without overwriting.  
  `💡 open('hello.txt','a')`

- [ ] 4. Write 5 names (one per line) to a file using `writelines()`.  
  `💡 writelines([name+'\n' for name in names])`

- [ ] 5. Read the file back line by line and print each line stripped of whitespace.  
  `💡 for line in f: print(line.strip())`

- [ ] 6. Count how many lines are in the file.  
  `💡 len(f.readlines())`

- [ ] 7. Use `'with open(...)'` to safely open and write a file (handles closing automatically).  
  `💡 with open('file.txt','w') as f:`

- [ ] 8. Write a program that saves a user's to-do list to a file and reads it back.  
  `💡 Combine input loop + file write`

---

### Day 27 — Modules & Imports
> Topics: `import`, `from...import`, `random`, `math`, `datetime`

- [ ] 1. Use the `math` module to print: `pi`, `sqrt(144)`, `ceil(4.3)`, `floor(4.9)`.  
  `💡 import math; math.pi, math.sqrt()`

- [ ] 2. Use `random.randint()` to simulate a dice roll (1–6). Roll 5 times.  
  `💡 import random; random.randint(1,6)`

- [ ] 3. Use `random.choice()` to pick a random item from a list of fruits.  
  `💡 random.choice(fruits)`

- [ ] 4. Use `random.shuffle()` to shuffle a deck (list of numbers 1–10).  
  `💡 random.shuffle(deck)`

- [ ] 5. Print today's date using the `datetime` module.  
  `💡 from datetime import date; date.today()`

- [ ] 6. Calculate how many days until 31 Dec 2025 from today.  
  `💡 datetime.date(2025,12,31) - date.today()`

- [ ] 7. Use the `os` module to print your current working directory.  
  `💡 import os; os.getcwd()`

- [ ] 8. Write your own module `myutils.py` with 2 functions. Import and use them.  
  `💡 from myutils import func1, func2`

---

### Day 28 — List Comprehensions & Lambdas
> Topics: List comprehensions, `map`, `filter`, `lambda`, `sorted` with key

- [ ] 1. Use list comprehension to create a list of cubes of numbers 1–10.  
  `💡 [x**3 for x in range(1,11)]`

- [ ] 2. Filter words longer than 4 characters from a list using list comprehension.  
  `💡 [w for w in words if len(w)>4]`

- [ ] 3. Write a lambda that squares a number. Assign to a variable and call it.  
  `💡 square = lambda x: x**2`

- [ ] 4. Use `map()` with a lambda to double every number in `[1,2,3,4,5]`.  
  `💡 list(map(lambda x: x*2, nums))`

- [ ] 5. Use `filter()` to keep only odd numbers from `[1,2,3,4,5,6,7,8]`.  
  `💡 list(filter(lambda x: x%2!=0, nums))`

- [ ] 6. Sort a list of tuples `[(name, score)]` by score using `sorted()` + lambda.  
  `💡 sorted(lst, key=lambda x: x[1])`

- [ ] 7. Use a dict comprehension to swap keys and values in `{'a':1,'b':2,'c':3}`.  
  `💡 {v:k for k,v in d.items()}`

- [ ] 8. Combine `map` and `filter`: from 1–20, get squares of only even numbers.  
  `💡 list(map(lambda x:x**2, filter(lambda x:x%2==0, range(1,21))))`

---

### Day 29 — OOP Deeper Practice
> Topics: Properties, class methods, dunder methods

- [ ] 1. Add `__repr__` to your `BankAccount` class. It should show class name + balance.  
  `💡 return f'BankAccount(balance={self.balance})'`

- [ ] 2. Add `__eq__` to compare two `BankAccounts` by balance.  
  `💡 return self.balance == other.balance`

- [ ] 3. Add `__lt__` so you can sort a list of `BankAccount` objects by balance.  
  `💡 return self.balance < other.balance`

- [ ] 4. Build a `Temperature` class using `@property` for `celsius` and `fahrenheit`.  
  `💡 @property def fahrenheit(self): return self._celsius*9/5+32`

- [ ] 5. Add a `@fahrenheit.setter` that converts back to Celsius when set.  
  `💡 self._celsius = (value-32)*5/9`

- [ ] 6. Add a `classmethod` `Person.from_string('Name-Age')` as alternate constructor.  
  `💡 name, age = s.split('-'); return cls(name, int(age))`

- [ ] 7. Add a `staticmethod` to validate that age is between 0 and 120.  
  `💡 return 0 <= age <= 120`

- [ ] 8. Write `__len__` for a custom `Bag` class — returns count of items inside.  
  `💡 return len(self.items)`

---

### Day 30 — Capstone Project 🎉
> Build a complete CLI Task Manager using everything you've learned

- [ ] 1. Create a `Task` class with `title`, `priority` (high/medium/low), and `done=False`.  
  `💡 OOP foundation`

- [ ] 2. Add `__str__` to `Task`: `'[DONE] Buy groceries (high)'` or `'[ ] Buy groceries (high)'`.  
  `💡 Use self.done to pick DONE or space`

- [ ] 3. Create a `TaskManager` class that stores tasks in a list.  
  `💡 self.tasks = []`

- [ ] 4. Add `add_task(title, priority)` and `complete_task(title)` methods to `TaskManager`.  
  `💡 Loop to find task by title`

- [ ] 5. Add `filter_by_priority(priority)` that returns only matching tasks.  
  `💡 List comprehension`

- [ ] 6. Add a decorator `@log_action` to print the method name every time it's called.  
  `💡 def wrapper(*args, **kwargs): print(func.__name__)`

- [ ] 7. Save all tasks to `tasks.json` on exit. Load them on startup.  
  `💡 import json; json.dump / json.load`

- [ ] 8. Build a CLI menu loop: 1-Add, 2-Complete, 3-List, 4-Filter by priority, 5-Exit.  
  `💡 while True + input() + if/elif`

---

## 🎯 You made it!

If you solved all 240 questions, you now have solid Python fundamentals.  
Your next steps:
- Push your Day 30 capstone project to GitHub
- Try solving problems on [HackerRank](https://www.hackerrank.com/domains/python) or [LeetCode Easy](https://leetcode.com/problemset/)
- Build something real — a FastAPI backend, a script that automates something you do daily

---

*Based on Chai aur Code Python series by Hitesh Choudhary*  
*Happy coding! 🍵*