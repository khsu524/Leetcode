def smallest_perm_num(num: str):
    num_zero = num.count("0")
    sorted_string = sorted(num)
    # result = [first not zero digit] + [zeros] + [first not zero's after to end]
    res_list = sorted_string[num_zero:num_zero + 1] + sorted_string[0:num_zero] * num_zero + sorted_string[num_zero + 1:]
    return "".join(res_list)

print(smallest_perm_num("12321342310"))