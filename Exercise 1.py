#Exercise 1
temp = int(input('Enter temperature: '))
unit = input('Enter unit of temperature: ')
def convert_temperature(temp, unit):
    if unit == 'C':
        f = temp * (9/5) + 32
        return f
    elif unit == 'F':
        c = (temp - 32) * (5/9)
        return c
    else:
        return 'Error 404'
if unit == 'c':
    unit_2 = 'F'
else:
    unit_2 = 'C'
n = convert_temperature(temp, unit)
print(f'{temp} {unit} = {n} {unit_2}')