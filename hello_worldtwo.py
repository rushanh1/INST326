#print("hello number two")
#plant_count = 6              # int
#spacing_in = 10.5            # float
#plant_name = "Basil"         # str
#is_outdoor = True            # bool

#print(type(plant_count), type(spacing_in), type(plant_name), type(is_outdoor))

# Conversions
#plants_str = str(plant_count)  # '6'
#height_ft = float(11) / 12     # convert inches to feet -> 0.9166...
#count_from_str = int("42")     # 42
#print(plants_str, height_ft, count_from_str)

first = "Ovtavia"
last = "Butler"
author_full = "Ovtavia Butler"

print(first + " " + last)

edition_text = "2" 
edition_num = 2
same = int(edition_text) == edition_num 

print (same)

copies = 3
copies = copies + 2
copies = copies - 1 

print(f"Final copies: {copies}")

copies = 3

for i in range(2):   # repeat 2 times
    copies = copies + 4   # returned copy
    copies = copies - 1   # lost copy
    print(f"Round {i+1} → Final copies: {copies}")


age = int(input("Enter your age: "))
print(f"You are currently {age} years old!")

year = int(input("What is the publication year? "))
modern = (year >= 2000)

print(modern)

title = "The Coluor of Magic"
coluor = "color"

print(title)

year_public = int(input("Enter the publication year: "))
modern = (year_public >= 2000)
print(f"Is the book modern? {'Yes' if modern else 'No' }")

title = "The Color of Magic"
new_title = title.replace("Color", "Colour")

print(new_title)
hold_ready = True 
print(f"{hold_ready} - status recorded")

# Your code here
title = "The Left Hand of Darkness"
keyword = "Hand"
present = title.find(keyword) != -1

print(present)

# Your code here
call_no = "QA.76.P98"
last_dot = call_no.rfind(".")

cutter = call_no[last_dot+1:]

# Your code here
int = int(input("Enter a rating thats 0-5: "))
valid = (int >= 0) and (int <= 5)

print(valid)
title = "Where The Wild Things Are"
author = "Jimmy Neutron"
year = "1970"

print(f"{title} - {author} ({year})")
avg_rating = 4.2667

print(f"{avg_rating:.2}")

via = (input("What is your search term? "))
normalized_via = via.strip().lower()

print(normalized_via)