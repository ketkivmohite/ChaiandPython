# ### Day 3 — Strings Basics
# > Topics: String creation, indexing, slicing, `len()`

# - [ ] 1. Store `'Chai aur Python'` in a variable. Print its length.  
#   `💡 Use len()`
check_length = 'Chai aur Python'
print(len(check_length))

# - [ ] 2. Print the first character and last character of the string `'Python'`.  
#   `💡 s[0] and s[-1]`
str = 'Python'
print(str[0])
print(str[-1])

# - [ ] 3. Slice `'Hello World'` to print only `'World'`.  
#   `💡 s[6:]`
Start = 'Hello World'
print(Start[6:])

# - [ ] 4. Print `'Python'` reversed using slicing.  
#   `💡 s[::-1]`
print(str[::-1])

# - [ ] 5. Concatenate `first_name = 'Hitesh'` and `last_name = 'Choudhary'` with a space between.  
#   `💡 first_name + ' ' + last_name`
first_name = 'Hitesh'
last_name = 'Choudhary'
print(first_name + " " + last_name)

# - [ ] 6. Repeat the string `'chai '` three times and print it.  
#   `💡 Use * operator on string`
str = 'Chai'
print(str * 3)

# - [ ] 7. Check if `'code'` is present inside the string `'chai aur code'`.  
#   `💡 Use the 'in' keyword`
str = 'chai aur code'
if 'code' in str :
    print("Code is there ")

# - [ ] 8. Print every other character from the string `'Programming'`.  
#   `💡 Use step in slicing: s[::2]`
str = 'Programming'
print(str[::2])

