# Calculate Discount Program

![pexels-goumbik-574073](https://github.com/user-attachments/assets/337072ae-0799-4de8-afb4-0b1c61911667)

## 📌 Overview
This Python program calculates the final price of an item after applying a discount.  
If the discount is **20% or higher**, the discount is applied.  
Otherwise, the original price is returned.

## 🛠 Features
- Takes **original price** and **discount percentage** as input from the user.
- Applies the discount only if it's **≥ 20%**.
- Displays the final price with two decimal places.
- Prevents unnecessary discounts when the percentage is too small.

## 📄 How It Works
1. The user enters the original price of the item.
2. The user enters the discount percentage.
3. The program:
   - If discount ≥ 20%, calculates:  
     ```
     final_price = price - (price * discount_percent / 100)
     ```
   - Else, returns the original price.

## 💻 Example Usage
```bash
Enter the original price: 100
Enter the discount percentage: 25
Discount applied! Final price: $75.00
