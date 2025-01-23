def monthly_repayment(loan, interest, duration):
    if type(loan) == int  or type(interest) == float or type(duration) == int:
        monthly_rate = interest / 100 / 12
        total_nr_repayments = duration * 12
        monthly_repayment = loan * (monthly_rate * (1 + monthly_rate) ** total_nr_repayments) / ((1 + monthly_rate) ** total_nr_repayments - 1)
    else:
        print("Please use number values")
    return monthly_repayment

print(monthly_repayment(500000,5.5,30))
