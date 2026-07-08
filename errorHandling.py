# revenue = 0
# expense =10

# try:
#     profit = revenue - expense
#     margin = profit*100 / revenue
#     print(margin)
   
# except ZeroDivisionError: 
#     print (f"Revenue is 0 can't calculate margin")
    
## Excercise ##
# Remember the chai bill calculator from lesson 2? Customers (and bugs) don't always behave. Make it bulletproof.
# Write a function safe_chai_bill(cups, price_per_cup) that:
# Converts cups and price_per_cup to numbers using int() / float() (they may arrive as text from a form).
# Uses try/except to catch a ValueError if someone passes "two" instead of 2 and returns the message:
# Please enter numbers only.
# If cups is less than 1, return the message:
# Cups must be at least 1
# Otherwise, return the total bill:
# # cups * price_per_cup
# print(safe_chai_bill("3", "15"))   # normal text input from a form
# print(safe_chai_bill(2, 15))       # normal numbers
# print(safe_chai_bill("two", 15))   # bad input -> caught
# print(safe_chai_bill(0, 15))       # too few cups

def safe_chai_bill(cups, price_per_cup):
    
    try:
        cups = int(cups)
        price_per_cup = float(price_per_cup)
    except ValueError:
        return "Please enter numbers only."
    
    if cups < 1:
       return "Cups must be at least 1"

    return cups*price_per_cup

print(safe_chai_bill("3", "15"))   # normal text input from a form
print(safe_chai_bill(2, 15))       # normal numbers
print(safe_chai_bill("two", 15))   # bad input -> caught
print(safe_chai_bill(0, 15))       # too few cups

    


