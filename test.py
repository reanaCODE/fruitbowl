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


#get_integer("Hello",0, 5)

def get_letter(m, letter_list):
    getting_letter = True
    while getting_letter is True:
        letter = input(m).upper().strip()
        if letter not in letter_list:
            print("not a correct letter")
        else:
            return letter

get_letter("Please choose letter (Y/N): ", ["Y", "N"])

