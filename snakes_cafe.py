from textwrap import dedent
from decimal import Decimal, ROUND_UP
import sys
import uuid
import math
import copy


# This currently does not allow for multi line inputs to work. Needs refactoring in the remove function as well. Need everything for lab 3, currently nothing...

WIDTH = 96
# order_complete = False
ITEMS = {
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
        'Steak': [18.50, 10],
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

class Order():
    def __init__(self):
        self.id = uuid.uuid4()
        self.cart = {}

    def __len__(self):
        items_in_cart = self.cart.keys()
        return len(items_in_cart)

    def __repr__(self):
        total_cost = 0
        items_in_cart = 0
        for elm in self.cart:
            for sections in ITEMS:
                if elm in ITEMS[sections]:
                    total_cost = total_cost + (self.cart[elm] * ITEMS[sections][elm][0])
            items_in_cart = items_in_cart + self.cart[elm]
        return f'< Order: {self.id} | Items: {items_in_cart} | Total: {format_nums(total_cost)}>'

    def calc_total(self):
        for elm in self.cart:
            for sections in ITEMS:
                if elm in ITEMS[sections]:
                    total_cost = total_cost + (self.cart[elm] * ITEMS[sections][elm][0])
        return total_cost

    def add_item(self, item_name, quantity = 1):
        for sections in ITEMS.keys():
            if item_name in ITEMS[sections]:
                quantity_added = input(dedent('''Quantity?
                '''))
                if quantity_added.isdigit() or quantity_added == '':
                    if quantity_added == '':
                        quantity_added = '1'
                    quantity_added = int(quantity_added)
                    for sections in ITEMS:
                        if item_name in ITEMS[sections]:
                            temp_quant = ITEMS[sections][item_name][1]
                            ITEMS[sections][item_name][1] -= quantity_added
                            if ITEMS[sections][item_name][1] < 0:
                                ITEMS[sections][item_name][1] = temp_quant
                                out_of_stock(item_name, self)
                            else:
                                if item_name in self.cart:
                                    if quantity_added > 0:
                                        self.cart[item_name] += quantity_added
                                        return item_name
                                    else:
                                        self.cart[item_name][0] += 1
                                        return item_name
                                elif item_name not in self.cart:
                                    self.cart[item_name] = quantity_added
                                    return item_name
                else:
                    quantity_error(self)

    def remove_item(self, item_name, quantity = 1):
        if item_name in self.cart:
            if self.cart[item_name] > 1:
                self.cart[item_name] -= 1
                print(dedent(f'''
                One order of {item_name} has been removed from your order.
                '''))
            elif self.cart[item_name] <= 1:
                self.cart.pop(item_name, None)
                print(dedent(f'''
                One order of {item_name} has been removed from your order.
                '''))
        else:
            print(dedent(f'''
            You can only remove menu items you've already added!
            '''))
            selection = input('')
            order_something(selection, self)

    def display_order(self, order_status):
        if self.cart[order_status] > 1:
            string_one = ' orders of '
            string_two = ' have been added to your meal'
        else:
            string_one = ' order of '
            string_two = ' has been added to your meal'
        running_total = 0
        for section in ITEMS.keys():
            for elm in ITEMS[section]:
                if elm in self.cart:
                    running_total = running_total + (int(self.cart[elm]) * ITEMS[section][elm][0])

        string_three = self.cart[order_status]
        string_four = order_status
        ln_one = str(string_three) + str(string_one) + str(string_four) + str(string_two)
        ln_two = 'Your running total is ' + format_nums(running_total)

        print(dedent(f'''
            {'**' + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + ln_one + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + '**'}
            {'**' + (' ' * (((WIDTH - len(ln_two)) // 2)-2)) + ln_two + (' ' * (((WIDTH - len(ln_two)) // 2)-2)) + '**'}
        '''))

    def print_order(self):
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
        for elm in self.cart:
            for sections in ITEMS:
                if elm in ITEMS[sections]:
                    total_cost = total_cost + (self.cart[elm] * ITEMS[sections][elm][0])
                    ln_four = str(elm) + ' x' + str(self.cart[elm])
                    item_total_cost = self.cart[elm] * ITEMS[sections][elm][0]
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
        receipt = dedent(f'''
            {'-' * WIDTH}
            {ln_six + white_space_length_01 + ln_seven}
            {ln_eight + white_space_length_02 + ln_nine}
            {'-' * len(ln_eight)}
            {ln_ten + white_space_length_03 + ln_eleven}
            {'*' * WIDTH}
        ''')
        print(receipt)






current_id = None

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
def order_question(order_obj):
    ln_one = 'What would you like to order?'
    question = dedent(f'''
        {'*' * WIDTH}
        {'**' + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + ln_one + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + '**'}
        {'*' * WIDTH}
    ''')
    user_input = input(question)
    order_something(user_input, order_obj)


# This function calls the menu function and allows for the user to input a new command
def view_menu(order_obj):
    menu()
    selection = input('')
    order_something(selection, order_obj)


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
def view_order_total(order_obj):
    order_obj.print_order()
    selection = input('')
    order_something(selection, order_obj)


# This function removes a single item from the users current meal.
def remove_item(item_remove, order_obj):
    item_to_remove_placeholder = str(item_remove).split()[1::]
    item_to_remove = ' '.join(item_to_remove_placeholder)
    order_obj.remove_item(item_to_remove)
    view_order_total(order_obj)


# This function is the main user input handler.
def order_something(user_input, order_obj):
    user_input_placeholder = str(user_input).split()[0::]
    for i in range(len(user_input_placeholder)):
        user_input_placeholder[i] = user_input_placeholder[i].capitalize()

    cap_input = ' '.join(user_input_placeholder)
    if cap_input == 'Quit':
        exit()
        return
    elif cap_input == 'Menu':
        view_menu(order_obj)
        return
    elif cap_input == 'Order':
        view_order_total(order_obj)
        return
    elif cap_input == 'Repr':
        print(repr(order_obj))
        selection = input('')
        order_something(selection, order_obj)
        return
    elif cap_input.split()[0] == 'Remove':
        remove_item(cap_input, order_obj)
        return
    elif cap_input in ITEMS:
        view_category(cap_input)
        selection = input('')
        order_something(selection, order_obj)
        return
    elif cap_input is not int:
        for sections in ITEMS.keys():
            if cap_input in ITEMS[sections]:
                add_to_cart(cap_input, order_obj)
                return
        wrong_order(order_obj)
        return
            # except TypeError:
            #     quantity_error()
    else:
        wrong_order(order_obj)
        return


def add_to_cart(cap_input, order_obj):
    ordered_item = order_obj.add_item(cap_input)
    order_obj.display_order(ordered_item)
    selection = input('')
    order_something(selection, order_obj)


def quantity_error(order_obj):
    print(dedent('''
            Invalid quantity! Try again
        '''))
    selection = input('')
    order_something(selection, order_obj)

# This function displays when the user puts in an incorrect order
def wrong_order(order_obj):
    print(dedent('''
            Please order something off the menu!
        '''))
    selection = input('')
    order_something(selection, order_obj)


def out_of_stock(item_input, order_obj):
    print(dedent(f'''
    Sorry, we dont have enough {item_input} in stock! Try ordering less
    '''))
    selection = input(' ')
    order_something(selection, order_obj)

# This function displays when a single item has been added to the users meal order
def order_complete(order_status, order_obj):
    selection = input(' ')
    order_something(selection, order_obj)


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
                    global ITEMS
                    ITEMS = custom_menu
            except FileNotFoundError:
                print('File Not Found!')
                return check_menu()
    elif menu_input.lower() == '':
        return
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




# This is the main function handler
def run():
    greeting()
    check_menu()
    new_customer = Order()
    global current_id
    current_id = new_customer.id
    menu()
    order_question(new_customer)




if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print('Thanks for coming!')

