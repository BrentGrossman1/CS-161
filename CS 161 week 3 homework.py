import datetime

# Part 1, Ask the user to enter their name, then say hello and repeat their name.
user_name = input("What is your name? ")
print("Hello", user_name)

# Part 2, Ask the user to enter their age. Print out their age 5 years from now.
# For the given example in the instructions, print(x + 5), it will give an error because python
# is trying to add a string and an integer, you need to convert the users input to an int first.
user_age = input("What is your age? ")
print("In 5 years you will be", int(user_age) + 5)

# Part 3, Use concatenation and str() to print a message telling the user how old they will be in y years.
years_added = input("How many years do you want to add to your age? ")
# I am first adding the users_age and the years_added as integers
# and then converting that output to a string to concatenate to the rest of the print statement
print("In " + str(years_added) + " years you will be " + str(int(user_age) + int(years_added)))

# Extra Credit life expectancy/probable date of death
# This is a dictionary of male life expectancy with your age as a key to how many years left you have
male_life_expectancy = {
    0: 73.54, 1: 72.97, 2: 72.00, 3: 71.02, 4: 70.04, 5: 69.05,
    6: 68.06, 7: 67.07, 8: 66.08, 9: 65.09, 10: 64.10, 11: 63.10,
    12: 62.11, 13: 61.12, 14: 60.14, 15: 59.16, 16: 58.18, 17: 57.22,
    18: 56.27, 19: 55.33, 20: 54.40, 21: 53.47, 22: 52.55, 23: 51.64,
    24: 50.72, 25: 49.82, 26: 48.91, 27: 48.01, 28: 47.12, 29: 46.23,
    30: 45.34, 31: 44.46, 32: 43.57, 33: 42.69, 34: 41.82, 35: 40.94,
    36: 40.06, 37: 39.19, 38: 38.32, 39: 37.45, 40: 36.58, 41: 35.72,
    42: 34.86, 43: 34.00, 44: 33.15, 45: 32.30, 46: 31.45, 47: 30.61,
    48: 29.77, 49: 28.94, 50: 28.12, 51: 27.30, 52: 26.50, 53: 25.70,
    54: 24.91, 55: 24.14, 56: 23.37, 57: 22.61, 58: 21.87, 59: 21.13,
    60: 20.41, 61: 19.70, 62: 19.00, 63: 18.31, 64: 17.63, 65: 16.95,
    66: 16.29, 67: 15.63, 68: 14.98, 69: 14.33, 70: 13.69, 71: 13.06,
    72: 12.43, 73: 11.82, 74: 11.21, 75: 10.62, 76: 10.05, 77: 9.49,
    78: 8.95, 79: 8.42, 80: 7.92, 81: 7.43, 82: 6.96, 83: 6.50,
    84: 6.07, 85: 5.65, 86: 5.26, 87: 4.88, 88: 4.53, 89: 4.21,
    90: 3.90, 91: 3.62, 92: 3.36, 93: 3.14, 94: 2.94, 95: 2.76,
    96: 2.60, 97: 2.45, 98: 2.32, 99: 2.20, 100: 2.09, 101: 1.98,
    102: 1.87, 103: 1.77, 104: 1.67, 105: 1.58, 106: 1.49, 107: 1.40,
    108: 1.32, 109: 1.24, 110: 1.16, 111: 1.09, 112: 1.01, 113: 0.95,
    114: 0.88, 115: 0.82, 116: 0.76, 117: 0.70, 118: 0.65, 119: 0.60
}
# This is a dictionary of female life expectancy with your age as a key to how many years left you have
female_life_expectancy = {
    0: 79.30, 1: 78.70, 2: 77.74, 3: 76.75, 4: 75.77, 5: 74.78,
    6: 73.79, 7: 72.79, 8: 71.80, 9: 70.81, 10: 69.82, 11: 68.82,
    12: 67.83, 13: 66.84, 14: 65.85, 15: 64.86, 16: 63.88, 17: 62.90,
    18: 61.92, 19: 60.94, 20: 59.97, 21: 59.00, 22: 58.03, 23: 57.07,
    24: 56.11, 25: 55.15, 26: 54.19, 27: 53.23, 28: 52.28, 29: 51.33,
    30: 50.38, 31: 49.44, 32: 48.50, 33: 47.56, 34: 46.62, 35: 45.69,
    36: 44.76, 37: 43.83, 38: 42.91, 39: 41.98, 40: 41.07, 41: 40.15,
    42: 39.24, 43: 38.33, 44: 37.42, 45: 36.52, 46: 35.62, 47: 34.73,
    48: 33.84, 49: 32.95, 50: 32.07, 51: 31.20, 52: 30.33, 53: 29.47,
    54: 28.62, 55: 27.77, 56: 26.93, 57: 26.10, 58: 25.27, 59: 24.46,
    60: 23.65, 61: 22.86, 62: 22.07, 63: 21.29, 64: 20.52, 65: 19.75,
    66: 18.99, 67: 18.23, 68: 17.48, 69: 16.74, 70: 16.00, 71: 15.27,
    72: 14.56, 73: 13.85, 74: 13.16, 75: 12.49, 76: 11.83, 77: 11.19,
    78: 10.57, 79: 9.96, 80: 9.38, 81: 8.81, 82: 8.26, 83: 7.73,
    84: 7.21, 85: 6.72, 86: 6.26, 87: 5.82, 88: 5.41, 89: 5.02,
    90: 4.65, 91: 4.31, 92: 3.99, 93: 3.71, 94: 3.45, 95: 3.22,
    96: 3.01, 97: 2.82, 98: 2.66, 99: 2.50, 100: 2.35, 101: 2.21,
    102: 2.08, 103: 1.95, 104: 1.82, 105: 1.71, 106: 1.59, 107: 1.49,
    108: 1.39, 109: 1.29, 110: 1.20, 111: 1.11, 112: 1.03, 113: 0.95,
    114: 0.88, 115: 0.82, 116: 0.76, 117: 0.70, 118: 0.65, 119: 0.60
}
current_year = datetime.datetime.now().year  # this gets the current year using the imported datetime library
users_birth_year = current_year - int(user_age) # this gets the users birth year by subtracting the users age from the current year
male_probable_death_year = current_year + male_life_expectancy[int(user_age)] # this estimates the male users death year by adding their remaining years to the current year
female_probable_death_year = current_year + female_life_expectancy[int(user_age)] # this estimates the female users death year by adding their remaining years to the current year
print(f"At your current age of {user_age}, you were born roughly in {users_birth_year},\n"
      f"If you are a male, your probable date of death based on your age is {male_life_expectancy[int(user_age)]} years from now (or the year {int(male_probable_death_year)})\n"
      f"If you are a female, your probable date of death based on your age is {female_life_expectancy[int(user_age)]} years from now (or the year {int(female_probable_death_year)})")

