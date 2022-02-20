# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

class ShoppingCart():
    # defines options menu for the user to use
    def chooseOption(self):
        action = input(
                'Please choose from the following options:\n'
                '\t(A)dd    - Adds an item to your cart.\n'
                '\t(R)emove - Removes an item from the cart.\n'
                '\t(S)how   - Shows all items in cart.\n'
                '\t(Q)uit   - Quit and print out shopping list\n'
                'Option > '
                )
        return action

    # asks for item to add to cart
    def getItem(self):
        item = input(
                '\n'
                '(O) to return to Options or add another item.\n'
                'What would you like to ADD to your cart? '
            )
        return item

    # function to ask for an item to remove
    def removeItem(self):
        removed_item = input(
            '\n'
            '(O) to return to Options or remove another item.\n'
            'What item would you like to REMOVE from your cart? '
            )
        return removed_item


    def shoppingCartExpress(self):
        # nice little banner
        print(
        '       _\n'
        '    \________       Welcome\n'
        ' ~   \######/         to the\n'       
        '  ~   |####/            Shopping Cart\n'
        ' ~    |____.              Express\n'
        '______o____o_____ \n'
        'Create a Shopping List\n'
        )

        # empty string for items in cart
        cart_items = []
        # blank action value


        # program brains
        while True:
            
            # asks user to choose an option and sets it equal to action
            option = ShoppingCart.chooseOption(self)

            # prints the list
            if option.lower() == 's':
                if not cart_items: # print another message if the list is empty
                    print(
                        '\n'
                        '--- Nothing in cart, please add items. ---'
                        '\n'
                        )
                else:
                    print('______________')
                    print(
                        'Shopping List: \n',
                        #*cart_items, sep = "\n"
                    )
                    for x in range(len(cart_items)):
                        print(f"-{cart_items[x].title()}")
                    print('____________________')
            # add option
            elif option.lower() == 'a':
                temp_item = ''
                while temp_item != 'o': # argument to keep repeating as long as item entered isn't 'O'
                    temp_item = ShoppingCart.getItem(self)
                    if temp_item in cart_items:
                        print(
                            '\n'
                            '--- Item already in cart, please enter a new option. ---' # could build out later to include an option to enter another item
                            '\n'
                            )
                    elif temp_item == '': # deals with user not entering anything
                        print(
                            '\n'
                            '--- Please enter an item to ADD. ---'
                            )
                    else:
                        cart_items.append(temp_item.strip()) # added strip to remove extra spaces before and after item entered
                cart_items.remove('o') # removes the 'o' that is entered before heading to options menu
            # remove option
            elif option.lower() == 'r':
                temp_remove = ''
                while temp_remove != 'o': # argument to keep repeating as long as item entered isn't 'O'
                    temp_remove = ShoppingCart.removeItem(self)
                    if temp_remove in cart_items:
                        cart_items.remove(temp_remove.strip()) # added strip to remove extra spaces before and after item entered
                    elif temp_remove == '': # deals with user not entering anything
                        print(
                            '\n'
                            '--- Please enter an item to REMOVE. ---'
                            )
                    else:
                        print(
                            '\n'
                            '--- Item not in cart, please enter a new option. ---' # could build out later to include an option to enter another item
                            '\n'
                            )
            elif option.lower() == 'q':
                print('______________')
                print(
                    'Shopping List: \n',
                        #*cart_items, sep = "\n"
                )
                for x in range(len(cart_items)):
                    print(f"-{cart_items[x].title()}")
                print(
                    '\n'
                    '_______________________________________________________\n'
                    'Thank you for using this app, enjoy your shopping trip!'
                    )
                break

run = ShoppingCart()
run.shoppingCartExpress()