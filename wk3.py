def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or more
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # No discount applied
        return price

# Example usage
#print(calculate_discount(100, 25))  # 75.0 (discount applied)
#print(calculate_discount(100, 10))  # 100 (no discount)


# Prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display final price
final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"Discount applied! Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Price: ${final_price:.2f}")
