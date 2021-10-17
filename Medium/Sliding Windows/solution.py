from typing import List

def car_parking_roof(car: List[int], min_car_cover: int):
  # sort the array
  car.sort()
  # use the max distance as initial
  shortest_roof = car[-1] - car[0] + 1
  start = 0 

  for end in range(0, len(car)):
    # if number of space occupied is less than min car covered, skip it
    if end - start + 1 < min_car_cover:
      continue
    current_roof = car[end] - car[start] + 1
    shortest_roof = min(shortest_roof, current_roof)

    # we can start sliding the start, since the ending is going
    start += 1

  return shortest_roof



n = [2, 10, 8, 17]
k = 3
short = car_parking_roof(n, k)
print(short)
# result: 9


n = [1,2, 3, 10]
k = 4
short = car_parking_roof(n, k)
print(short)
# result: 10

