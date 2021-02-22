total_money_collected = 0


def has_raw_materials(f_raw_materials, d_raw_materials):
    """Check if there are enough raw materials in the machine

    Params:
        f_raw_materials: dict
        d_raw_materials: dict

    Returns:
        str or bool
    """
    additional_resources_needed = ''
    for f_raw_material in f_raw_materials:
        if f_raw_materials[f_raw_material] > d_raw_materials[f_raw_material]:
            additional_resources_needed += 'Machine Needs Additional: {0}\n'.format(f_raw_material)
    if additional_resources_needed:
        return additional_resources_needed
    else:
        return True


def add_needed_ingredients(f_raw_materials, d_raw_materials, f_secret_points):
    """ Check for missing ingredients and add them in.

    Params:
        f_raw_materials: dict
        d_raw_materials: dict

    Returns:
        str, int
    """
    f_secret_points -= 1
    for f_raw_material in f_raw_materials:
        if f_raw_materials[f_raw_material] > d_raw_materials[f_raw_material]:
            d_raw_materials[f_raw_material] += f_raw_materials[f_raw_material]
    return 'The elves have restocked the machine. You have {0} secret points left.'.format(f_secret_points), \
           f_secret_points


def collect_money(f_max_value, f_quarters, f_dimes, f_nickels):
    """Collect money into the machine

    Params:
        f_max_value: float

    Returns:
        float or str
    """
    try:
        money_collected = int(f_quarters) * 0.25
        money_collected += int(f_dimes) * 0.10
        money_collected += int(f_nickels) * 0.05
        if money_collected >= f_max_value:
            return 'Machine can\'t hold more than ${0:.2f}...  Dispensing coins inserted.'.format(f_max_value)
        else:
            return money_collected
    except ValueError:
        return 'Please enter valid currency.\n'


def has_enough_money(f_money_collected, f_cupcake_price, f_secret_points, f_total_money_collected):
    """Check to see if customer put in enough money into the machine

    Params:
        f_money_collected: float
        f_cupcake_price: float

    Returns:
        str, int
    """
    # global total_money_collected
    if f_money_collected > f_cupcake_price:
        excess_money_collected = round(f_money_collected - f_cupcake_price, 2)
        f_total_money_collected += f_cupcake_price
        return 'Change: ${0:.2f}\n'.format(excess_money_collected)
    elif f_money_collected == f_cupcake_price:
        f_total_money_collected += f_cupcake_price
        f_secret_points += 1
        return 'You\'ve earned one secret point. Total secret points: {0}'.format(f_secret_points), f_secret_points, \
               f_total_money_collected
    else:
        return 'Insufficient funds...  Dispensing coins inserted.\n'


def bake_cupcake(f_cupcake_choice, f_raw_materials, d_raw_materials):
    """Bake cupcake from raw materials

    Params:
        f_cupcake_choice: str
        f_raw_materials: dict
        d_raw_materials: dict

    Returns:
        str
    """
    for f_raw_material in f_raw_materials:
        d_raw_materials[f_raw_material] -= f_raw_materials[f_raw_material]
    return 'A {0} cupcake has been dispensed!'.format(f_cupcake_choice)


def stats(d_raw_materials, f_secret_points, f_total_money_collected):
    """
    Show machine statistics

    Params:
        d_raw_materials: dict

    Returns:
        str
    """
    cm_stats = 'sugar {0} tablespoons remaining\n'.format(d_raw_materials['sugar'])
    cm_stats += 'butter {0} teaspoons remaining\n'.format(d_raw_materials['butter'])
    cm_stats += 'dark chocolate {0} tablespoons remaining\n'.format(d_raw_materials['dark chocolate'])
    cm_stats += 'caramel {0} tablespoons remaining\n'.format(d_raw_materials['caramel'])
    cm_stats += 'light corn syrup {0} teaspoons remaining\n'.format(d_raw_materials['light corn syrup'])
    cm_stats += 'sweetened condensed milk {0} teaspoons remaining\n'.format(d_raw_materials[
        'sweetened condensed milk'])
    cm_stats += 'vanilla extract {0} teaspoons remaining\n'.format(d_raw_materials['vanilla extract'])
    cm_stats += 'sprinkles {0} tablespoons remaining\n'.format(d_raw_materials['sprinkles'])
    cm_stats += 'bing cherries {0} tablespoons remaining\n'.format(d_raw_materials['bing cherries'])
    cm_stats += 'candied bacon {0} tablespoons remaining\n'.format(d_raw_materials['candied bacon'])
    cm_stats += 'bacon infused bourbon {0} tablespoons remaining\n'.format(d_raw_materials['bacon infused bourbon'])
    cm_stats += 'sea salt {0} tablespoons remaining\n'.format(d_raw_materials['sea salt'])
    cm_stats += 'Total Money Collected: ${0:.2f}\n'.format(f_total_money_collected)
    cm_stats += 'Total secret points earned: {0}'.format(f_secret_points)
    return cm_stats
