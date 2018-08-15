from textwrap import dedent
from decimal import Decimal, ROUND_UP
import sys
import uuid


WIDTH = 96
# order_complete = False
ITEMS = [
    {
    'section': 'Appetizers',
    'item': 'Wings',
    'item_selects': 0,
    'cost': 2.00,
    },
    {
    'section': 'Appetizers',
    'item': 'Cookies',
    'item_selects': 0,
    'cost': 2.50,
    },
    {
    'section': 'Appetizers',
    'item': 'Spring Rolls',
    'item_selects': 0,
    'cost': 3.25,
    },
    {
    'section': 'Appetizers',
    'item': 'Fries',
    'item_selects': 0,
    'cost': 3.15,
    },
    {
    'section': 'Appetizers',
    'item': 'Cheese Sticks',
    'item_selects': 0,
    'cost': 5.75,
    },
    {
    'section': 'Appetizers',
    'item': 'Chips and Dip',
    'item_selects': 0,
    'cost': 2.75,
    },
    {
    'section': 'Entrees',
    'item': 'Salmon',
    'item_selects': 0,
    'cost': 12.75,
    },
    {
    'section': 'Entrees',
    'item': 'Steak',
    'item_selects': 0,
    'cost': 18.50,
    },
    {
    'section': 'Entrees',
    'item': 'Meat Tornado',
    'item_selects': 0,
    'cost': 22.99,
    },
    {
    'section': 'Entrees',
    'item': 'A Literal Garden',
    'item_selects': 0,
    'cost': 199.99,
    },
    {
    'section': 'Entrees',
    'item': 'Burrito',
    'item_selects': 0,
    'cost': 8.50,
    },
    {
    'section': 'Entrees',
    'item': 'Pizza',
    'item_selects': 0,
    'cost': 15.00,
    },
    {
    'section': 'Desserts',
    'item': 'Ice Cream',
    'item_selects': 0,
    'cost': 5.00,
    },
    {
    'section': 'Desserts',
    'item': 'Cake',
    'item_selects': 0,
    'cost': 15.99,
    },
    {
    'section': 'Desserts',
    'item': 'Pie',
    'item_selects': 0,
    'cost': 12.25,
    },
    {
    'section': 'Desserts',
    'item': 'Gelato',
    'item_selects': 0,
    'cost': 8.00,
    },
    {
    'section': 'Desserts',
    'item': 'Popsicle',
    'item_selects': 0,
    'cost': 1.50,
    },
    {
    'section': 'Desserts',
    'item': 'Milkshake',
    'item_selects': 0,
    'cost': 6.20,
    },
    {
    'section': 'Drinks',
    'item': 'Coffee',
    'item_selects': 0,
    'cost': 5.00
    },
    {
    'section': 'Drinks',
    'item': 'Tea',
    'item_selects': 0,
    'cost': 3.75,
    },
    {
    'section': 'Drinks',
    'item': 'Blood of the Internet',
    'item_selects': 0,
    'cost': 666.66
    },
    {
    'section': 'Drinks',
    'item': 'Kool-Aid',
    'item_selects': 0,
    'cost': 3.75,
    },
    {
    'section': 'Drinks',
    'item': 'Martini',
    'item_selects': 0,
    'cost': 7.50,
    },
    {
    'section': 'Drinks',
    'item': 'Purple Drank',
    'item_selects': 0,
    'cost': 12.00,
    },
    {
    'section': 'Sides',
    'item': 'Hash Browns',
    'item_selects': 0,
    'cost': 3.00,
    },
    {
    'section': 'Sides',
    'item': 'Bacon',
    'item_selects': 0,
    'cost': 2.50,
    },
    {
    'section': 'Sides',
    'item': 'BBQ',
    'item_selects': 0,
    'cost': 0.50,
    },
    {
    'section': 'Sides',
    'item': 'Guacamole',
    'item_selects': 0,
    'cost': 500.00,
    },
    {
    'section': 'Sides',
    'item': 'Fortune Cookie',
    'item_selects': 0,
    'cost': 1.00,
    },
    {
    'section': 'Sides',
    'item': 'Pickles',
    'item_selects': 0,
    'cost': 2.75,
    },
    ]
