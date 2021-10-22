# Arranging names in ascending order , firstly by Name and then by roman numerals.

def sort_name(names):
    # Roman numerals: I, V, X, L - 50, c - 100, D - 500, M - 1000
    occ = {} # storing the R for the first name
    result = []
    # 1. sort names
    names = sorted(names)

    # 2. examine each name and store in hashmap: {name: [R vals]}
    for n in names:
        name_part = n.split(" ")
        name = name_part[0]
        r = name_part[1]
        if name in occ:
            occ[name].append(r)
        else:
            occ[name] = [r]
    
    # 3. add each name in order into the result
    i = 0
    while i < len(names):
        fn = names[i].split(" ")[0]
        r_to_add = occ[fn]
        # figure out the order of all the romans: occ[fn]
        sort_r = sorted(r_to_add, key=lambda x: convert_roman_to_num(x))
        for r in sort_r:
            result.append(f"{fn} {r}")
        # skip over same names using len
        i += len(r_to_add)

    return result


def convert_roman_to_num(roman_val: str):
    val_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in reversed(range(0, len(roman_val))):
        curr_val = val_map[roman_val[i]]
        if i == len(roman_val) - 1: # it is the last letter
            total += curr_val
        elif curr_val >= val_map[roman_val[i+1]]: # compare it with the letter to your right
            total += curr_val
        else:
            total -= curr_val
    return total

R = "CXCV"
print(convert_roman_to_num(R))

input = ['Louis XX', 'Louis VI', 'Louis I', 'Peter I']
print(sort_name(input))
# ['Louis I', 'Louis VI', 'Louis XX', 'Peter I']

input = ['Zan VV','Zan I','Louis V', 'Louis VI', 'Louis X','Peter III','Peter I', "Peter II"]
print(sort_name(input))