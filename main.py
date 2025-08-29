from pyscript import display

# String
restaurant_name = "Seoul Garden"

# String
owner_name = "Navjot Kaur"

# Integer (year)
year_established = 2025

# String
popular_item_price = "₱100"

# Boolean (True/False)
has_delivery = True

# List of Strings
product_names = ["Chestnut Ice Cream", "Makgeolli (Korean Rice Wine) Ice Cream", "Corn Ice Cream"]

# String
business_hours = "9:00 AM to 8:00 PM"

# Dictionary (menu item + price)
menu_prices = { "Chestnut Ice Cream": "₱100", "Makgeolli Ice Cream": "₱120", "Corn Ice Cream": "₱90", "Green Tea Ice Cream": "₱110", "Sweet Potato Ice Cream": "₱130"}

# List of Strings (allergens)
common_allergens = ["Dairy", "Nuts", "Gluten"]

# Float (decimal)
tax_rate = 0.08

# Display 5+ pieces of data
display("<h2>Welcome to " + restaurant_name + "!</h2>")
display("<p><b>Owner:</b> " + owner_name + "</p>")
display("<p><b>Established:</b> " + str(year_established) + "</p>")
display("<p><b>Popular Item Price:</b> " + popular_item_price + "</p>")
display("<p><b>Business Hours:</b> " + business_hours + "</p>")
display("<p><b>Has Delivery?</b> " + str(has_delivery) + "</p>")
display("<p><b>Common Allergens:</b> " + ", ".join(common_allergens) + "</p>")
