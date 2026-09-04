# Takes the customer's name as input
customer_name = input("Enter customer name: ")

# Takes names and prices of 3 products as input
product1_name = input("Product 1 name: ")
product1_price = float(input("Price: "))

product2_name = input("Product 2 name: ")
product2_price = float(input("Price: "))

product3_name = input("Product 3 name: ")
product3_price = float(input("Price: "))

# Calculates Subtotal
subtotal = product1_price + product2_price + product3_price

# Determines the discount
if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.00

# Calculates Discount and Final Total
discount = subtotal * discount_rate

# Calculates Final Total
final_total = subtotal - discount

# Displays the shopping summary using a formatted string (f-string)
print("\n* Shopping Summary *")
print(f"\nCustomer Name: {customer_name}")
print(f"Product 1: {product1_name}")
print(f"Price: {product1_price:.0f}")
print(f"Product 2: {product2_name}")
print(f"Price: {product2_price:.0f}")
print(f"Product 3: {product3_name}")
print(f"Price: {product3_price:.0f}")
print(f"Subtotal: {subtotal:.0f}")
print(f"Discount: {discount:.0f}")
print(f"Final Total: {final_total:.0f}")