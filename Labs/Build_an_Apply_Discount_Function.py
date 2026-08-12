# In this lab I'll write a function that calculates the final price of an item after applying a percentage discount.

def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"

    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return final_price

price = input("Enter the price: ")
discount = input("Enter the discount (%): ")

final_price = apply_discount(price, discount)

print("The final price is:", final_price)
