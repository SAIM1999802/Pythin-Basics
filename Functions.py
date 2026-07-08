## how to define a function 
# def cal_mar(revenue, expenses):
#     profit = revenue - expenses
#     margin = (profit*100)/revenue
#     return margin

# print(cal_mar(50 , 20))

## Return profit and margin
# def cal_pro_mar(revenue, expenses):
#     profit = revenue - expenses
#     margin = (profit*100)/revenue
#     return profit , margin 

# revenue = 50
# expense = 20
# profit , margin = cal_pro_mar(revenue, expense)
# print(profit)
# print(margin)



## Exercise: The Chai Bill Calculator

# You run a chai stall. Customers order multiple cups of chai, sometimes with add-ons (extra ginger, masala, biscuits). 
# Write a function to calculate their bill. Your task: Write a function chai_bill(cups, *addons, discount) that:
# Charges 15 per cup of chai.
# Adds 5 for each addon passed via *args (like "ginger", "masala", "biscuit").
# Applies a discount only if discount_percent is passed via kwargs.
# Returns the final bill amount.
# Test it with these calls:
# print(chai_bill(2))
# print(chai_bill(3, "ginger", "masala"))
# print(chai_bill(4, "biscuit", discount_percent=10))
# print(chai_bill(5, "ginger", "masala", "biscuit", discount_percent=20))
# Expected output:
# 30
# 55
# 58.5
# 112.0

def chai_bill(cups,*addons,**discount):
    
    total = cups*15
    extra = len(addons)*5
    total = total + extra
    if 'discount_per' in discount:
        percentage = discount['discount_per']
        total = total-(total*percentage / 100)
    return total

print(chai_bill(2))                                         # Expected: 30
print(chai_bill(3, "ginger", "masala"))                     # Expected: 55
print(chai_bill(4, "biscuit", discount_per=10))         # Expected: 58.5
print(chai_bill(5, "ginger", "masala", "biscuit", discount_per=20)) # Expected: 112.0