# Discount Calculator

#A simple Python script that calculates the final price after applying a discount.

#Applies discount only if it's 20% or more

#Prompts user for price and discount

#Returns the final price




def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Getthe users inout 
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    print(f"\nFinal price after discount: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values.")
