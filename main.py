import random

index = {}
rev_index = {}

with open('book.txt', 'rt') as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c in index:
                index[c].append(f"{i+1}:{j+1}")
            else:
                index[c] = [f"{i+1}:{j+1}", ]

for k, v in index.items():
    for b in v:
        rev_index[b] = k

#for k, v in index.items():
#    print(k, ':', v)

with open('input.txt', 'rt') as f:
    text = f.read()

with open('output.txt', 'wt') as f:
    for c in text:
        if c in index:
            b = random.choice(index[c])
            f.write(b + '\n')
        else:
            print(f"ERROR: '{c}' not in dataset")

with open('output.txt', 'rt') as f:
    for code in f.read().split('\n'):
        if len(code) == 0: continue
        
        if code in rev_index:
            print(rev_index[code], end='')
        else:
            print(f"ERROR: '{code}' not in book")
        
