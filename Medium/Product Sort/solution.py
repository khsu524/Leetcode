from typing import List


def itemsSort(items: List[int]):
    items.sort()
    counter = {}
    for num in items:
        counter[num] = counter.get(num, 0) + 1

    # sorted takes in the counter.items as a list of tuples (key, values), ordered by the x[1], the value
    sorted_val = sorted(counter.items(), key=lambda x: x[1])
    # this will produce a list of sorted tuple by the values [(key, val)]

    result = []
    for key in sorted_val:
        result  += [key[0]] * key[1] # produce "val" number of that key
    print(result)
    return result

inputs = [4,5,6,5,4,3]
itemsSort(inputs)


inputs = [8, 5, 5, 5, 5, 1, 1, 1, 4, 4]
itemsSort(inputs)

inputs = [1] * 9
itemsSort(inputs)