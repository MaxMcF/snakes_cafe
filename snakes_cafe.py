from textwrap import dedent
import sys


WIDTH = 96
ITEMS = [
    {
    'section': 'Appetizers',
    'item': 'Wings',
    'item_selects': 0,
    },
    {
    'section': 'Appetizers',
    'item': 'Cookies',
    'item_selects': 0,
    },
    {
    'section': 'Appetizers',
    'item': 'Spring Rolls',
    'item_selects': 0,
    },
    {
    'section': 'Entrees',
    'item': 'Salmon',
    'item_selects': 0,
    },
    {
    'section': 'Entrees',
    'item': 'Steak',
    'item_selects': 0,
    },
    {
    'section': 'Entrees',
    'item': 'Meat Tornado',
    'item_selects': 0,
    },
    {
    'section': 'Entrees',
    'item': 'A Literal Garden',
    'item_selects': 0,
    },
    {
    'section': 'Desserts',
    'item': 'Ice Cream',
    'item_selects': 0,
    },
    {
    'section': 'Desserts',
    'item': 'Cake',
    'item_selects': 0,
    },
    {
    'section': 'Desserts',
    'item': 'Pie',
    'item_selects': 0,
    },
    {
    'section': 'Drinks',
    'item': 'Coffee',
    'item_selects': 0,
    },
    {
    'section': 'Drinks',
    'item': 'Tea',
    'item_selects': 0,
    },
    {
    'section': 'Drinks',
    'item': 'Blood of the Internet',
    'item_selects': 0,
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
]


def greeting():
    ln_one = 'Welcome to the Snakes Cafe!'
    ln_two = 'Please see our menu below.'
    ln_three = 'To quit at any time, type "quit"'

    print(dedent(f'''
        {'*' * WIDTH}
        {'**' + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + ln_one + (' ' * (((WIDTH - len(ln_one)) // 2)-1)) + '**'}
        {'**' + (' ' * (((WIDTH - len(ln_two)) // 2)-2)) + ln_two + (' ' * (((WIDTH - len(ln_two)) // 2)-2)) + '**'}
        {'**'}
        {'**' + (' ' * (((WIDTH - len(ln_three)) // 2)-2)) + ln_three + (' ' * (((WIDTH - len(ln_three)) // 2)-2)) + '**'}
        {'*' * WIDTH}
    '''))


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
                print(dedent(f'''
                    {ln_two}
                '''))


def order_question():
    ln_one = 'What would you like to order?'
    question = dedent(f'''
        {'*' * WIDTH}
        {'**' + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + ln_one + (' ' * (((WIDTH - len(ln_one)) // 2)-2)) + '**'}
        {'*' * WIDTH}
    ''')
    user_input = input(question)
    order_something(user_input)


def order_something(user_input):
    if str(user_input).lower() == 'quit':
        exit()
        return
    for menu_items in ITEMS:
        if menu_items['item'].lower() == str(user_input).lower():
            menu_items['item_selects'] += 1
            order_complete(menu_items)
        # elif :
        #     print(dedent('''
        #         Please order something off the menu!
        #     '''))
            # wrong_order()

# def wrong_order():
#     selection = input('')
#     order_something(selection)


def order_complete(order_status):
    if order_status['item_selects'] > 1:
        ln_one = ' orders of '
        ln_two = ' have been added to your meal'
    else:
        ln_one = ' order of '
        ln_two = ' has been added to your meal'
    ln_three = order_status['item_selects']
    ln_four = order_status['item']
    usable_line = str(ln_three) + str(ln_one) + str(ln_four) + str(ln_two)
    print(dedent(f'''
        {'**' + (' ' * (((WIDTH - len(usable_line)) // 2)-2)) + usable_line + (' ' * (((WIDTH - len(usable_line)) // 2)-2)) + '**'}
    '''))
    selection = input(' ')
    order_something(selection)


def exit():
    print(dedent('''
        Thanks you, come again!
    '''))
    sys.exit()


def run():
    greeting()
    menu()
    order_question()



if __name__ == '__main__':
    run()
