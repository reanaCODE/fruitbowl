# lists=data structure
# lists have index number, the first item is always #0
# len= numbers onf index numbers in list
# might want to access an item, might want to print a list, add smt to list (end, place?), remove smt from list
# might want to update an item/change, might want to sort list
# access an item at an index


def get_integer_input(m):
    my_input = int(input(m))
    # the function terminates when a return is called
    return my_input


def get_string(m):
    my_input = input(m)
    # the function terminates when a return is called
    return my_input


def print_at_index(l):
    my_index = get_integer_input("Please enter index number: -> ")
    output = "The value -- {} -- is at index {} in the list".format(l[my_index], my_index)
    print(output)
    print("-" * 100)


def print_list(l):
    for x in l:
        print(x)
    print("-" * 100)


def print_list_index(l):
    for i in range(0, len(l)):
        print("{} : {}".format(i, l[i]))
    print("-" * 100)


def add_item(l):
    new_item = get_string("Please enter new name: ")
    l.append(new_item)
    print("-"*100)


def menu():
    my_list = ["May", "Pasty", "Jean",
               "Costantino", "Parra"]
    my_menu = '''
    A: print the list
    B: print the list with indices 
    C: add item to list
    D: print at index number 
    Q: quit
    '''
    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please select you option: --> ")
        print("-" * 100)
        if choice == "A":
            print_list(my_list)
        elif choice == "B":
            print_list_index(my_list)
        elif choice == "C":
            add_item(my_list)
        elif choice == "D":
            print_at_index(my_list)
        elif choice == "Q":
            print("Thank You")
            print("-"*100)
            run = False
        else:
            print("-ERROR- This input is invalid, please try again")
            print("-"*100)


menu()

# prints list
# print_list_index(my_list)
# adding a name through the program into list
# my_list.append("Damian")
# adding a name chosen from the user
# add_item(my_list)
# prints list again to see what has changed
# print_list_index(my_list)
