# 5. Weather Activity Suggestion 
# Problem : Suggest an activity based on the weather 
# (e.g. Sunny - Go for a walk , Rainy - Read a book , Snowy- Build a snowman )

choose_weather = input("Enter the weather nearby you (Sunny , Rainy , Snowy) : ")

if choose_weather == "Sunny":
    print("Go for a walk")
elif choose_weather == "Rainy":
    print("Read a book")
elif choose_weather == "Snowy":
    print("Build a snowman")
else:
    print("Enter a valid weather")