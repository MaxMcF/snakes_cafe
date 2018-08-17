from textwrap import dedent
from decimal import Decimal, ROUND_UP
import sys
import uuid
import math
import copy


# This currently does not allow for multi line inputs to work. Needs refactoring in the remove function as well. Need everything for lab 3, currently nothing...

WIDTH = 96
# order_complete = False
DEFAULT_MENU = {
    'Appetizers': {
        'Wings': [2.00, 10],
        'Cookies': [2.50, 10],
        'Spring Rolls': [3.25, 10],
        'Fries': [3.15, 10],
        'Fried Rice': [4.15, 10],
        'Poutine': [6.35, 10],
        'Bean Dip': [1.19, 10],
        'Cheese Sticks': [5.75, 10],
        'Chips And Dip': [2.75, 10],
    },
    'Entrees': {
        'Salmon': [12.75, 10],
        'Steak': [18.50],
        'Meat Tornado': [22.99, 10],
        'A Literal Garden': [199.99, 10],
        'Burrito': [8.50, 10],
        'Pizza': [15.00, 10],
        'Fajitas': [16.75, 10],
        'Chicken Katsu': [10.99, 10],
        'Fried Chicken': [15.99, 10],
    },
    'Desserts': {
        'Ice Cream': [5.00, 10],
        'Cake': [15.99, 10],
        'Pie': [12.25, 10],
        'Gelato': [8.00, 10],
        'Popsicle': [1.50, 10],
        'Milkshake': [6.20, 10],
        'Creme Brulee': [8.99, 10],
        'Chocolate Bar': [4.99, 10],
        'Peach Cobbler': [12.99, 10],
    },
    'Drinks': {
        'Coffee': [5.00, 10],
        'Tea': [3.75, 10],
        'Blood of the Internet': [666.66, 10],
        'Kool-Aid': [3.75, 10],
        'Martini': [7.50, 10],
        'Purple Drank': [12.00, 10],
        'Beer': [5.75, 10],
        'Lemonade': [3.99, 10],
        'Shirley Temple': [4.55, 10],
    },
    'Sides': {
        'Hash Browns': [3.00, 10],
        'Bacon': [2.50, 10],
        'BBQ Sauce': [0.50, 10],
        'Guacamole': [500.00, 10],
        'Fortune Cookie': [1.00, 10],
        'Pickles': [2.75, 10],
        'Tatar Sauce': [0.50, 10],
        'Ketchup': [0.50, 10],
        'Mayonnaise': [0.50, 10],
    },
    }

CART = {
}

# This function displays the initial greeting, as well as the function commands available
def greeting():
    ln_one = 'Welcome to the Snakes Cafe!'
    ln_two = 'Please see our menu below.'
    ln_three = 'To view the menu at any time, type "menu"'
    ln_four = 'To view any menu section, type the section'
    ln_five = 'To view your order, type "order"'
    ln_six = 'To remove an item from your order, type "remove (your item)"'
    ln_seven = 'To quit at any time, type "quit"'

    print(dedent(f'''
        {'*' * WIDTH}
        {'**' + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + ln_one + (' ' * (((WIDTH - len(ln_one)) // 2)-1)) + '**'}
        {'**' + (' ' * (((WIDTH - len(ln_two)) // 2)-2)) + ln_two + (' ' * (((WIDTH - len(ln_two)) // 2)-2)) + '**'}
        {'**' + (' ' * (((WIDTH - len(ln_three)) // 2)-2)) + ln_three + (' ' * (((WIDTH - len(ln_three)) // 2)-2)) + '**'}
        {'**' + (' ' * (((WIDTH - len(ln_four)) // 2)-2)) + ln_four + (' ' * (((WIDTH - len(ln_four)) // 2)-2)) + '**'}
        {'**' + (' ' * (((WIDTH - len(ln_five)) // 2)-2)) + ln_five + (' ' * (((WIDTH - len(ln_five)) // 2)-2)) + '**'}
        {'**' + (' ' * (((WIDTH - len(ln_six)) // 2)-2)) + ln_six + (' ' * (((WIDTH - len(ln_six)) // 2)-2)) + '**'}
        {'**' + ((WIDTH-4) * ' ') + '**'}
        {'**' + (' ' * (((WIDTH - len(ln_seven)) // 2)-2)) + ln_seven + (' ' * (((WIDTH - len(ln_seven)) // 2)-2)) + '**'}
        {'*' * WIDTH}
    '''))


# This function displays the menu of items.
def menu():
    for section in ITEMS.keys():
        ln_one = section
        print(dedent(f'''

            {ln_one}
            {'-' * len(ln_one)}
        '''))
        for elm in ITEMS[section]:
            ln_two = elm
            ln_three = format_nums(ITEMS[section][elm][0])
            ln_four = str(ln_two) + (' ' * (WIDTH - (len(ln_two) + len(ln_three)))) + str(ln_three)
            print(dedent(f'''{ln_four}'''))


