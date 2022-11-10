
expenses = []

with open("day1.txt", "r") as f:
    for line in f:
        expenses.append(int(line.strip('\n')))

def sum_expenses(expenses):

    for i in expenses:
        for e in expenses:
            if i + e == 2020:
                return i*e

# print(sum_expenses(expenses))

def sum_three_expenses(expenses):
    for x in expenses:
        for y in expenses:
            for z in expenses:
                if x + y + z == 2020:
                    return x*y*z

print(sum_three_expenses(expenses))
