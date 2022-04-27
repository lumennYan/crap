import math
import numpy as np
import test
import sys
import time
import bt

from behave import condition, action, FAILURE
from behave import repeat, forever, succeeder, failer
from behave import SUCCESS, FAILURE, RUNNING, BehaveException, \
                   action, condition

class Drone:
    def __init__(self,start,index):
        self.index = index
        self.position_x=start[0]
        self.position_y=start[1]
        self.velocity = 0
        self.acc_tracking = 2
        self.acc_total = 0
        self.size = 3
        self.neighbors = []
        self.neighbors_path = []
        self.R = 5
   
        #跟随路径
    def tracking(self,path): 
        length = len(path)
        position = np.array([self.position_x,self.position_y,length-1])
        velocity = self.velocity
        velocity = 0
        t=0
        dis = 0
        R = self.R
        position_array = []
        while dis < length:
            self.position_x = path[length-1-dis][0]
            self.position_y = path[length-1-dis][1]
            print('position',self.position_x,self.position_y)
            position_array.append([self.position_x,self.position_y])
            print(position_array)
            position = np.array([self.position_x,self.position_y,length-1-dis])   
            t = t+1
            print('t',t)
            F = self.getF(self.neighbors)
            
            #####run不了的部分

            tree = ( ( bt.toofar(self.position_x,self.position_y,self.neighbors) >> 
                      (bt.notnear(self.position_x,self.position_y,self.neighbors_path,R)>>
                       (bt.close(self.position_x,self.position_y,self.neighbors,test.goal)>>
                        bt.slow(self.acc_total,self.acc_tracking,acc_swarm = self.cluster(F,position,path)))))|bt.go(self.acc_total,acc_swarm = self.cluster(F,position,path))
                )
            bb = tree.blackboard(5)
            state = bb.tick()
            print ("state = %s\n" % state)
            while state == RUNNING:
                state = bb.tick()
                print ("state = %s\n" % state)
            assert state == SUCCESS or state == FAILURE
            ##########
          

              


            print('acc total',self.acc_total)
            if velocity<2: #最大速度设置
                velocity = self.acc_total*0.5 + velocity
            else:
                pass
            print('velocity',velocity)
            dis = velocity*t
            if np.isnan(dis): #以防dis为空
                dis = 0
            else:
                dis = round(dis)
            print('dis',dis)

        
            time.sleep(0.01)
        return position_array

        #受力
    def getF(self,others):
        length = len(others)
        a = 4
        R = self.R 
        b = 2
        m = 0.25
        n = 0.5
        F = np.array([0,0])
        for i in range(length):
            d = math.hypot(self.position_x - others[i].position_x, self.position_y - others[i].position_y)
            if d >= a and d <= R: #引力场
                f = -m*np.array([self.position_x - others[i].position_x, self.position_y - others[i].position_y])
            elif d <= b: #斥力
                f = n*(1/d - 1/b)/pow(d,3)*np.array([self.position_x - others[i].position_x, self.position_y - others[i].position_y])
            else:#没力
                f = np.array([0,0])
            F = F + f
        print('F',F)
        return F

        #群聚加速度
    def cluster(self,F,position,path):
        self.now = np.array([position[0],position[1]])
        self.next = np.array([path[position[2]-1][0],path[position[2]-1][1]])
        direction = self.next - self.now
        print('direction',direction)
        norm = np.linalg.norm(direction)
        print('norm',norm)
        direction = direction/norm
        acc_swarm = np.dot(F,direction)
        print('acc swarm',acc_swarm)
        return acc_swarm


    #树节点 #自用
    def istoofar(self,others):
        length = len(others)
        for i in range(length):
            d = math.hypot(self.position_x - others[i].position_x, self.position_y - others[i].position_y)
            if d > self.R:
                print("too far")
                return True
            print("not too far")
            return False
    def isnearpath(self,otherpath,r):
        for i in range(self.position_x-r,self.position_x+r):
            for j in range(self.position_y-r,self.position_y+r):
                if (i,j) in otherpath:
                    return True
                return False
    def farfromgoal(self,other,goal):
        own_dis = math.hypot(self.position_x - goal[0],self.position_y-goal[1])
        oth_dis = math.hypot(other.position_x - goal[0],other.position_y-goal[1])
        if own_dis > oth_dis:
            return True
        return False


    def going(self):
        self.acc_total = self.acc_tracking + self.cluster(F,position,path)


    def slow(self):
        self.acc_total = -2 + self.cluster(F,position,path)

