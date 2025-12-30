# Personal income tax calculator for 2009

# Ask user for filing status and income
status = int(input("Enter filing status (0-single, 1-married jointly, 2-married separately, 3-head of household): "))
income = float(input("Enter taxable income: "))

tax = 0

# Define tax brackets
if status == 0:  # Single
    brackets = [(8350, 0.10), (33950, 0.15), (82250, 0.25),
                (171550, 0.28), (372950, 0.33)]
elif status == 1:  # Married filing jointly
    brackets = [(16700, 0.10), (67900, 0.15), (137050, 0.25),
                (208850, 0.28), (372950, 0.33)]
elif status == 2:  # Married filing separately
    brackets = [(8350, 0.10), (33950, 0.15), (68525, 0.25),
                (104425, 0.28), (186475, 0.33)]
elif status == 3:  # Head of household
    brackets = [(11950, 0.10), (45500, 0.15), (117450, 0.25),
                (190200, 0.28), (372950, 0.33)]
else:
    print("Invalid filing status")
    exit()

previous_limit = 0

# Calculate tax
for limit, rate in brackets:
    if income > limit:
        tax += (limit - previous_limit) * rate
        previous_limit = limit
    else:
        tax += (income - previous_limit) * rate
        break

# Tax for income above last bracket
if income > previous_limit:
    tax += (income - previous_limit) * 0.35

print(f"Total tax is: ${tax:.2f}")
