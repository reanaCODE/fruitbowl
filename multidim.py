def get_string(m):
    my_string = input(m)
    return my_string


def get_integer(message):
    my_integer = int(input(message))
    return my_integer


def double_loop_print(l):
    for i in range(0, len(l)):
        output = "{} : {}".format(i, l[i])
        print(output)
        for j in range(0, len(l[i])):
            output = "{} : {}".format(j, l[i][j])
            print(output)


def single_loop_print(l):
    for i in range(0, len(l)):
        output = "{:10} ---  {:10} --- {:<10}".format(l[i][0], l[i][1], l[i][2])
        print(output)


def print_with_indexes(l):
    for i in range(0, len(l)):
        output = "{:3} :  {:10}  {:10}  {:10}".format(i, l[i][0], l[i][1], l[i][2])
        print(output)

def loop_with_indexes(l):
    for i in range(0, len(l)):
        output = "{:3} ->  {:10}   {:<10}".format(i, l[i][0]. l[i][1]. l[i][2])
        print(output)

def create_new_entry(l):
    name = get_string("Please enter name: -> ")
    hair_colour = get_string("Please enter hair colour: -> ")
    age = get_integer("Please enter age: -> ")
    l.append([name, hair_colour, age])
    return None

def add_new_entry(l):
    print("Start Adding new entry.")
    name = get_string("Please enter the new name: -->")
    hair_colour = get_string("Please enter hair colour: -> ")
    age = get_integer("Please enter age: -> ")
    new_list = [name, hair_colour, age]
    l.append(new_list)


def main():
    my_l = [
        ["Alice", "Blond", 12],
        ["Cathy", "Blond", 15],
        ["Dan", "Black", 10],
        ["Bob", "Brown", 13],
        ["Joe", "Green", 13]
    ]

    # print (my_l)
    # double_loop_print(my_l)
    # single_loop_print(my_l)
    # print_with_indexes(my_l)
    add_new_entry(my_l)
    print_with_indexes(my_l)


main()
