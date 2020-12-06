with open("input.dat", 'r') as f:
    id_list = []
    for l in f:
        column_code = l[:7]
        row_code = l[7:].strip()
        column = 0
        row = 0
        for bit in column_code:
            column = column << 1
            column = column | (bit == 'B')
        for bit in row_code:
            row = row << 1
            row = row | (bit == 'R')

        id_list.append(column*8+row)
    
    id_list.sort()
    for i, num in enumerate(id_list):
        print(f"curr_seat: {num}, next_seat: {id_list[i+1]}")
        if id_list[i+1] - num == 2:
            print(num + 1)
            break
