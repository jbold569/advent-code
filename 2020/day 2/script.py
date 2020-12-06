import re

with open("input.dat", 'r') as f:
    counter = 0
    for l in f:
        m = re.search(r"(\d+)-(\d+) (\w): (\w+)", l)
        lower = int(m.group(1))
        upper = int(m.group(2))
        char = m.group(3)
        password = m.group(4)
        if password.count(char) >= lower and password.count(char) <= upper:
            counter += 1
    print(counter)

