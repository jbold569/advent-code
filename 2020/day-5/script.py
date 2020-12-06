with open("input.dat", 'r') as f:
    id = 0
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
        
        tmp = column*8+row
        if tmp > id: id = tmp

    print(id)
