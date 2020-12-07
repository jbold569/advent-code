import re
from collections import defaultdict

def sum_nodes(p, tree) -> list:
    layer = tree[p]
    if layer == []:
        return []
    else:
        return [i for i,c in layer] + [ i*n for i,c in layer for n in sum_nodes(c, tree) ]

with open("input.dat", 'r') as f:
    counter = 0
    tree = defaultdict(list)
    for l in f:
        parent_bag, contents = [ x.strip() for x in l.split("bags contain") ]
        for i in contents.split(","):
            m = re.match(r"^(\d+)\s(\w+\s\w+).*", i.strip())
            if m:
                tree[parent_bag].append((int(m[1]),m[2]))
                
    print(sum(sum_nodes("shiny gold", tree)))