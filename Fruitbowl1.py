# Amy has a large bowl of fruit at home
# It currently contains 5 Apples, 7 Pears, 2 Mangoes, 9 KiwiFruit and 3 Peaches
# Amy would like a program designed so that she can monitor the consumption of her fruit
# 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
def add_to_fruit_bowl():
    return None


def reveiw_fruit(l):
    for x in l:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)
    return None


def main():
    fruit_list = (
        ("Apples", 2),
        ("Pears", 8),
        ("Oranges", 3),
        ("Lemons", 7)
    )
    reveiw_fruit(fruit_list)
    return None


main()
