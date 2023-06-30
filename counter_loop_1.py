#loops
#loops are repeated actions (iterations)

# loop with a counter (will run a certain number of times)
def  loop_with_counter():
    c = 0
    while c  <  10:
        print(      "hello c is {}".format(c)   )     
        #increment c
        c += 1
    return None

# indefinite loop
def indefinite_loop():
    run = True
    while run == True:
        user_choice = input("Press n to stop the loop \n or anything else to stay in it: ")
        if user_choice == "n":
            print("loop stopped")
            run = False
        else:
           print("You are still in the loop")

#loop_with_counter()
indefinite_loop()
