import numpy as np
import math
class Env:
    def __init__(self):
        self.x_range = 300 # 背景大小
        self.y_range = 300
        self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def obs_map(self):
       

        x = self.x_range
        y = self.y_range
        obs = set()

        #生成许多圆
        #第一行
        for i in range(23,60):
            for j in range(23,60):
               obs.add((i,j))
                    
        for i in range(94,135):
            for j in range(15,60):
               obs.add((i,j))

        for i in range(169,210):
            for j in range(15,60):
               obs.add((i,j))
        for i in range(240,285):
            for j in range(15,60):
               obs.add((i,j))

        #第二行
        for i in range(55,95):
            for j in range(93,132):
                obs.add((i,j))
        for i in range(131,169):
            for j in range(93,132):
                obs.add((i,j))
        for i in range(206,244):
            for j in range(93,132):
                obs.add((i,j))
       #第三行
        for i in range(18,57):
            for j in range(168,207):
                obs.add((i,j))
        for i in range(93,132):
            for j in range(168,207):
                obs.add((i,j))
        for i in range(168,207):
            for j in range(168,207):
                obs.add((i,j))
        for i in range(243,282):
            for j in range(168,207):
                obs.add((i,j))
       #第四行
        for i in range(55,95):
            for j in range(243,282):
                obs.add((i,j))
        for i in range(131,169):
            for j in range(243,282):
                obs.add((i,j))
        for i in range(206,244):
            for j in range(243,282):
                obs.add((i,j))


        return obs