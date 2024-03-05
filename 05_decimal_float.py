# decimal vs Float in Python

from decimal import Decimal

product_cost = 88.40
commision_rate = 0.08
qty = 450

product_cost += (commision_rate * product_cost)
print(product_cost * qty)


product_cost = Decimal(88.40)
commision_rate = Decimal(0.08)
qty = 450 

product_cost += (commision_rate * product_cost)
print(product_cost * qty)
