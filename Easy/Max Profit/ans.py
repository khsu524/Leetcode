from typing import List


def max_profit(prices: List[int]):
    min, max = prices[0], prices[0]
    for p in prices:
        if p < min:
            min = p
        if p > max:
            max = p
    return max-min


print(max_profit([2132,7,324,3254,1,324,2,4,5,43,6556,]*100000))