# This function displays a question, and call the order_something function with user input as the argument
def order_question():
    ln_one = 'What would you like to order?'
    question = dedent(f'''
        {'*' * WIDTH}
        {'**' + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + ln_one + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + '**'}
        {'*' * WIDTH}
    ''')
    user_input = input(question)
    order_something(user_input)


# This function calls the menu function and allows for the user to input a new command
def view_menu():
    menu()
    selection = input('')
    order_something(selection)


# This function allows the user to view a specific category, as well as all the items within that category
def view_category(category):
    ln_one = category
    print(dedent(f'''
        {ln_one}
        {'-' * len(ln_one)}
        '''))
    for section in ITEMS.keys():
        if category == section:
            for elm in ITEMS[section]:
                ln_two = elm
                ln_three = format_nums(ITEMS[section][elm][0])
                ln_four = str(ln_two) + (' ' * (WIDTH - (len(ln_two) + len(ln_three)))) + str(ln_three)
                print(dedent(f'''{ln_four}'''))
    print(dedent('''
    '''))


# This function displays the total cost owed depending on the state of the users order
def view_order_total():
    total_cost = 0
    ln_one = 'The Snakes Cafe'
    ln_two = '"Eatability unconstricted!"'
    ln_three = str('Order #') + str(uuid.uuid4())
    print(dedent(f'''
        {'*' * WIDTH}
        {ln_one}
        {ln_two}

        {ln_three}
        {'=' * WIDTH}
    '''))
    for elm in CART:
        for sections in ITEMS:
            if elm in ITEMS[sections]:
                total_cost = total_cost + (CART[elm] * ITEMS[sections][elm][0])
                ln_four = str(elm) + ' x' + str(CART[elm])
                item_total_cost = CART[elm] * ITEMS[sections][elm][0]
                item_cost_dec = str("{:.2f}".format(item_total_cost))
                ln_five = '$' + str(item_cost_dec)
                white_space_length = (' ' * (WIDTH - (len(ln_four) + len(ln_five))))
                print(dedent(f'''
                {ln_four + white_space_length + ln_five}'''))
    tax_total = total_cost * (0.101)
    totals_total = total_cost + tax_total
    ln_six = 'Subtotal'
    ln_seven = format_nums(total_cost)
    white_space_length_01 = (' ' * (WIDTH - (len(ln_six) + len(ln_seven))))
    ln_eight = 'Sales Tax'
    ln_nine = format_nums(tax_total)
    white_space_length_02 = (' ' * (WIDTH - (len(ln_eight) + len(ln_nine))))
    ln_ten = 'Total Due'
    ln_eleven = format_nums(totals_total)
    white_space_length_03 = (' ' * (WIDTH - (len(ln_ten) + len(ln_eleven))))
    print(dedent(f'''
        {'-' * WIDTH}
        {ln_six + white_space_length_01 + ln_seven}
        {ln_eight + white_space_length_02 + ln_nine}
        {'-' * len(ln_eight)}
        {ln_ten + white_space_length_03 + ln_eleven}
        {'*' * WIDTH}
    '''))
    selection = input('')
    order_something(selection)


# This function removes a single item from the users current meal.
def remove_item(item_remove):
    item_to_remove_placeholder = str(item_remove).split()[1::]
    item_to_remove = ' '.join(item_to_remove_placeholder)
    print(item_to_remove)
    if item_to_remove in CART:
        if CART[item_to_remove] > 1:
            CART[item_to_remove] -= 1
            print(dedent(f'''
            One order of {item_to_remove} has been removed from your order.
            '''))
        elif CART[item_to_remove] <= 1:
            CART.pop(item_to_remove, None)
            print(dedent(f'''
            One order of {item_to_remove} has been removed from your order.
            '''))
    else:
        print(dedent(f'''
        You can only remove menu items you've already added!
        '''))
        selection = input('')
        order_something(selection)
    view_order_total()


# This function is the main user input handler.
def order_something(user_input):
    user_input_placeholder = str(user_input).split()[0::]
    for i in range(len(user_input_placeholder)):
        user_input_placeholder[i] = user_input_placeholder[i].capitalize()

    cap_input = ' '.join(user_input_placeholder)
    if cap_input == 'Quit':
        exit()
        return
    elif cap_input == 'Menu':
        view_menu()
        return
    elif cap_input == 'Order':
        view_order_total()
        return
    elif cap_input.split()[0] == 'Remove':
        remove_item(cap_input)
        return
    if cap_input in ITEMS:
        view_category(cap_input)
        selection = input('')
        order_something(selection)
        return
    for sections in ITEMS.keys():
        if cap_input in ITEMS[sections]:
            add_to_cart(cap_input)

            # except TypeError:
            #     quantity_error()
    else:
        wrong_order()


