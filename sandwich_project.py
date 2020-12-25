'''Sandwich Maker  Write a program that asks users for their sandwich
preferences. The program should use PyInputPlus to ensure that they enter valid
input, such as:    Using inputMenu() for a bread type: wheat, white, or
sourdough.  Using inputMenu() for a protein type: chicken, turkey, ham, or
tofu.  Using inputYesNo() to ask if they want cheese.  If so, using inputMenu()
to ask for a cheese type: cheddar, Swiss, or mozzarella.  Using inputYesNo() to
ask if they want mayo, mustard, lettuce, or tomato.  Using inputInt() to ask
how many sandwiches they want. Make sure this number is 1 or more.  Come up
with prices for each of these options, and have your program display a total
cost after the user enters their selection.'''
from pyinputplus import inputInt, inputMenu
import os
from time import sleep

items = {
    'bread': {
        'wheat': 10,
        'white': 20,
        'sourbread': 30},
    'protein': {
        'chicken': 20,
        'turkey': 20,
        'ham': 20},
    'cheese': {
        'cheddar': 50,
        'swiss': 15,
        'mozarella': 60},
    'souce': {
        'mayo': 5,
        'mustard': 6,
        'lettuce': 2,
        'tomato': 3}
}


def display_type_of_item_and_price(item):
    for elements in items[item]:
        price = items[item].get(elements)
        print(f'{elements} ---> ${price}')


want_new_other = True
while want_new_other:
    total = 0
    print('welcome to bread prepare yourself!!')
    quantity_sandwich = inputInt('How many sandwich do you want: ', min=1)

    has_prepared_all_sandwich = False
    while not has_prepared_all_sandwich:

        display_type_of_item_and_price('bread')

        type_bread = inputMenu(['wheat', 'white', 'sourbread'],
                               prompt='choose one please: \n')

        display_type_of_item_and_price('protein')

        type_protein = inputMenu(['chicken', 'turkey', 'ham'],
                                 prompt='choose one please: \n')

        display_type_of_item_and_price('cheese')

        type_cheese = inputMenu(['cheddar', 'swiss', 'mozarella'],
                                prompt='choose one please: \n')

        display_type_of_item_and_price('souce')

        type_souce = inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'],
                               prompt='choose one please: \n')

        price_type_of_bread = items['bread'].get(type_bread)
        price_type_of_protein = items['protein'].get(type_protein)
        price_type_of_cheese = items['cheese'].get(type_cheese)
        price_type_of_souce = items['souce'].get(type_souce)

        total = price_type_of_bread + price_type_of_cheese +\
            price_type_of_souce + price_type_of_protein

        print(f'total bill {total}')

        quantity_sandwich -= 1
        if quantity_sandwich == 0:
            has_prepared_all_sandwich = True
            sleep(30)
            os.system('cls')
