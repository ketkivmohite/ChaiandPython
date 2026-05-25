# 7. Coffee Customization 
# Problem : Customize a coffee order : "Small", "Medium", "Large" with an option for "Extra shot" of espresso
# Coffee Customization

order = "Medium"
extra_shot = True

if extra_shot:
    coffee = order + " coffee with an extra shot"
else:
    coffee = order + " coffee"

print("Order:", coffee)