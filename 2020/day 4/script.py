# byr(Birth Year)
# iyr(Issue Year)
# eyr(Expiration Year)
# hgt(Height)
# hcl(Hair Color)
# ecl(Eye Color)
# pid(Passport ID)
# cid(Country ID)
def isValid(id) -> bool:
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = True
    missing = []
    for field in fields:
        if not field in id.keys():
            missing.append(field)
            valid = False
    return valid

with open("input.dat", 'r') as f:
    counter = 0
    id = {}
    for l in f:
        if l == "\n":
            counter += int(isValid(id))
            id={}
            continue
        pairs = l[:-1].split(" ")
        for pair in pairs:
            k,v = pair.split(":")
            id[k]=v
    counter += int(isValid(id))
    print(counter)

