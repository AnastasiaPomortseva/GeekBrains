def make_sandwich(size, *toppings):
    """displays the composition of the sandwich"""
    print(f"Making a {size}-inch sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('smal','ham','salad')
make_sandwich('big','cheese','ham','tomato')