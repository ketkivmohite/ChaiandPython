# 3. Grade Calculator 
# Problem : Assign a letter based on a students score : 
# A(90-100), B(80-90), C(70-79),D(60-69),F(Below 60).

score = int(input("Enter your marks: "))

if score >= 101:
    print("Please verify your score again")
    exit()
    
if 90 <= score <= 100 :
    print("A")
elif 80 <= score <= 99 :
    print("B")
elif 70 <= score <= 79 :
    print("C")
elif 60 <= score <= 69 :
    print("D")
else :
    print("F")
