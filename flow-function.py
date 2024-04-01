def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
    - price: The original price of the item.
    - discount_percent: The discount percentage.
    
    Returns:
    The final price after applying the discount if the discount is 20% or more;
    otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for the original price and the discount percentage
original_price = float(input("50,98 "))
discount_percentage = float(input("20%"))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price
if final_price < original_price:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount was applied. The original price is: {original_price}")
