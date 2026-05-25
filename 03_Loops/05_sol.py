# 5. Find the First Non - Repeated character
# Problem : Given a string , find the first non - repeated character 

given_str = "mom"


for char in given_str :
    print(char)
    if given_str.count(char) == 1 :
        print("Char is ", char)
