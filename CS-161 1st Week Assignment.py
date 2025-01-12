# this imports the datetime library
import datetime
# this is my starting date of january 1st
start_date = datetime.date(2025, 1, 1)
# this is my end date of february 1st
end_date = datetime.date(2025, 2, 1)
# this gets the number of days in january by subtracting the 2 dates
days = (end_date - start_date).days
# this calculates the seconds by multiplying the days by the hours, minutes, and seconds
seconds_in_january = days * 24 * 60 * 60

# here are my pets type and name
pet_type = "cat"
pet_name = "Salem"
# here is my print statement for step 1
print(f"I have a {pet_type}. and his name is {pet_name}")

first_name = input("Enter your first name: ")
# I defined these inputs as integers so they can be added, multiplied, and divided below
current_age = int(input("Enter your current age: "))
yearly_savings = int(input("Enter your yearly savings: "))
future_age = current_age + 10
future_savings = yearly_savings * 5
monthly_savings = future_savings / 60

# this is my step 2 print statement using \n so as to only use a single print across multiple lines
print(f"Hello {first_name}! You are currently {current_age} years old."
      f"\nIn 10 years, you will be {future_age} years old."
      f"\nIf you save ${yearly_savings} each year, in 5 years you will have saved ${future_savings}."
      f"\nYour average monthly savings is ${monthly_savings:.2f}.")

# this is my step 3 print statement using the seconds_in_january calculated using the datetime library
print(f"The number of seconds in January is {seconds_in_january}")

# here are my variables for step 4 using the floor division and modulo operators
number_of_eggs = int(input("Enter the number of eggs: "))
dozens_of_eggs = number_of_eggs // 12
eggs_remainder = number_of_eggs % 12

# here is my step 4 print statement
print(f"This makes {dozens_of_eggs} dozen eggs with {eggs_remainder} left over.")