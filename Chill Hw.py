#For "Pizza": Ask for the size ("Small", "Medium", "Large").
#For "Burger": Ask if the customer wants cheese ("Yes" or "No").
#For "Salad": Ask for the type of dressing ("Italian", "Ranch", "Caesar").

def pizza():
    found_pos = -1
    cost = 0
    size_list = ['small', 'medium', 'large']
    cash = [25, 30, 45]
    size = input('Which size do you want: ')
    number = int(input('How many: '))
    for i in range(len(size_list)):
        if  size_list[i] == size:
            found_pos = i
        else:
            print('Invalid')
    cost = cash[found_pos] * number
    print(number, size_list[i], 'pizza')
    print(f' Total cost is {cost}')

def burger():
    cash = 0
    cheese = input('Do you want cheese:(y/n) ')
    if cheese == 'y':
        cash = 15
    elif cheese == 'n':
        cash = 10
    else:
        print('Invalid')
    cost = cash
    print(f' Total cost is {cost}')

def salad():
    cost = 0
    number = int(input('How many number? '))
    dressing = input('Which type of dressing:("Italian", "Ranch", "Caesar") ')
    if dressing == 'Italian':
        cash = 15
    elif dressing == 'Ranch':
        cash = 17
    elif dressing == 'Caesar':
        cash = 19
    else:
        print('Invalid')
    cost = cash * number
    print(f' Total cost is {cost}')

def main():
    running = True
    while running:
        choice = int(input('What would you like to order: '))
        if choice == 1:
            pizza()
        elif choice == 2:
            burger()
        elif choice == 3:
            salad()
        elif choice == 4:
            running = False
        else:
            print('Invalid choice!')

main()