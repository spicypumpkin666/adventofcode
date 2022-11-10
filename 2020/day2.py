import logging as log

log.basicConfig(level=log.DEBUG)

data = open("day2.txt").readlines()
passwords = [line.strip() for line in data]

def check_valid_passwords_count(passwords):
    valid = 0

    for line in passwords:
        print(line)
        key, value = line.split(': ')
        k, letter = key.split(" ")
        lower, upper = k.split('-')

        if int(lower) <= value.count(letter) <= int(upper):
            valid += 1

    log.info(f"valid count: {valid}")

    return valid

def check_valid_passwords_positions(passwords):
    valid = 0

    for line in passwords:
        print(line)
        key, value = line.split(': ')
        k, letter = key.split(" ")
        lower, upper = k.split('-')
        lower = int(lower) - 1
        upper = int(upper) - 1

        if value[lower] == letter:
            if value[upper] != letter:
                valid += 1
        elif value[upper] == letter:
            if value[lower] != letter:
                valid += 1

    log.info(f"valid count: {valid}")

    return valid

print(check_valid_passwords_positions(passwords))