# Mortgage Calculator

This Python program is an educational project of a mortgage calculator that can compute key financial metrics for a loan or mortgage. it's part of Codecademy Computer Science course, and it's by no mean something that can be used for real use cases. Any suggestion for improvement or fix would be highly appreciated. 

It supports the following calculations:

1. **Monthly Repayment**: Calculate the monthly repayment amount for a loan.
2. **Loan Amount**: Determine the loan amount based on repayment, interest, and duration.
3. **Loan Duration**: Estimate the duration of the loan given repayment, interest, and amount.
4. **Interest Rate**: Approximate the interest rate for a loan based on repayment, amount, and duration.

## Features

- Handles key mortgage calculations with precision.
- Simple text-based menu interface for user interaction.
- Validates input to ensure correct calculations.

## Prerequisites

- Python 3.x
- Basic understanding of loans and mortgages.

## Usage

1. Clone the repository or copy the code to your local system.
2. Run the program:
   ```bash
   python mortgage_calculator.py
3. Follow the menu prompts to choose a calculation:
        ```1: Calculate monthly repayment
        2: Calculate loan amount
        3: Calculate loan duration
        4: Calculate interest rate
        Q: Quit the program```

Example
Option 1: Calculate Monthly Repayment

Enter the loan amount: 300000
Enter the interest rate: 5.5
Enter the duration of the mortgage: 30
The monthly repayments are 1703.37$

Code Structure

 * monthly_repayment(amount, interest, duration): Calculates monthly repayment.
 * loan_amount(repayment, interest, duration): Computes the maximum loan amount.
 * loan_duration(repayment, interest, amount): Estimates loan duration in years.
 * interest_rate(amount, repayment, duration): Approximates the interest rate.

Notes

Ensure input values are numeric to avoid errors.
For edge cases, such as very low repayment or interest rates, additional handling is included.

License

This project is licensed under the GPL v3 or later License.
