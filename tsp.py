import numpy as np
import math
import time

class TSP:
    def __init__(self,map_arr,init_point):
        self.initp = init_point    
        self.map_arr = map_arr    
        self.map_size = max(map(max,self.map_arr))+1
        self.map_struct = np.zeros((self.map_size,self.map_size))
        self.walk_arr = []
        self.travel_arr = []
        self.min_arr = []
        self.min_cost = 0

        self.init_map()
        self.show_init()
        print()
        self.nearest_neighbor_path()
        self.visual_arr(self.walk_arr.copy())
        print("start travel~~~")
        cost = 0
        self.travel_arr.append(self.initp)
        self.travel_path(self.map_arr.copy(),self.initp.copy(),cost)
        print()
        print()
        print("show min path")
        self.visual_arr(self.min_arr.copy())
        print("min cost: ",self.min_cost)

    def init_map(self):
        for m in self.map_arr:
            self.map_struct[m[0],m[1]] = 1
        
    def show_init(self):
        print("Show Init Information~~~")
        print()
        print("Input: ")
        print("map_arr: ")
        print(self.map_arr)
        print("init_point: ",self.initp)
        print()
        print("Class Init: ")
        print("Map Visualization")
        print(self.map_struct)

    def get_cost(self,x,y):
            return math.sqrt((x[0]-y[0])*(x[0]-y[0])+(x[1]-y[1])*(x[1]-y[1]))

    def visual_arr(self,arr):
        mm = np.zeros((self.map_size,self.map_size))
        print("Start Visualization~~~")
        cnt = 1
        for i in arr:
            mm[i[0]][i[1]] = cnt
            cnt += 1
        print(mm)            

    def nearest_neighbor_path(self):
        # initialize
        self.walk_arr.append(self.initp)
        self.map_arr.remove(self.initp)
        m_arr = self.map_arr.copy()

        # travel
        print("get min path~~~")
        spot = self.initp
        cost = 0

        terminate = 1000
        while(len(m_arr) != 0 and terminate > 0):
            min_num = 10^5
            s = spot
            for i in m_arr:
                if(min_num > self.get_cost(i,spot)):
                    min_num = self.get_cost(i,spot)
                    #print("min_cost: ",min_num)
                    s = i
            if(s != spot):
                self.walk_arr.append(s)
                m_arr.remove(s)
                cost += self.get_cost(spot,s)
                spot = s
            else:
                print("No Spot")
            #print()
            
            terminate -= 1
        if(len(m_arr) == 0 and (cost < self.min_cost or self.min_cost == 0)):
            self.min_cost = cost
            print("min cost: ",self.min_cost)


    def travel_path(self,m_arr,spot,cost):
        if(len(m_arr) == 0):
            if(cost <= self.min_cost):
                self.min_cost = cost
                self.min_arr = self.travel_arr.copy()
            
            self.travel_arr.pop()
            return 0
        elif(cost > self.min_cost):
            self.travel_arr.pop()
            return 0
        else:
            for i in m_arr:
                new_arr = m_arr.copy()
                new_cost = cost
                new_cost += self.get_cost(spot,i)
                self.travel_arr.append(i)
                new_arr.remove(i)
                self.travel_path(new_arr,i,new_cost)
        
        self.travel_arr.pop()
        return 0
            
        

        
