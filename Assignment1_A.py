total_cost = float(input("Enter the cost of your dream home:"))  # Ask for total cost
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))  # Ask for portion saved
annual_salary = float(input("Enter your annual salary: "))  # Ask for annual salary
portion_down_payment = 0.25  # down payment rate
current_savings = 0.0  # current saving starts from 0
r = 0.04  # annual investment return rate
number_of_month = 0  # how many month to save

while current_savings < total_cost * portion_down_payment:  # when current saving < total cost, loop continue
    number_of_month += 1  # time flies
    current_savings += current_savings * r / 12  # investment return Year to month
    current_savings += annual_salary / 12 * portion_saved  # save part of salary every month (should switch with line11)
print(number_of_month)  # show how many month to save

