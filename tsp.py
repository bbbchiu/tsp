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
        self.walk()
        #self.show_result()
        self.visual_w()
        print("start travel~~~")
        cost = 0
        self.travel_arr.append(self.initp)
        self.travel_path(self.map_arr.copy(),self.initp.copy(),cost)
        print()
        print()
        print("show min path")
        self.visual_m()
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

    def walk(self):
        # initialize
        self.walk_arr.append(self.initp)
        self.map_arr.remove(self.initp)

        # travel
        print("get min path~~~")
        self.min_path(self.map_arr.copy())


    def show_result(self):
        print("Result: ")
        print(self.walk_arr)
        print("Remain arr: ")
        print(self.map_arr)

    def visual_w(self):
        mm = np.zeros((self.map_size,self.map_size))
        print("Start Visualization~~~")
        cnt = 1
        for i in self.walk_arr:
            mm[i[0]][i[1]] = cnt
            cnt += 1
        print(mm)            

    def visual_t(self):
        mm = np.zeros((self.map_size,self.map_size))
        print("Start Visualization~~~")
        cnt = 1
        for i in self.travel_arr:
            mm[i[0]][i[1]] = cnt
            cnt += 1
        print(mm)  
        
    def visual_m(self):
        mm = np.zeros((self.map_size,self.map_size))
        print("Start Visualization~~~")
        cnt = 1
        for i in self.min_arr:
            mm[i[0]][i[1]] = cnt
            cnt += 1
        print(mm)  

    def min_path(self,m_arr):
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
#        print("m_arr: ",m_arr)
#        print("spot: ",spot)
#        print("cost: ",cost)
#        print("travel_arr: ",self.travel_arr)
#        print()
#        if(len(m_arr) == 0 or cost > self.min_cost):
#            if(len(m_arr) == 0 and cost <= self.min_cost and len(self.travel_arr) == len(self.walk_arr)):
#                print("cost: ",cost)
#                self.visual_t()
#                self.min_cost == cost
#                self.min_arr = self.travel_arr.copy()
#                self.travel_arr = []
#                self.travel_arr.append(self.initp)
#            elif(len(self.travel_arr) > 1):
#                pass
#                print("pop: ",self.travel_arr.pop())
#            else:
#                pass
#            return 0
        if(len(m_arr) == 0):
            if(cost <= self.min_cost):
                #self.visual_t()
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
            
        

        
