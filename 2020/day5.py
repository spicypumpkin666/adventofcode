import logging as log

log.basicConfig(level=log.DEBUG)

r = open('day5.txt').read().strip('\n')
seats = r.splitlines()

def get_row(row):
    low_row = 0
    high_row = 127
    i = 0

    while True:
        if row[i] == 'F':
            if low_row == 0:
                high_row = round(high_row / 2) - 1
            else:
                high_row = (round((high_row - low_row) / 2) - 1) + low_row
        elif row[i] == 'B':
            if low_row == 0:
                low_row = round(high_row / 2)
            else:
                low_row = (round((high_row - low_row) / 2)) + low_row
        if high_row - low_row == 1:
            if row[i+1] == 'F':
                return low_row
            elif row[i+1] == 'B':
                return high_row
        i += 1


def get_column(col):
    seats = [0,1,2,3,4,5,6,7]
    r = int(len(seats) / 2)
    i = 0

    while True:
        if r == 1:
            if col[i] == 'R':
                return seats[1]
            elif col[i] == 'L':
                return seats[0]

        if col[i] == 'R':
            seats = seats[r:]
        if col[i] == 'L':
            seats = seats[:r]

        r = int(r / 2)
        i += 1

filled_seats = []

def get_highest_seat_ID():

    highest = 0
    for seat in seats:
        row = get_row(seat[:8])
        col = get_column(seat[-3:])
        seat_id = (row * 8) + col
        filled_seats.append(seat_id)
        if seat_id > highest:
            highest = seat_id
    return highest

log.info((f'the highest seat is {get_highest_seat_ID()}'))

def find_missing_seat(filled_seats):
    return sorted(set(range(filled_seats[0], filled_seats[-1])) - set(filled_seats))

log.info(f'the missing seat is {find_missing_seat(filled_seats)}')