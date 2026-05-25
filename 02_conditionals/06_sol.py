# 6. Transportation mode selection 
# Problem : Choose a mode of transportation based on the distance 
# (e.g. <3 km: Walk ,3-15 km : Bike, >15 km : Car)

distance = int(input("Enter your distance in km : "))
if distance < 3 :
    print("Walk")
elif 3 <= distance <= 15 :
    print("Bike")
elif distance >= 15 :
    print("Car")
else:
    print("Enter a valid distance")
