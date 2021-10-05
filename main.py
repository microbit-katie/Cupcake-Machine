from funcs import has_raw_materials, collect_money, has_enough_money, bake_cupcake, stats, add_needed_ingredients
from data import CUPCAKE_CHOICES, raw_materials
from microbit import *
import neopixel
from random import randint
from ssd1306 import initialize, clear_oled, command
from ssd1306_text import add_text
import gc

CHOICES = ('rainbow', 'salted caramel', 'dark cherry', 'bacon bourbon', 'stats', 'shutdown')
SPEND_POINT_YES = ('Y', 'y')
SPEND_POINT_NO = ('N', 'n')
SHUTDOWN_PASSWORD = '101010'
machine_active = True
secret_points = 0
total_money_collected = 0
image = Image("08880\n"
              "88888\n"
              "88888\n"
              "55555\n"
              "55555\n")
np = neopixel.NeoPixel(pin1, 10)
initialize()
clear_oled()
display.show(image)

while machine_active:
    gc.collect()
    speaker.off()
    audio.play(Sound.HAPPY)
    for pixel_id in range(0, len(np)):
        red = randint(0, 60)
        green = randint(0, 60)
        blue = randint(0, 60)
        np[pixel_id] = (red, green, blue)
        np.show()
        sleep(100)
    add_text(0, 0, 'Cupcake Game!')
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
        stats_ = stats(raw_materials, secret_points, total_money_collected)
        print(stats_)
    elif valid_choice:
        selection = CUPCAKE_CHOICES[choice]
        has_enough_raw_materials = has_raw_materials(selection['ingredients'], raw_materials)
        if not isinstance(has_enough_raw_materials, bool):
            print(has_enough_raw_materials)
            if secret_points >= 1:
                spend_point = input('Would you like to spend 1 secret point to add more ingredients? Enter Y or N: ')
                if spend_point in SPEND_POINT_YES:
                    add_needed_ingredients_now, secret_points = add_needed_ingredients(selection['ingredients'],
                                                                                       raw_materials,
                                                                                       secret_points)
                    if isinstance(add_needed_ingredients_now, str):
                        print(add_needed_ingredients_now)
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
                change, secret_points, total_money_collected = has_enough_money(money, selection['price'],
                                                                                secret_points, total_money_collected)
                if change == 'Insufficient funds...  Dispensing coins inserted.\n':
                    print(change)
                else:
                    cupcake = bake_cupcake(choice, selection['ingredients'], raw_materials)
                    print(cupcake)
                    print(change)
        else:
            machine_active = False

print('We are going down for maintenance...')
