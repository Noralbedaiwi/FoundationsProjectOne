####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "N20"#complete me!
signature_flavors = ['tuna' , 'salmon']#complete me!
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print("Our menu: ")
    for item in menu:
        print('-"%s" (%s KD)' % (item, menu[item]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print()
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for item in original_flavors:
        print("- \"%s\" " % item)



def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for item in signature_flavors:
        print("- \"%s\" " % item)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    return order.lower() in menu or order.lower() in original_flavors or order.lower() in signature_flavors


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    order_list = []
    order = input("What's your order? (Enter the exact spelling of the item you want. Type 'Exit' to end your order.)\n")
    while order.lower() != "exit":
        if is_valid_order(order):
            order_list.append(order)
        order = input()

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for item in order_list:
        item = item.lower()
        if item in menu:
            total += menu[item]
        elif item in original_flavors:
            total += original_price
        elif item in signature_flavors:
            total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for order in order_list:
        print("- %s " % order)

    print()
    price = get_total_price(order_list)
    print("That'll be KD %s" % price)
    if accept_credit_card(price):
        print("This order is eligible for credit card payment.")

    print("Thank you for shopping at %s" % cupcake_shop_name)




