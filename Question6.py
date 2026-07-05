#Happy Pirates
print("Welcome to the PYTHON ISLAND 🏴‍☠️!!!\n\n\n")
user_name=input("Introduce yourself...\n")
print("Warm Welcome", user_name, "on the PYTHON ISLAND 🏴‍☠️")

print(user_name,"what is your Age?\n")
user_age=input('Age:')
print(user_name, "is",user_age, "years old.")

print(user_name,"what is your favorite color?\n")
fav_colour=input('Color:')
print("favorite animal?\n")
fav_animal=input('Animal:')
pirate_name=fav_colour+" "+fav_animal # Swashbuckler way of naming pirates

print(user_name, ", how many coins did you get?\n")
coins=int(input('Coins:'))
print(user_name, "has", coins, "coins")

pirates=int(input("How many pirates are on the crew though?\n"))
share_per_pirate=coins/pirates

if share_per_pirate>=15:
    print("Yeeei!!! We have happy pirates on the crew")
else:
    print( "Awwwch!!! We don't have big coins yet. Yet to have!")