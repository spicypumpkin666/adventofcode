import logging as log
import re

log.basicConfig(level=log.DEBUG)

r = open('day4.txt').read()
input_ = r.split('\n\n')
input_ = [line.replace('\n', ' ') for line in input_]

REQ_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = []
for line in input_:
    passport = {}
    for field in line.split():
        key, value = field.split(':')
        passport[key] = value
    if not REQ_FIELDS - passport.keys():
        passports.append(passport)

log.info(f"valid ppt: {len(passports)}")

eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def make_check(passport):
    valid = 0
    if 1920 <= int(passport['byr']) <= 2002:
        valid += 1
    if 2010 <= int(passport['iyr']) <= 2020:
        valid += 1
    if 2020 <= int(passport['eyr']) <= 2030:
        valid += 1
    if passport['hgt']:
        if passport['hgt'][-2:] == 'cm':
            try:
                if 150 <= int(passport['hgt'][:3]) <= 193:
                    valid += 1
            except ValueError:
                pass
        elif passport['hgt'][-2:] == 'in':
            try:
                if 59 <= int(passport['hgt'][:2]) <= 76:
                    valid += 1
            except ValueError:
                pass
    pattern1 = re.compile("#([a-f][0-9]+)")
    pattern2 = re.compile("#([a-f]+)")
    pattern3 = re.compile("#([0-9]+)")
    if pattern1.match(passport['hcl']) or pattern2.match(passport['hcl']) or pattern3.match(passport['hcl']):
        valid += 1
    if passport['ecl'] in eyes:
        valid += 1
    if len(passport['pid']) == 9:
        if int(passport['pid']):
            valid += 1

    if valid == 7:
        return True
    return False

total = 0

for passport in passports:
    if make_check(passport):
        total += 1
    else:
        log.info(f'invalid ppt {passport}')

log.info(f"valid ppt: {len(passports)}")

log.info(f"total valid {total}")
