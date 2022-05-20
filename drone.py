import math
import numpy as np
import test
import sys
import time
import bt
import matplotlib.pyplot as plt
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
        self.acc_tracking = 0.5
        self.acc_total = 0
        self.size = 3
        self.neighbors = []
        self.neighbors_path = []
        self.R = 10
        self.lost = None
        self.lost_paths = []
        self.msg = []
        self.share = []
        self.goal = test.goal
        self.acc_swarm = 0
        #跟随路径

    def tracking(self,path,share): 
        length = len(path)
        position = np.array([self.position_x,self.position_y,length-1])
        velocity = self.velocity
        velocity = 0
        t=0
        ttt = 0
        dis = 0
        R = self.R
        position_array = []
        iscollision = []
        while dis < length:
            self.position_x = path[length-1-dis][0]
            self.position_y = path[length-1-dis][1]
            self.update(self.position_x,self.position_y,self.index,share)
            self.share = share
            print('position',self.position_x,self.position_y)
            print('share',self.share)
           
            if share[0] == share[1] or share[0] == share[2] or share[1] == share[2]:
                iscollision.append(0)
            else:
                iscollision.append(1)

            position_array.append([self.position_x,self.position_y])
            print(self.index,position_array)
            position = np.array([self.position_x,self.position_y,length-1-dis])   
            t = t+1
            print('t',t)

            F = self.getF(self.share)
            self.acc_swarm = self.cluster(F,position,path)

            #####行为树
            tree = ( ( bt.toofar >> bt.notnear >> bt.close>> bt.slow)|bt.go)
            bb = tree.blackboard(self)
            state = bb.tick()
            ##########
 
            print('acc total',self.acc_total)
            if velocity<6.0:
                velocity = self.acc_total*1 + velocity
                if velocity<=-6.0:
                   velocity = -6.0 #最多减到-3
            else:
                velocity = 6.0 
            print('velocity',self.index,velocity)
            dis = velocity*1 + dis
            if np.isnan(dis): #以防dis为空
                dis = 0
            else:
                dis = round(dis)
            print('dis',dis)
            time.sleep(0.01)

        print('t',t)
        x1 = np.linspace(0,t,t)
        plt.figure()
        plt.plot(x1,iscollision)
        plt.title('map2--index_changed  velocity=5.0')
        plt.xlabel('t',fontsize=14)
        plt.ylabel('safety',fontsize=14)
        plt.xlim(0,t)
        plt.ylim(0,1.1)
        #plt.show()
        print('ttt',ttt)
        return position_array

        #受力
    def getF(self,others):
        length = len(others)
        a = 8
        R = self.R 
        b = 4
        m = 0.05
        n = 6
        F = np.array([0,0])
        for i in range(length):
            if i == self.index:
                pass
            elif (others[i][0],others[i][1]) == self.goal:
                pass
            else:
                d = math.hypot(self.position_x - others[i][0], self.position_y - others[i][1])
                print('d',d)
                if d != 0:
                    if d >= a and d <= R: #引力场
                        f = -m*np.array([self.position_x - others[i][0], self.position_y - others[i][1]])
                    elif d <= b: #斥力
                        f = n*(1/d - 1/b)/pow(d,3)*np.array([self.position_x - others[i][0], self.position_y - others[i][1]])
                    else:#没力
                        f = np.array([0,0])
                    F = F + f
                else:
                    pass
                    
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

        #找迷路朋友的路
    def get_lostpaths(self,neighbors_paths,index):
        aths = []
        for i in range(len(neighbors_paths)):
            if i == index:
                paths = neighbors_paths[i]
        return paths

        #更新全局变量
    def update(self,x,y,index,share):
        for i in range(len(share)):
            if i == index:
                share[i] = [x,y]
            else:
                pass

        #状态机节点 
    def istoofar(self,others):
        length = len(others)
        for i in range(length):
            if i ==self.index:
                pass
            else:
                d = math.hypot(self.position_x - others[i][0], self.position_y - others[i][1])
                if d > self.R:
                    print("too far")
                    self.lost = i
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
        oth_dis = math.hypot(other[0] - goal[0],other[1]-goal[1])
        print('own_dis',own_dis)
        print('oth_dis',oth_dis)
        if own_dis > oth_dis:
            return True
        return False


