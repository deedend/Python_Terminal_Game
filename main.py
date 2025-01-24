import math

def monthly_repayment(amount, interest, duration):
    if all(isinstance(value, (int, float)) for value in [amount, interest, duration]):
        monthly_rate = float(interest) / 100 / 12
        total_nr_repayments = int(duration) * 12
        repayment = int(amount) * (monthly_rate * (1 + monthly_rate) ** total_nr_repayments) / ((1 + monthly_rate) ** total_nr_repayments - 1)
        return round(repayment, 2)
    else:
        print("Please use number values")

def loan_amount(repayment, interest, duration):
    if not all(isinstance(value, (int, float)) for value in [repayment, interest, duration]):
        print("Please use numeric values for repayment, interest, and duration.")
        return None
    monthly_rate = interest / 100 / 12
    total_nr_repayments = duration * 12
    if monthly_rate == 0:
        return repayment * total_nr_repayments
    loan = repayment * ((1 + monthly_rate) ** total_nr_repayments - 1) / (monthly_rate * (1 + monthly_rate) ** total_nr_repayments)
    return round(loan, 0)

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

def interest_rate(amount, repayment, duration):
    if not all(isinstance(value, (int, float)) for value in [amount, repayment, duration]):
        print("Please use valid numeric values")
        return
    cover = repayment * 12 * duration
    if cover < amount:
        print("Repayment is too low to cover the loan: consider increasing it")
        return None
    interest = 0.01
    
    monthly_rate = interest / 100 / 12
    total_nr_repayments = duration * 12
    inter = True
    iteration = 0
    previous_adjustment = 0
    
    while inter:
        if monthly_rate == 0:
            raise ValueError("Monthly rate cannot be zero")
        monthly_calculated = amount * (monthly_rate * (1 + monthly_rate) ** total_nr_repayments) / ((1 + monthly_rate) ** total_nr_repayments - 1)
        difference = abs(monthly_calculated - repayment)
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
            if interest <= 0:
                print("Unable to find a suitable interest rate. Consider increasing the repayment amount.")
                return None
            monthly_rate = interest / 100 / 12
        else:
            inter = False
    return round(interest, 3)#, round(monthly_calculated, 0)

while True:
    print("*** CodeCademy project - Mortgage Calculator ***\n")
    choice = input("Choose an option: \n1 - Calculate monthly repayment\n2 - Calculate loan amount\n3 - Calculate loan duration\n4 - Calculate (approximate) interest rate\nQ - Quit\n\nInput: ")
    if choice == "1":
          amount = int(input("Enter the loan amount: "))
          interest = float(input("Enter the interest rate: "))
          duration = int(input("Enter the duration of the mortgage: "))
          repayments = monthly_repayment(amount, interest, duration)
          print(f"The monthly repayments are {repayments}$")
    elif choice == "2":
          repayment = int(input("Enter the repayment amount: "))
          interest = float(input("Enter the interest rate: "))
          duration = int(input("Enter the duration of the mortgage: "))
          amount = loan_amount(repayment, interest, duration)
          print(f"The amount you can borrow is {amount}$")
    elif choice == "3":
          repayment = int(input("Enter the repayment amount: "))
          interest = float(input("Enter the interest rate: "))
          amount = int(input("Enter the loan amount: "))
          duration = loan_duration(repayment, interest, amount)
          print(f"The mortgage is {duration} years long")
    elif choice == "4":
          repayment = int(input("Enter the repayment amount: "))
          amount = int(input("Enter the loan amount: "))
          duration = int(input("Enter the duration of the mortgage: "))
          interest = interest_rate(amount, repayment, duration)
          print(f"The approximate interest rate is {interest}%")
    else:
          print("Exiting...")
          break
