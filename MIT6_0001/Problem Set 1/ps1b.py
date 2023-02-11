### Date: 02/05/2023
### Author Name: Changhyun Park
### Course: MIT OPENCOURSEWARE 6.0001 Fall 2016
### Part B: Saving, with a raise

'''
In part A, we unrealistically assumed that your salary did not change. So
we are going to build on your solution to Part A by factoring in a raise
every six months
'''

annual_salary = float(input("Enter you starting annual salary: "))
portion_saved = float(input("Enter your portion of salary to be saved, as a decimal: "))
total_cost    = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enther your semi-annual salary: "))


portion_down_payment = 0.25 # the portion of the cost needed for a down payment (25%)
current_savings = 0 # the amount that you have saved thus far
monthly_salary = annual_salary/12

r = 0.04 # 매달 annual earn is 4%

total_money_need = portion_down_payment * total_cost
number_of_months = 0

while(current_savings <= total_money_need):
    current_savings += monthly_salary * portion_saved
    current_savings += current_savings * r / 12 # At the end of each month annual return 받음
    
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12

print("Number of months: ", number_of_months)