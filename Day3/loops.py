#Asabeneh IT, [12/28/2021 12:54 PM]

a = 10
if a > 0:
    print(f'{a} is a positive  number')
elif a < 0:
    print(f'{a} is a negative number')
elif a == 0:
    print(f'{a} is zero')
else:
    print('We do not know about this number')


weather = input('What is the weather like to day? ').lower()
print(weather)

if weather == 'rainy' :
    print('Please take an umbrella or a raincoat')
elif weather == 'shiny':
    print('The day seems shiny go out freely')
elif weather == 'snowy':
    print('It might be slipper')
elif weather == 'cloudy':
    print('It is good to consider an umbrella')
elif weather == 'foggy':
    print('There might limited visibility')
else:
    print('No one know the weather')

"""

He is Asabeneh Yetayeh. He is 250 years old. He live in Helsink, Finland. 

"""
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
country = input('Where are you from? ')
city = input('What is the capital city? ')
year_born = input('When were you born')
current_year = 2021

gender = input('What is your gender ? ')

Fassica Damtew, [12/28/2021 1:07 PM]
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
country = input('Where are you from? ')
city = input('What is the capital city? ')
year_born = int(input('When were you born? '))
current_year = 2021
age = current_year - year_born
gender = input('What is your gender ? female or male?').lower()

pronoun = ''
if gender == 'female':
    pronoun = 'She'
else:
    pronoun = 'He'

print(f'{pronoun} is {first_name} {last_name}. {pronoun} is {age} years old. {pronoun} lives in {city}, {country}.')

Asabeneh IT, [12/28/2021 2:44 PM]

