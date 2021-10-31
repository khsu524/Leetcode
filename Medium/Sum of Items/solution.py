from typing import List
import time

def sum_of_items(input: List, key: int):
    start_time = time.time()
    # input = [4,2,-5,11]
    # key = 3 
    size = len(input)
    res_list = [0] * size
    cached = 0
    last_known_positive_index = 0 
    for i in range(1, size + 1):
        sum_key = 0
        curr_index = i if i < size  else i - size
        last_index_of_set = curr_index + key - 1
        last_index_of_set = last_index_of_set if last_index_of_set < size else last_index_of_set - size 
        # print("\nlast index:" + str(last_index_of_set))
        if i == 1:
            for each in input[1:key+1]:
                sum_key += each
        else:
            sum_key = cached + input[last_index_of_set]
        # print("sum key:" + str(sum_key))

        cached = sum_key - input[curr_index]
        # print("cache:" + str(cached))
        
        # insert values into final list
        res_list[curr_index] = sum_key
        # res_list.append(sum_key)
        if sum_key > 0:
            last_known_positive_index = curr_index
        
    for i in range(last_known_positive_index, last_known_positive_index + size):
        actual_index = i if i < size  else i - size
        if res_list[actual_index] < 0: 
            last_index = actual_index - 1 if actual_index > 0 else size - 1
            res_list[actual_index] = res_list[last_index]
    
    print("--- %s seconds ---" % (time.time() - start_time))
    return res_list

# Brute force
def sum_of_items_brute(input: List, key: int):
    start_time = time.time()
    size = len(input)
    res_list = [0] * size
    last_known_positive_index = 0 
    for i in range(1, size + 1):
        sum_key = 0
        curr_index = i if i < size  else i - size
        # last_index_of_set = curr_index + key - 1
        # last_index_of_set = last_index_of_set if last_index_of_set < size else last_index_of_set - size

        for j in range(i, i + key):
            curr_index = j if j < size  else j - size   
            sum_key += input[curr_index]
        res_list[curr_index] = sum_key
        if sum_key > 0:
            # print("POS IND: ")
            # print(curr_index)
            last_known_positive_index = curr_index
    # print(res_list)
    for i in range(last_known_positive_index, last_known_positive_index + size):
        actual_index = i if i < size  else i - size
        if res_list[actual_index] < 0: 
            last_index = actual_index - 1 if actual_index > 0 else size - 1
            # print("laST IND: ")
            # print(res_list[last_index])
            res_list[actual_index] = res_list[last_index]

    print("--- %s seconds ---" % (time.time() - start_time))
    return res_list
    

input = [3, -1,-1,-1, -3] * 10000000
key = 3 
print("\noptimized: ")
sum_of_items(input, key) # this took 2.55

print("\nbrute: ")
sum_of_items_brute(input, key) # this took 3.72