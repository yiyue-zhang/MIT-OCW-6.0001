# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# PART A
# =============================================================================
# =============================================================================
# annual_salary = int(input('Enter your annual salary:'))
# portion_saved = float(input('Enter the percent of your salry to save, as decimal:'))
# total_cost = int(input('Enter the cost of your dream home:'))
# current_saving = 0
# month = 0
# portion_down_payment = .25*total_cost
# monthly_salary = annual_salary/12
# r = .04
# while portion_down_payment > current_saving:
#     current_saving += monthly_salary*portion_saved + current_saving*r/12
#     month += 1
# print('Number of months:', month)
# =============================================================================

# =============================================================================
# PART B
# =============================================================================

# =============================================================================
# annual_salary = int(input('Enter your annual salary:'))
# portion_saved = float(input('Enter the percent of your salry to save, as decimal:'))
# total_cost = int(input('Enter the cost of your dream home:'))
# semi_annual_raise = float(input('Enter the semi-annual raise, as decimal:'))
# current_saving = 0
# month = 0
# portion_down_payment = .25*total_cost
# monthly_salary = annual_salary/12
# r = .04
# while portion_down_payment > current_saving:
#     current_saving += monthly_salary*portion_saved + current_saving*r/12
#     month += 1
#     if month%6 == 0:
#         monthly_salary += semi_annual_raise*monthly_salary
# print('Number of months:', month)
# =============================================================================

# =============================================================================
# PART C infinitely for loop?
# =============================================================================
# =============================================================================
annual_salary = int(input('Enter the starting salary:'))
total_cost = 1000000
portion_down_payment = .25 * total_cost
semi_annual_raise = .07
step = 0
r = .04
low = 0
high = 10000
while True:
    monthly_salary = annual_salary / 12
    current_saving = 0
    portion_saved = (high + low) / 2 / 10000
    step += 1
    for month in range(0, 36):
        current_saving += monthly_salary * portion_saved + current_saving * r / 12
        if month % 6 == 0:
            monthly_salary += semi_annual_raise * monthly_salary
    if abs(current_saving - portion_down_payment) <= 100:
        print('Best savings rate:', portion_saved)
        print('Steps in bisection search:​', step)
        break
    #reduce rate because saving too much
    elif abs(current_saving - portion_down_payment) > 100 and current_saving > portion_down_payment:
        high = portion_saved
    #increase rate because saving too little
    elif abs(current_saving - portion_down_payment) > 100 and current_saving > portion_down_payment:
        low = portion_saved
    if high == low:
        print('It is not possible to pay the down payment in three years.')
        break

