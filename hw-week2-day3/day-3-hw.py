#EXERCISE 1) Build a Shopping Cart
#You can use either lists or dictionaries. The program should have the following capabilities:

#1) Takes in input
#2) Stores user input into a dictionary or list
#3) The User can add or delete items
#4) The User can see current shopping list
#5) The program Loops until user 'quits'
#6) Upon quiting the program, print out all items in the user's list


# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

cart = {}

def store_user_info(product, amount):
    cart[product] = amount
    
def main():
    #step 3
    while True:
        #step 4
        product = input("What Item do you want to add?")
        amount = input("How many of that Item?")
        #step 6
        store_user_info(product, amount)
        
        shop_list = input("Want to see Shoping Cart? (y/n)")

        if shop_list == 'y':
            print(cart)

        cont = input("Would you like to continue (y/n)?")
        
        #step 5 
        if cont == 'n':
            #step 5b
            break
    #step 5a
    print(cart)

main()

