#split the treasures
print("Welcome to the PYTHON ISLAND 🏴‍☠️!!!\n\n\n")
user_name=input("Introduce yourself...\n")
print("Warm Welcome", user_name, "on the PYTHON ISLAND 🏴‍☠️")

user_age=input(user_name,"what is your Age?\n")
print(user_name, "is",user_age, "years old.")

fav_colour=input(user_name,", what is your favorite color?\n")
fav_animal=input(user_name, ", what is your favorite animal?\n")
pirate_name=fav_colour+" "+fav_animal # Swashbuckler way of naming pirates

coins=input(user_name, ", how many coins did you get?\n")
print(user_name, "has", coins, "coins")

pirates=input("How many pirates are on the crew though?\n")
share_per_pirate=coins/pirates