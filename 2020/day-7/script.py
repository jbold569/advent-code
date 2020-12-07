import re
from collections import defaultdict

def sum_nodes(p, tree) -> list:
    
    layer = tree[p]
    return [c for i,c in layer] + [ n for i,c in layer for n in sum_nodes(c, tree)  ]

with open("input.dat", 'r') as f:
    counter = 0
    tree = defaultdict(list)
    for l in f:
        parent_bag, contents = [ x.strip() for x in l.split("bags contain") ]
        for i in contents.split(","):
            m = re.match(r"^(\d+)\s(\w+\s\w+).*", i.strip())
            if m:
                tree[m[2]].append((int(m[1]),parent_bag))
                
    print(len(set(sum_nodes("shiny gold", tree))))