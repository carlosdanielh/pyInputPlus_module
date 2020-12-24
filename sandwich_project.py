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
from pyinputplus import inputStr, inputInt, inputMenu
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


want_new_other = True
while want_new_other:
    print('welcome to bread prepare yourself!!')
    quantity_sandwich = inputInt('How many sandwich do you want: ', min=1)

    has_prepared_all_sandwich = False
    while not has_prepared_all_sandwich:
        type_bread = inputMenu(['wheat', 'white', 'sourbread'],
                               prompt='choose one please')
        quantity_sandwich -= 1
        if quantity_sandwich == 0:
            has_prepared_all_sandwich = True
