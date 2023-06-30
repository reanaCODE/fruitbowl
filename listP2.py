# lists=data structure
# lists have index number, the first item is always #0
# len= numbers onf index numbers in list
# might want to access an item, might want to print a list, add smt to list (end, place?), remove smt from list
# might want to update an item/change, might want to sort list
# access an item at an index
import random


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
    # user searches for a name via index number
    print(output)
    print("-" * 100)


def print_list(l):
    for x in l:
        print(x)
        # prints list
    print("-" * 100)


def print_list_index(l):
    for i in range(0, len(l)):
        print("{} : {}".format(i, l[i]))
        # prints list with index numbers
    print("-" * 100)


def add_item(l):
    new_item = get_string("Please enter new name: ")
    # user adds a new name to list
    l.append(new_item)
    print("-"*100)


def find_item(l):
    item = get_string("Who do you want to find? -->")
    # system asking user to input the name they want to find and prints out index number
    if item in l:
        index_num = l.index(item)
        output = "{} has been found and is at index number {}".format(l[index_num], index_num)
        print(output)
    else:
        print("{} is not in the list".format(item))
    print("-"*100)


def remove_item(l):
    item = get_string("Who do you want to remove? --> ")
    # if user wants to remove a name from list this will delete said name/value they want to remove
    if item in l:
        l.remove(item)
        output = "{} has been removed from the list".format(item)
        print(output)
    else:
        print("{} could not be found".format(item))
    print("-"*100)


def sort_list(l):
    l.sort()
    # ????? IDK what this does - find out

def shuffle_list(l):
    random.shuffle(l)
    # shuffles the list so the names/values have a new order and index numbers


def change_value(l):
    # print menu so user has index numbers
    print_list_index(l)
    index_num = get_integer_input("Please choose the index number: --> ")
    new_value = get_string("Please enter new name: -->")
    # we now have all the values we need
    # temporarily hold value for print out
    # runs if user wants to replace one name in the list with another
    old_value = l[index_num]
    # update value
    l[index_num] = new_value
    # confirmation message
    output = "The old value of {} is now changed to {}".format(old_value, l[index_num])
    print(output)


def menu():
    # prints menu/list/options which are presented to user and goes into loop until they choose the 'quit' option
    my_list = ["May", "Pasty", "Jean", "Costantino", "Parra"]
    print("my_list is currently set to: {}".format(my_list))
    my_menu = '''
    A: print the list
    B: print the list with indices 
    C: add item to list
    D: print at index number 
    E: change value in the list
    F: find item in list
    G: remove item from list
    H: sort list
    I: shuffle list
    Q: quit
    '''
    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please select you option: --> ").upper()
        print("-" * 100)
        if choice == "A":
            print_list(my_list)
        elif choice == "B":
            print_list_index(my_list)
        elif choice == "C":
            add_item(my_list)
        elif choice == "D":
            print_at_index(my_list)
        elif choice == "E":
            change_value(my_list)
        elif choice == "F":
            find_item(my_list)
        elif choice == "G":
            remove_item(my_list)
        elif choice == "H":
            sort_list(my_list)
        elif choice == "I":
            shuffle_list(my_list)
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