# Part 4, Ask the user to enter values that might be floating point.
# using float() here to convert the users input into a floating point number
hours_worked = float(input("How many hours do you work in a week?: "))
hourly_wage = float(input("What is your hourly wage, without the $ sign: "))

# Part 5, Print out the result of the calculation in a single print statement, using concatenation.
print(f"Your gross pay this week is ${hourly_wage * hours_worked:.2f}\n" 
      f"Your estimated annual gross pay will be ${((hourly_wage * hours_worked) * 4) * 12:.2f}")
    # I used f strings here to print out everything in 1 print statement and :.2f to limit the number of decimals printed

# Extra credit Tax tables
# This calculates annual income for a 40-hour work week times 50 weeks worked
annual_income = 40 * 50 * hourly_wage

# These are the tax brackets and associated tax rates
tax_brackets = [
    (11600.00, 0.10),
    (47150.00, 0.12),
    (100525.00, 0.22),
    (191950.00, 0.24),
    (243725.00, 0.32),
    (609350.00, 0.35),
    (float('inf'), 0.37)]
# This find the tax rate based on the users calculated annual_income by using a for loop to iterate through
# each pay bracket to find the right tax rate
tax_rate = 0.37
for pay_limit, tax in tax_brackets:
    if annual_income <= pay_limit:
        tax_rate = tax
        break
# this finds hopw much you owe in taxes by multiplying your tax rate by your annual income
tax_amount = tax_rate * annual_income
# this finds your net pay by subtracting your taxes from your annual or gross pay
net_pay = annual_income - tax_amount

print(f"Your tax amount is ${tax_amount:.2f}\n"
      f"And your yearly income after taxes is {net_pay:.2f}")