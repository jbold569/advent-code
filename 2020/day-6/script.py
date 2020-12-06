with open("input.dat", 'r') as f:
    questions = set()
    counter = 0
    for l in f:
        line = l.strip()
        if line == "":
            counter += len(questions)
            questions.clear()
        else:
            for char in line: 
                questions.add(char)
    counter += len(questions)
        
    print(counter)
