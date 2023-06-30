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

def update_name(l):
    print_with_indexes(l)
    my_index = get_integer("Please enter the index number to update the name: -> ")
    new_name = get_string("Please enter the new name: ->")
    old_name = l[my_index][0]
    l[my_index][0] = new_name
    output_Message = "{} has now been changed to {}".format(old_name, new_name)
    print(output_Message)

def update_hair(l):
    print_with_indexes(l)
    my_index = get_integer("Please enter the index number to update the hair colour: -> ")
    new_hair = get_string("Please enter the new hair colour: ->")
    old_hair = l[my_index][1]
    l[my_index][1] = new_hair
    output_Message = "{} has now been changed to {}".format(old_hair, new_hair)
    print(output_Message)

def update_age(l):
    print_with_indexes(l)
    my_index = get_integer("Please enter the index number to update the age: -> ")
    new_age = get_string("Please enter the new age: ->")
    old_age = l[my_index][2]
    l[my_index][2] = new_age
    output_Message = "{} has now been changed to {}".format(old_age, new_age)
    print(output_Message)

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
    # add_new_entry(my_l)
    # print_with_indexes(my_l)
    update_name(my_l)
    update_hair(my_l)
    update_age(my_l)
    print_with_indexes(my_l)


main()
