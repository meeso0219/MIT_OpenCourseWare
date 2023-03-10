### Date: 02/11/2023
### Author Name: Changhyun Park
### Course: MIT OPENCOURSEWARE 6.0001 Fall 2016
### Part C: Finding the right amount to save away

'''
    In Part B, you had a chance to explore how both the percentage of 
    your salary that you save each month and your annual raise affect
    how long it takes you to save for a down payment. This is nice, but
    suppose you want to set a particular goal, e.g to be able to afford
    the down payment in three years. How much should you save each month
    to achieve this? In this problem, you are going to write a program
    to answer that question. To simplify things, assume:

        1. Your semi-annual raise is .07 (7%)
        2. Your investments have an annual return of 0.04 (4%)
        3. The down payment is 0.25 (25%) of the cost of the house
        4. The cost of the house that you are saving for is $1M.
    
    You are now going to try to find the best rate of savings to achieve
    a down payment on a $1M house in 36 months. Since hitting this exactly
    is a challenge, we simply want your savings to be within $100 of the
    required down payment.
'''

epsilon = 100.0 # $100

annual_salary = float(input("Enter you starting annual salary: "))
monthly_salary = annual_salary / 12

portion_down_payment = 0.25 # 25%
annual_return = 0.04 # 4%
semi_annual_raise = 0.07
total_cost = 1000000.0
number_of_months = 36
current_savings = 0
total_money_need = portion_down_payment * total_cost

number_of_guesses = 0

low = 0.0
high = 1.0
guess = (high + low) / 2.0
portion_saved = guess

# TODO
while number_of_months >= 36 or current_savings >= total_money_need:
    number_of_guesses += 1
    number_of_months += 1
    portion_saved = guess


