from tsp import TSP
import random
import numpy as np

map_size = 5
map_arr = []
for x in range(map_size):  # random map
    for y in range(map_size):
        if(random.randint(0,1)):
            map_arr.append([x,y])
t = TSP(map_arr,map_arr[0])