import random


def get_integer(m, lower, upper):
    getting_integer = True
    while getting_integer is True:
        try:
            user_input = int(input(m))
        except ValueError:
            print("Please enter an integer")
            continue
        if user_input > upper or user_input < lower:
            print("Please enter a valid value")
        else:
            return user_input


def get_string(m):
    user_input = input(m)
    return user_input


def get_option(m):
    get_letter = True
    while get_letter is True:
        user_input = input(m).upper().strip()
        if len(user_input) != 1:
            print("One character needed")
        elif user_input.isdigit():
            print("I need a letter please try again")
        else:
            return user_input


def reveiw_fruit(l):
    for x in l:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)
    return None


def print_list_index(l):
    for i in range(0, len(l)):
        print("{} : {}".format(i, l[i]))
        # prints list with index numbers
    print("-" * 100)


def change_value(l):
    print("-" * 100)
    print_list_index(l)
    index_num = get_integer("Please choose the index number: --> ", 0, len(l) - 1)
    new_value = get_integer("Please enter new quantity: -->", 0, 10)
    old_value = l[index_num][1]
    l[index_num][1] = new_value
    output = "The old quantity of {} is now changed to {}".format(old_value, new_value)
    print(output)


def add_fruit(l):
    print("-" * 100)
    add_new = get_string("Please enter new fruit: ")
    add_numbers = get_integer("Please enter amount of this fruit: ", 0, 10)
    output = "You have added {} and the quantity is {}".format(add_new, add_numbers)
    print(output)
    l.append([add_new, add_numbers])
    # user adds a new fruit to list
    print("-" * 100)


def shuffle_list(l):
    random.shuffle(l)


# remove item in list
# find item in list


def main():
    fruit_list = [
        ["Apples", 2],
        ["Pears", 8],
        ["Oranges", 3],
        ["Lemons", 7]
    ]
    menu_list = [
        ["R", "Reveiw Fruit"],
        ["Q", "Quit"],
        ["V", "Change Value"],
        ["A", "Add Fruit"],
        ["S", "Shuffle List"]
    ]

    run_program = True
    while run_program:
        print("-" * 100)
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        print("-" * 100)
        user_choice = get_option("Please select an option: -> ")
        if user_choice == "R":
            reveiw_fruit(fruit_list)
        elif user_choice == "Q":
            run_program = False
        elif user_choice == "V":
            change_value(fruit_list)
        elif user_choice == "A":
            add_fruit(fruit_list)
        elif user_choice == "S":
            shuffle_list(fruit_list)
        else:
            print("Unrecognised entry")
    print("Thank you, the program has ended")


if __name__ == "__main__":
    main()