def add_to_cart(cap_input):
    for sections in ITEMS.keys():
        if cap_input in ITEMS[sections]:
            quantity_added = input(dedent('''Quantity?
            '''))
            if quantity_added.isdigit() or quantity_added == '':
                if quantity_added == '':
                    quantity_added = '1'
                quantity_added = int(quantity_added)
                for sections in ITEMS:
                    if cap_input in ITEMS[sections]:
                        temp_quant = ITEMS[sections][cap_input][1]
                        ITEMS[sections][cap_input][1] -= quantity_added
                        if ITEMS[sections][cap_input][1] < 0:
                            ITEMS[sections][cap_input][1] = temp_quant
                            out_of_stock(cap_input)
                        else:
                            if cap_input in CART:
                                if quantity_added > 0:
                                    CART[cap_input] += quantity_added
                                    order_complete(cap_input)
                                    return
                                else:
                                    CART[cap_input][0] += 1
                                    order_complete(cap_input)
                                    return
                            elif cap_input not in CART:
                                CART[cap_input] = quantity_added
                                order_complete(cap_input)
                                return
            else:
                quantity_error()


def quantity_error():
    print(dedent('''
            Invalid quantity! Try again
        '''))
    selection = input('')
    order_something(selection)

# This function displays when the user puts in an incorrect order
def wrong_order():
    print(dedent('''
            Please order something off the menu!
        '''))
    selection = input('')
    order_something(selection)


def out_of_stock(item_input):
    print(dedent(f'''
    Sorry, we dont have enough {item_input} in stock! Try ordering less
    '''))
    selection = input(' ')
    order_something(selection)

# This function displays when a single item has been added to the users meal order
def order_complete(order_status):
    print(order_status)
    if CART[order_status] > 1:
        string_one = ' orders of '
        string_two = ' have been added to your meal'
    else:
        string_one = ' order of '
        string_two = ' has been added to your meal'
    running_total = 0
    for section in ITEMS.keys():
        for elm in ITEMS[section]:
            if elm == order_status:
                running_total = running_total + (int(CART[order_status]) * ITEMS[section][elm][0])

    string_three = CART[order_status]
    string_four = order_status
    ln_one = str(string_three) + str(string_one) + str(string_four) + str(string_two)
    ln_two = 'Your running total is ' + format_nums(running_total)

    print(dedent(f'''
        {'**' + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + ln_one + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + '**'}
        {'**' + (' ' * (((WIDTH - len(ln_two)) // 2)-2)) + ln_two + (' ' * (((WIDTH - len(ln_two)) // 2)-2)) + '**'}
    '''))
    selection = input(' ')
    order_something(selection)


def format_nums(number):
    '''This formats any number into a dollar amount to 2 decimals
    '''
    string = '$' + str("{:.2f}".format(float(number)))
    return string


def check_menu():
    '''This function checks to see if the user wants to use a custom menu.
    If they do, it replaces the default menu with the custom one.
    '''
    menu_input = input('''Type custom if using a custom menu, otherwise hit enter
    >''')
    if menu_input.lower() == 'custom':
        menu_path = input('''Please type the path name of the menu file (example: ./assets/custom_menu.csv)
        >''')
        file_structure = menu_path.split('/')
        file_extension = file_structure[-1].split('.')
        if file_extension[1] != 'csv':
            print('You did not enter a valid CSV file, please try again')
            return check_menu()
        else:
            try:
                with open(menu_path) as file:
                    csv_menu = file.read()
                    custom_menu = menu_decoder(csv_menu)
                    print(custom_menu)
                    return custom_menu
            except FileNotFoundError:
                print('File Not Found!')
                return check_menu()
    elif menu_input.lower() == '':
        return DEFAULT_MENU
    else:
        print('That was not a valid command, Try again')
        return check_menu()


def menu_decoder(csv_menu):
    '''This function takes the raw .csv file and formats it the same way that

    '''
    custom_menu = {}
    line_list = csv_menu.split('\n')

    for line in line_list:
        seperated_line = line.split(',')
        temp_dict = {seperated_line[0]: [float(seperated_line[2]), int(seperated_line[3])]}
        if str(seperated_line[1]) not in custom_menu:
            custom_menu[str(seperated_line[1])] = temp_dict
        else:
            custom_menu[str(seperated_line[1])][seperated_line[0]] = [float(seperated_line[2]), int(seperated_line[3])]
    return custom_menu


# This function allows the user to exit the program
def exit():
    print(dedent('''
        Thanks you, come again!
    '''))
    sys.exit()


ITEMS = check_menu()

# This is the main function handler
def run():
    greeting()
    menu()
    order_question()



if __name__ == '__main__':
    run()
