first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
country = input('Where are you from? ')
city = input('What is the capital city? ')
year_born = int(input('When were you born ? '))
current_year = 2021

gender = input('What is your gender ? ').lower()

pronoun=' '
if gender == 'female':
    pronoun ='She'
else:
    pronoun ='He'

print(f'{pronoun} is {first_name} {last_name}. {pronoun} is {current_year - year_born} old. {pronoun} lives in {city}, {country}')



""" 
1. The name of the function is calculate_area_rectangle. It takes lenght and widht as parameters and it returns the area. Formulat of area = length * width
2. Calculate perimeter of a reactangle. It takes lenght and width as parameters and it should return the perimeter of the rectangle. Formula of perimeter = 2 * (lenght + width)

 """

def add_two_nums(a, b):
    total = a  + b
    return total

def multiply_two_nums(a, b):
    mul = a * b
    return mul

def make_square(n):
    return n ** 2


def calculate_area_rectangle(length, width):
    return length * width

def generate_evens(n):
    evens = list(range(0, n + 1, 2))
    return evens

def calculate_weight (mass, gravity = 9.81):
    weight = mass * gravity
    return weight

def calc_perimeter_rect(length, width):
    perimeter = (length  + width) * 2
    return perimeter
