#print("Hello World")
#print("Come up with a schedule")

# Your code here
#title = "Where The Wild Things Are"
#author = "Maurice Sendak"
#year_published = 1963
#isbn = "9780060254926"

#print(f"{title} ({year_published}) by {author} — ISBN: {isbn}")
#Total_Copies = 89
#print(f"Total copies after delivery: {Total_Copies}")
"""
tree = input("Enter a book title: ")
cleaned_tree = tree.strip()

print(f'"{cleaned_tree}"')

days_late = int(input("How many days late?"))

negative_days = max(days_late, 0)

fee = negative_days * 0.25
print(f"Late fee: ${fee:.2f}")

# Your code here
title = "Where The Wild Things Are"
author = "Rushan Heaven"

print(f"Title: {title:3}   Author: {author:20}")

price = 12.50
discount = 2.00

final_price = price - discount
print(f"Final price: ${final_price:2f}")

home_branch = " umd "
normalized = home_branch.strip().upper()
print(normalized)
"""
frost_date_passed = False
soil_temp = 55
plant_type = "lettuce"


if plant_type == "tomato" and not frost_date_passed:
    print("Too early to plant tomatos - risk of frost!")
elif plant_type == "lettuce" and soil_temp > 48:
    print("perfect time for lettuce planting")
else:
    print("Check you planting calandar")

titles = ["Python 101", "Data Wrangling", "AI Basics", "Networks", "UX Design"]
available = [True, True, False, True, False]
print(f"The {plant_type} is {frost_date_passed}")