import math

def monthly_repayment(loan, interest, duration):
    if type(loan) == int  or type(interest) == float or type(duration) == int:
        monthly_rate = interest / 100 / 12
        total_nr_repayments = duration * 12
        monthly_repayment = loan * (monthly_rate * (1 + monthly_rate) ** total_nr_repayments) / ((1 + monthly_rate) ** total_nr_repayments - 1)
    else:
        print("Please use number values")
    return monthly_repayment

def loan_amount(repayment, interest, duration):
    if type(repayment) == int  or type(interest) == float or type(duration) == int:
        monthly_rate = interest / 100 / 12
        total_nr_repayments = duration * 12
        loan = repayment * ((1 + monthly_rate) ** total_nr_repayments - 1) / (monthly_rate * (1 + monthly_rate) ** total_nr_repayments)
    else:
        print("Please use number values")
    return loan

def loan_duration(repayment, interest, amount):
    if type(repayment) == int  or type(interest) == float or type(amount) == int:
        monthly_rate = interest / 100 / 12
        if repayment <= amount * interest:
            duration_months = (math.log(repayment) - math.log(repayment - amount * monthly_rate)) / math.log(1 + monthly_rate)
            duration = duration_months / 12
        else:
            print("The repayment amount is too low: it must cover the interests.")
    else:
        print("Please use number values")
    return round(duration, 1)

def interest_rate(loan, repayment, duration):
    if not all(isinstance(value, (int, float)) for value in [loan, repayment, duration]):
        print("Please use valid numeric values")
        return
    cover = repayment * 12 * duration
    if cover < loan:
        print("Repayment is too low to cover the loan: consider increasing it")
        return None
    interest = 0.01
    #if repayment <= loan * (interest / 100 / 12):
        #print("Repayment amount is too low for the given loan and duration")
        #return
    
    monthly_rate = interest / 100 / 12
    total_nr_repayments = duration * 12
    inter = True
    #max_iterations = 1000
    iteration = 0
    previous_adjustment = 0
    
    while inter:
        if monthly_rate == 0:
            raise ValueError("Monthly rate cannot be zero")
        monthly_calculated = loan * (monthly_rate * (1 + monthly_rate) ** total_nr_repayments) / ((1 + monthly_rate) ** total_nr_repayments - 1)
        #print(f"monthly calculated = {monthly_calculated}")
        difference = abs(monthly_calculated - repayment)
        #print(f"difference = {difference}")
        if round(difference, 3) > 0.01:
            adjustment = 0.1 * (difference / repayment)
            if monthly_calculated < repayment:
                adjustment = abs(adjustment)
            else:
                adjustment = -abs(adjustment)
            if abs(adjustment) == abs(previous_adjustment):
                adjustment /= 2
            previous_adjustment = adjustment
            if abs(adjustment) < 0.00001:
                print("Adjustment is small enough, breaking the loop.")
                break
            interest += adjustment
            #print(f"interest = {interest}")
            #print(f"adjustment = {adjustment}")
            #print(f"interest = {interest}")
            if interest <= 0:
                print("Unable to find a suitable interest rate. Consider increasing the repayment amount.")
                return None
            monthly_rate = interest / 100 / 12
        else:
            inter = False
        #iteration += 1
        #if iteration >= max_iterations:
            #print(f"Failed to converge on an interest rate after {iteration} iterations. Last calculated rate: {interest}%, with a montly repayment of  {monthly_calculated}$.")
            #return None
    return round(interest, 3), round(monthly_calculated, 0)

print(loan_duration(5000,5,500000))
