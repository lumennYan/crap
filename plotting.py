"""
Plot tools 2D
@author: huiming zhou
"""

import matplotlib.pyplot as plt
import env
class Plotting:
    def __init__(self, xI, xG):
        self.xI, self.xG = xI, xG
        self.env = env.Env()
        self.obs = self.env.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def animation(self, way1,way2,way3,name):
        self.plot_grid(name)
        self.plot_path(way1,way2,way3)
        plt.show()


    def plot_grid(self, name):
        obs_x = [x[0] for x in self.obs]
        obs_y = [x[1] for x in self.obs]
        xI = self.xI
        for i in range(len(xI)):
            plt.plot(self.xI[i][0], self.xI[i][1], "gs")
        plt.plot(self.xG[0], self.xG[1], "rs")
        plt.plot(obs_x, obs_y, "ks")
        plt.title(name)
        plt.axis("equal")

    def plot_visited(self, visited, cl='gray'):
        for i in range(xI):
            if self.xI[i] in visited:
                visited.remove(self.xI[i])

        if self.xG in visited:
            visited.remove(self.xG)

        count = 0

        for x in visited:
            count += 1
            plt.plot(x[0], x[1], color=cl, marker='o')
            plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])

            if count < len(visited) / 3:
                length = 20
            elif count < len(visited) * 2 / 3:
                length = 30
            else:
                length = 40

            if count % length == 0:
                plt.pause(0.001)
        plt.pause(0.01)

    def plot_path(self, way1, way2, way3):  
        i = 0
        xI = self.xI
        while True:
            if i < len(way1):
                path1_x = [way1[j][0] for j in range(0,i)]
                path1_y = [way1[j][1] for j in range(0,i)]
                drone1_x = way1[i][0]
                drone1_y = way1[i][1]
                plt.plot(path1_x, path1_y, linewidth='1', color='#F08080')
                p1,=plt.plot(drone1_x, drone1_y, "#191970", marker='*')

            if i<len(way2):
                path2_x = [way2[j][0] for j in range(0,i)]
                path2_y = [way2[j][1] for j in range(0,i)]
                drone2_x = way2[i][0]
                drone2_y = way2[i][1]
                plt.plot(path2_x, path2_y, linewidth='1', color='#F08080')
                p2,=plt.plot(drone2_x, drone2_y, "#191970", marker='*')

            if i<len(way3):
                path3_x = [way3[j][0] for j in range(0,i)]
                path3_y = [way3[j][1] for j in range(0,i)]
                drone3_x = way3[i][0]
                drone3_y = way3[i][1]
                plt.plot(path3_x, path3_y, linewidth='1', color='#F08080')
                p3,=plt.plot(drone3_x, drone3_y, "#191970", marker='*')

            i = i+1        
            plt.pause(0.1)
            if i <= len(way1):
                p1.remove()
            if i <= len(way2):
                p2.remove()
            if i <= len(way3):
                p3.remove()
            if i == max(len(way1),len(way2),len(way3)):
                break
        for i in range(len(xI)):
            plt.plot(self.xI[i][0], self.xI[i][1], "#00FF00")
        plt.plot(self.xG[0], self.xG[1], "r")
        plt.pause(0.01)
  
    @staticmethod
    def color_list():
        cl_v = ['silver',
                'wheat',
                'lightskyblue',
                'royalblue',
                'slategray']
        cl_p = ['gray',
                'orange',
                'deepskyblue',
                'red',
                'm']
        return cl_v, cl_p

    @staticmethod
    def color_list_2():
        cl = ['silver',
              'steelblue',
              'dimgray',
              'cornflowerblue',
              'dodgerblue',
              'royalblue',
              'plum',
              'mediumslateblue',
              'mediumpurple',
              'blueviolet',
              ]
        return cl