SECTIONS = [
    {
    'section': 'Appetizers',
    },
    {
    'section': 'Entrees',
    },
    {
    'section': 'Desserts',
    },
    {
    'section': 'Drinks',
    },
    {
    'section': 'Sides',
    },
]

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
    for item in SECTIONS:
        ln_one = item['section']
        print(dedent(f'''

            {ln_one}
            {'-' * len(ln_one)}
        '''))
        for elm in ITEMS:
            if item['section'] == elm['section']:
                ln_two = elm['item']
                ln_three = format_nums(elm['cost'])
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
def view_category(section):
    ln_one = section
    print(dedent(f'''
        {ln_one}
        {'-' * len(ln_one)}
        '''))
    for elm in ITEMS:
        if section == elm['section']:
            ln_two = elm['item']
            ln_three = format_nums(elm['cost'])
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
    for elm in ITEMS:
        if elm['item_selects'] != 0:
            total_cost = total_cost + (elm['cost']*elm['item_selects'])
            ln_four = str(elm['item']) + ' x' + str(elm['item_selects'])
            item_total_cost = elm['item_selects'] * elm['cost']
            item_cost_dec = str("{:.2f}".format(item_total_cost))
            ln_five = '$' + str(item_cost_dec)
            # stln_five(Decimal('10.00')))
            white_space_length = (' ' * (WIDTH - (len(ln_four) + len(ln_five))))
            print(dedent(f'''
                {ln_four + white_space_length + ln_five}
            '''))
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
    for elm in ITEMS:
        if elm['item'].lower() == ' '.join(str(item_remove).lower().split()[1::]):
            if elm['item_selects'] > 0:
                elm['item_selects'] -= 1
                print(dedent(f'''
                One order of {elm['item']} has been removed from your order.
                '''))
            else:
                print(dedent(f'''
                You can only remove menu items you've already added!
                '''))
                selection = input('')
                order_something(selection)
                break
    view_order_total()


# This function is the main user input handler.
def order_something(user_input):
    if str(user_input).lower() == 'quit':
        exit()
        return
    elif str(user_input).lower() == 'menu':
        view_menu()
        return
    elif str(user_input).lower() == 'order':
        view_order_total()
        return
    elif str(user_input).lower().split()[0] == 'remove':
        remove_item(user_input)
        return
    for category in SECTIONS:
        if category['section'].lower() == str(user_input).lower():
            view_category(category['section'])
            selection = input('')
            order_something(selection)
            return
    for menu_items in ITEMS:
        if menu_items['item'].lower() == str(user_input).lower():
            menu_items['item_selects'] += 1
            order_complete(menu_items)
            return
    else:
        wrong_order()


# This function displays when the user puts in an incorrect order
def wrong_order():
    print(dedent('''
            Please order something off the menu!
        '''))
    selection = input('')
    order_something(selection)


# This function displays when a single item has been added to the users meal order
def order_complete(order_status):
    if order_status['item_selects'] > 1:
        string_one = ' orders of '
        string_two = ' have been added to your meal'
    else:
        string_one = ' order of '
        string_two = ' has been added to your meal'
    running_total = 0
    for elm in ITEMS:
        if elm['item_selects'] > 0:
            running_total = running_total + (elm['item_selects'] * elm['cost'])
    string_three = order_status['item_selects']
    string_four = order_status['item']
    ln_one = str(string_three) + str(string_one) + str(string_four) + str(string_two)
    ln_two = 'Your running total is ' + format_nums(running_total)

    print(dedent(f'''
        {'**' + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + ln_one + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + '**'}
        {'**' + (' ' * (((WIDTH - len(ln_two)) // 2)-2)) + ln_two + (' ' * (((WIDTH - len(ln_two)) // 2)-2)) + '**'}
    '''))
    selection = input(' ')
    order_something(selection)


def format_nums(number):
    string = '$' + str("{:.2f}".format(number))
    return string

# This function allows the user to exit the program
def exit():
    print(dedent('''
        Thanks you, come again!
    '''))
    sys.exit()


# This is the main function handler
def run():
    greeting()
    menu()
    order_question()



if __name__ == '__main__':
    run()
