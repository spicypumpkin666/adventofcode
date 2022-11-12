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
total = 0

def make_check(passport):
    if 1920 > int(passport['byr']) > 2002:
        return False
    if 2010 > int(passport['iyr']) > 2020:
        return False
    elif 2020 > int(passport['eyr']) > 2030:
        return False
    elif passport['hgt']:
        if passport['hgt'][-2] == 'cm':
            if 150 <= passport['hgt'][:3] <= 193:
                pass
            else:
                return False
        elif passport['hgt'][-2] == 'in':
            if 59 <= passport['hgt'][:2] <= 76:
                pass
            else:
                return False
        else:
            return False
    pattern = re.compile("#([a-f][0-9]+)")
    if not pattern.match(passport['hcl']):
        return False
    if passport['ecl'] not in eyes:
        return False
    elif len(str(passport['pid'])) != 9:
        return False
    return True

for passport in passports:
    if make_check(passport):
        total += 1


log.info(f"total valid {total}")
