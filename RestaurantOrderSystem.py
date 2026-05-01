#Restaurant Order System

delivery_price = 5.00

restaurant_name = "--- Food Palace ---\n"
customer_name = "Peter\n"
is_delivery = True

#Products
product1_name = "Pizza Peperoni"
product1_price = 7.20
product1_quantity = 2

product2_name = "Pasta"
product2_price = 3.25
product2_quantity = 3

product3_name = "Salad"
product3_price = 4.20
product3_quantity = 1

product4_name = "Cola"
product4_price = 1.20
product4_quantity = 3

#Calculations
total1 = product1_quantity * product1_price
total2 = product2_quantity * product2_price
total3 = product3_quantity * product3_price
total4 = product4_quantity * product4_price
grand_total = total1 + total2 + total3 + total4 + delivery_price

#Print
print(restaurant_name)
print(f"Customer: {customer_name}")

print(f"{product1_name} {product1_quantity}X = {total1:.2f} €")
print(f"{product2_name} {product2_quantity}X = {total2:.2f} €")
print(f"{product3_name} {product3_quantity}X = {total3:.2f} €")
print(f"{product4_name} {product4_quantity}X = {total4:.2f} €\n")

print(f"Is delivery?: {is_delivery}")
print(f"Delivery: {delivery_price:.2f} €\n")

print("-------------------------------")
print(f"Grand Total: {grand_total:.2f} €")

#Overall - 6.00