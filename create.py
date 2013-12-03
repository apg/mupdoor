create.py
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29

import json
import re
import sys


def extract(row):
    name = row['member']['name'].strip()
    q1 = row['answers'][0].strip()
    guests = row['guests']

    if name != q1 and len(q1) != 0:
        return (q1.title(), guests,)
    elif len(name) == 0:
        return None
    else:
        return (name, guests,)


def print_it(results):
    for n in sorted(results):
        if n[1] == 0:
            print n[0].encode('ascii', 'ignore')
        else:
            print n[0].encode('ascii', 'ignore'), 'guests=', n[1]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        xs = json.loads(open(sys.argv[1]).read())
        print_it(filter(None, map(extract, xs['results'])))
