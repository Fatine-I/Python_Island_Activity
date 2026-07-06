#Count the treasure
print("Welcome to the PYTHON ISLAND 🏴‍☠️!!!\n\n\n")
user_name=input("Introduce yourself...\n")
print("Warm Welcome", user_name, "on the PYTHON ISLAND 🏴‍☠️")

print(user_name,"what is your Age?\n")
user_age=int(input('Age:'))
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

print(user_name, "Hey we have a secret number between 0 and 10 here...\n")
secret_number=7
user_guess=int(input("What do you think is the secret number?\n"))
if user_guess==secret_number:
    print( "Genious! that is the secret number!")
else:
    print("My bad! that's not the secret number.")

print(user_name)
user_word=input(", give a word of your choice:\n")
print("\n\n")
n=0
while n<5:
    print(user_word, "\n")
    n+=1

inventory=["Sword", "Key", "Compass", "Map", "Lantern"]
print("Inventory:")
for item in inventory:
    print(item)

print(user_name, ", this is the total number of items in your inventory: ")
print(len(inventory))
