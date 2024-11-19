'''
author name:ANNU JAMES
DATE:19/11/24
'''
inventory = [
    ('laptop', 5, 30, ),
    ('headphone', 15, 1000),
    ('mouse', 12, 500),
    ('keyboard',15,450),
    ("monitor",10,1200)
]
highest_total_value=0
item_with_highest_total_value="none"
for item in inventory:
    item_name,quantity,unit_price=item
    total_value=quantity*unit_price
    print(f"item_name:{item_name},the total value is:{total_value}")
    if total_value>highest_total_value:
        highest_total_value =total_value
        item_with_highest_total_value =item_name
print(f"Highest total value is:{highest_total_value}")
print(f"item with highest total values is:{item_with_highest_total_value}")



