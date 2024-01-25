product_and_price_dict = {}
product_and_price_dict['Condom'] = 10
product_and_price_dict['Snack'] = 3
product_and_price_dict['PS5'] = 100
product_and_price_dict['Honey'] = 16
print(product_and_price_dict)
def print_dictionary():
    for product_names, values in product_and_price_dict.item():
        print(f'{product_names}: {values}')
def add_word():
    product_names = input('Enter product name: ')
    values = int(input('Enter price: '))
    if product_names in product_and_price_dict:
        print(f'{product_names} is already in the dictionary')
    else:
        product_and_price_dict[product_names] = values
        print(f'Added {product_names} to the dictionary')
        print(product_and_price_dict)
def edit_word():
    product_names = input('Enter a product name: ')
    values = int(input('Enter a price: '))
    if product_names not in product_and_price_dict:
        print(f'{product_names} is not in the dictionary')
    else:
        product_and_price_dict[product_names] = values
        print(f'Updatedd {product_names} to the dictionary')
        print(product_and_price_dict)
def delete_word():
    product_names = input('Enter a current product name to delete: ')
    if product_names not in product_and_price_dict:
        print(f'{product_names} is not in the dictionary')
    else:
        product_and_price_dict.pop(product_names)
        print(f'{product_names} is removed')
        print(product_and_price_dict)
def print_menu():
    print('ENGLISH - VIETNAMESE DICTIONARY')
    print('1. Show all products')
    print('2. Add new product')
    print('3. Edit price')
    print('4. Delete a product')
    print('5. Quit')

### Main program ###
running = True
while running:
    print_menu()
    choice = int(input('Enter your choices: '))
    if choice == 1:
        print_dictionary()
    elif choice == 2:
        add_word()
    elif choice == 3:
        edit_word()
    elif choice == 4:
        delete_word()
    elif choice == 5:
        running = False
    else:
        print('Invalid choice')