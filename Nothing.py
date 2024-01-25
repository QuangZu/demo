student_names = ['Huy', 'Quang', 'Huy Anh', 'Phan Anh']
grades = [4.5, 5, 4, 2.5]

def add_student():
    student_name = input('Enter a student name: ')
    grade = float(input(('Enter a grade: ')))
    if student_names in student_names:
        print(f'{student_names} is already in the system')
        return
    student_names.append(student_name)
    grades.append(grade)

def show_student():
    for i in range(len(student_names)):
        print(f'{i+1}. {student_names[i]}: {grades[i]}')

def edit_grade():
    student_name = input('Enter student name: ')
    grade = int(input('Enter grade : '))
    if student_name not in student_names:
        print(f'{student_name} is not in the list.')
    else:
        grades[student_names.index(student_name)] = grade

def search_student():
    student_name = input('Enter student name: ')
    if student_name in student_names:
        pos_found = student_names.index(student_name)
        print(f'{student_name}: {grades[pos_found]}')
    else:
        print(f'{student_name} is not in the list.')

def print_menu():
    print('PRODUCT MANAGEMENT')
    print('1. Add student')
    print('2. Show all students')
    print('3. Edit grade')
    print('4. Search student')
    print('5. Quit')

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_student()
        elif choice == 2:
            show_student()
        elif choice == 3:
            edit_grade()
        elif choice == 4:
            search_student()
        elif choice == 5:
            running = False
        else:
            print('Invalid choice!')
