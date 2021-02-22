from funcs import has_raw_materials, collect_money, has_enough_money, bake_cupcake, stats, add_needed_ingredients
from data import CUPCAKE_CHOICES, raw_materials

CHOICES = ('rainbow', 'salted caramel', 'dark cherry', 'bacon bourbon', 'stats', 'shutdown')
SPEND_POINT_YES = ('Y', 'y')
SPEND_POINT_NO = ('N', 'n')
SHUTDOWN_PASSWORD = '101010'
machine_active = True
SECRET_POINTS = 0

while machine_active:
    valid_choice = False
    choice = input('ORDER [rainbow - salted caramel - dark cherry - bacon bourbon]: ')
    if choice in CHOICES:
        valid_choice = True
    else:
        print('That is not a valid selection...\n')
    if choice == 'shutdown':
        entered_password = input('ENTER SHUTDOWN PASSWORD: ')
        if entered_password == SHUTDOWN_PASSWORD:
            machine_active = False
        else:
            print('YOU ARE NOT AUTHORIZED TO DISABLE THIS MACHINE!\n')
    elif choice == 'stats':
        stats_ = stats(raw_materials)
        print(stats_)
    elif valid_choice:
        selection = CUPCAKE_CHOICES[choice]
        has_enough_raw_materials = has_raw_materials(selection['ingredients'], raw_materials)
        if not isinstance(has_enough_raw_materials, bool):
            print(has_enough_raw_materials)
            if SECRET_POINTS >= 1:
                spend_point = input('Would you like to spend 1 secret point to add more ingredients? Enter Y or N.')
                if spend_point in SPEND_POINT_YES:
                    add_needed_ingredients_now = add_needed_ingredients(selection['ingredients'], raw_materials)
                    if isinstance(add_needed_ingredients_now, str):
                        print(add_needed_ingredients_now)
                    SECRET_POINTS -= 1
                    selection = CUPCAKE_CHOICES[choice]
                    has_enough_raw_materials = has_raw_materials(selection['ingredients'], raw_materials)
                elif spend_point in SPEND_POINT_NO:
                    machine_active = False
                else:
                    print('That is not a valid selection...\n')
            else:
                machine_active = False
        if isinstance(has_enough_raw_materials, bool):
            print('A {0} cupcake costs {1:.2f}'.format(choice, selection['price']))
            quarters = input('Quarters: ')
            dimes = input('Dimes: ')
            nickels = input('Nickels: ')
            money = collect_money(100.00, quarters, dimes, nickels)
            if not isinstance(money, float):
                print(money)
            else:
                change = has_enough_money(money, selection['price'])
                if change == 'Insufficient funds...  Dispensing coins inserted.\n':
                    print(change)
                else:
                    cupcake = bake_cupcake(choice, selection['ingredients'], raw_materials)
                    print(cupcake)
                    print(change)
                    if isinstance(change, str):
                        SECRET_POINTS += 1
        else:
            machine_active = False

print('We are going down for maintenance...')
