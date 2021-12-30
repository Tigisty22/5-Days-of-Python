from countries_list import countries
from pprint import pprint
def get_countries_with_five_letter():
    five_letter = []
    for c in countries:
        if len(c) == 5:
            five_letter.append(c)
    return five_letter


pprint(get_countries_with_five_letter())