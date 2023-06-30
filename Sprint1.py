def get_integer(n):
    user_input = int(input(n))
    return user_input


def get_string(n):
    user_input = input(n)
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


def main():
    fruit_list = [
        ["Apples", 2],
        ["Pears", 8],
        ["Oranges", 3],
        ["Lemons", 7]
    ]
    menu_list = [
        ["R", "Reveiw Fruit"],
        ["Q", "Quit"]
    ]

    run_program = True
    while run_program:
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        user_choice = get_string("Please select an option: -> ")
        if user_choice == "R":
            reveiw_fruit(fruit_list)
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry")
    print("Thank you, the program has ended")


if __name__ == "__main__":
    main()
