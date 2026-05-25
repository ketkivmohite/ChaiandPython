
# 4. Fruit Ripeness Checker 
# Probelm : Determine if a fruit is ripe , overripe or unripe on its color 
# (e.g. , Banana : Green - Unripe, Yellow - Ripe , Brown - Overripe)

banana_checker = input("Enter your banana's color (Green , Yellow, Brown): ")

if banana_checker == "Green":
    print("Unripe")
elif banana_checker == "Yellow":
    print("Ripe")
elif banana_checker == "Brown":
    print("Overripe")
else:
    print("Invalid")