import re

# byr(Birth Year)
# iyr(Issue Year)
# eyr(Expiration Year)
# hgt(Height)
# hcl(Hair Color)
# ecl(Eye Color)
# pid(Passport ID)
# cid(Country ID)

def byrValid(v: str) -> bool:
    m = re.match(r"^\d{4}$",v)
    if m:
        y = int(m[0])
        return y >= 1920 and y <= 2002
    return False

def iyrValid(v: str) -> bool:
    m = re.match(r"^\d{4}$",v)
    if m:
        y = int(m[0])
        return y >= 2010 and y <= 2020
    return False

def eyrValid(v: str) -> bool:
    m = re.match(r"^\d{4}$",v)
    if m:
        y = int(m[0])
        return y >= 2020 and y <= 2030
    return False

def hgtValid(v: str) -> bool:
    m = re.match(r"^(\d+)(cm|in)$",v)
    if m:
        h = int(m[1])
        unit = m[2]
        if unit == "cm":
            return h >= 150 and h <= 193
        else:
            return h >= 59 and h <= 76
    return False

def hclValid(v: str) -> bool:
    m = re.match(r"^#([0-9a-f]{6})$",v)
    return bool(m)

def eclValid(v: str) -> bool:
    m = re.match(r"^amb|blu|brn|gry|grn|hzl|oth$", v)
    return bool(m)

def pidValid(v: str) -> bool:
    print(v)
    m = re.match(r"^\d{9}$", v)
    return bool(m)

def isValid(id) -> bool:
    fields = {
        "byr": byrValid, 
        "iyr": iyrValid, 
        "eyr": eyrValid, 
        "hgt": hgtValid, 
        "hcl": hclValid, 
        "ecl": eclValid, 
        "pid": pidValid
    }
    valid = True
    for field, func in fields.items():
        try:
            value = id[field]
            print(f"value: {value}, valid: {func(value)}")
            if not func(value):
                valid = False
                break
        except KeyError as e:
            valid = False
            break
    return valid


with open("input.dat", 'r') as f:
    counter = 0
    id = {}
    for l in f:
        if l == "\n":
            counter += int(isValid(id))
            id = {}
            continue
        pairs = l.strip().split(" ")
        for pair in pairs:
            k, v = pair.split(":")
            id[k] = v
    counter += int(isValid(id))
    print(counter)
