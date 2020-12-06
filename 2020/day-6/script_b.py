def count_intersec(group: set) -> int:
    x = group[0]
    intersec = x.intersection(*group[1:])
    return len(intersec)

with open("input.dat", 'r') as f:
    group = []
    counter = 0
    for l in f:
        questions = set()
        line = l.strip()
        if line == "":
            counter += count_intersec(group)
            group.clear()
        else:
            for char in line: 
                questions.add(char)
            group.append(questions)
    counter += count_intersec(group)
        
    print(counter)
