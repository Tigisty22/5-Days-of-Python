""" 
Mirteye 2, [12/29/2021 11:20 AM]
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
prin

Asabeneh IT, [12/29/2021 11:51 AM]
""" 
1. The name of the function is calculate_area_rectangle. It takes lenght and widht as parameters and it returns the area. Formulat of area = length * width
2. Calculate perimeter of a reactangle. It takes lenght and width as parameters and it should return the perimeter of the rectangle. Formula of perimeter = 2 * (lenght + width)

 """
 """ 

def cal_area_rectangle (l,w):
    area = l * w
    return area


print(cal_area_rectangle((4,3))

def cal_permeter_rectangle (l,w):
    permeter = 2*l + 2*w
    return permeter


print(cal_permeter_rectangle(4,3))






    