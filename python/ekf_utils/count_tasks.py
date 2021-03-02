import sys
import re

categories = {'W':'Writing','S':'Science','L':'Logistics','M':'Meeting'}
catnames = "".join(categories.keys())

def count ( str_input ):
    counts = dict(zip(categories.keys(),[0,]*len(categories)))
    tasks = str_input.splitlines()
    for task in tasks:
        category = re.findall(f'(?<=\[)[{catnames}](?=\])',task)
        if len(category) > 0:
            counts[category[0]] += 1
    return counts

def fmt_counts ( cdict ):
    for key in cdict:
        print (f'{categories[key]}:\t{cdict[key]}')

def main ( str_input ):
    cdict = count ( str_input )
    fmt_counts(cdict)

if __name__ == '__main__':
    str_input = sys.argv[1]
    main(str_input)
