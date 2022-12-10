
#Getting necessary functions from datetime library
from datetime import date

#gathering user info
user_name = input('What is your name?\n')
user_age = input('What is your age?\n')
user_age = int(user_age)

#Calculting user birth age:
year = date.today().year
b_year = year - user_age

#printing results:
print('Name and birth year: ', user_name, b_year)
