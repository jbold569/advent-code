with open("input.dat", 'r') as f:
    right = 3
    down = 1
    pos_x = 0
    pos_y = 0
    counter = 0
    geo_map = [ l for l in f ]
    while True:
        pos_x = (pos_x + right) % (len(geo_map[0])-1)
        pos_y += down
        if pos_y == len(geo_map): break
        print(f'pos_x: {pos_x}, pos_y: {pos_y}, char: {geo_map[pos_y][pos_x]}')
        if geo_map[pos_y][pos_x] == '#':
            counter += 1        
    print(counter)

