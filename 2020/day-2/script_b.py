import re

with open("input.dat", 'r') as f:
    counter = 0
    for l in f:
        m = re.search(r"(\d+)-(\d+) (\w): (\w+)", l)
        pos_1 = int(m.group(1))-1
        pos_2 = int(m.group(2))-1
        char = m.group(3)
        password = m.group(4)
        if (password[pos_1] == char) ^ (password[pos_2] == char):
            counter += 1
    print(counter)
    
