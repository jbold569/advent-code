def tree_count(right: int, down: int) -> int:
    with open("input.dat", 'r') as f:
        pos_x = 0
        pos_y = 0
        counter = 0
        geo_map = [l for l in f]
        while True:
            pos_x = (pos_x + right) % (len(geo_map[0])-1)
            pos_y += down
            if pos_y >= len(geo_map):
                break
            #print(f'pos_x: {pos_x}, pos_y: {pos_y}, char: {geo_map[pos_y][pos_x]}')
            if geo_map[pos_y][pos_x] == '#':
                counter += 1
        return counter


print(tree_count(1, 1)*tree_count(3, 1)*tree_count(5, 1)
      * tree_count(7, 1)*tree_count(1, 2))
