with open("input.dat", 'r') as f:
    numbers = [int(l) for l in f]
    for i, num_i in enumerate(numbers):
        for j, num_j in enumerate(numbers):
            if i == j or num_i + num_j >= 2020:
                continue
            for k, num_k in enumerate(numbers):
                if k == i or k == j:
                    continue
                if num_i + num_j + num_k == 2020:
                    print(num_i*num_j*num_k)
