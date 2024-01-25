#Exercise 2:
#1.
customers = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Mike', 'John']
tickets = [15, 23, 7, 12, 6, 10, 20]
found_pos = -1
name = input('Enter name: ')
for i in range(len(customers)):
    if customers[i] == name:
        print(f'Your number is {tickets[i]}')
#2.
m = tickets[0]
max_pos = 0
for i in range(1, len(tickets)):
    if tickets[i] > m:
        m = tickets[i]
        max_pos = i
print(f'Customer that bought the most number of tickets is {customers[max_pos]}: {tickets[max_pos]}')
#3.
count = 0
a = 0
for i in tickets:
  a += i
avg = a / len(tickets)
for j in tickets:
  if j > avg:
    count += 1
print(f'Average number of tickets is: {avg}')
print(f'Number of customers that number of tickets they bought are greater than the average number of tickets: {count}')