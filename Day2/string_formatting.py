first_name = 'Tigist' 
last_name = 'Yoseph'
age = 99
city = 'ashburn'
country = 'USA'
skills = ['LINUX', 'SPANISH', 'TRAVEL', 'Python'] 
first_skill = ', '.join(skills[0:-1])
last_skill = skills[-1]
tech_lang = 'python'

print(f'I am {first_name} {last_name}.\nI live in {city} {country}.\nI am learning {tech_lang}.\nMy skills are {first_skill} and {last_skill}.\nI am {age} years old.') 

