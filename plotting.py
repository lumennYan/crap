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

    def animation(self, way_list,name):
        self.plot_grid(name)
        self.plot_path(way_list)
        plt.show()


    def plot_grid(self, name):
        obs_x = [x[0] for x in self.obs]
        obs_y = [x[1] for x in self.obs]
        xI = self.xI
        for i in range(len(xI)):
            plt.plot(self.xI[i][0], self.xI[i][1], "gs")
        plt.plot(self.xG[0], self.xG[1], "rs")
        plt.plot(obs_x, obs_y, "bs")
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

    def plot_path(self,way_list):  
        i = 0
        xI = self.xI
        path_x = []
        path_y = []
        drone_x = []
        drone_y = []
        length = []
        #p = []
        for l in range(len(way_list)):
            length.append(len(way_list[l]))
        print(length)


        while True:

            if i < len(way_list[0]):
                path1_x = [way_list[0][j][0] for j in range(0,i)]
                path1_y = [way_list[0][j][1] for j in range(0,i)]
                drone1_x = way_list[0][i][0]
                drone1_y = way_list[0][i][1]
                plt.plot(path1_x, path1_y, linewidth='1', color='#F08080')
                p1,=plt.plot(drone1_x, drone1_y, "#191970", marker='*')

            if i < len(way_list[1]):
                path2_x = [way_list[1][j][0] for j in range(0,i)]
                path2_y = [way_list[1][j][1] for j in range(0,i)]
                drone2_x = way_list[1][i][0]
                drone2_y = way_list[1][i][1]
                plt.plot(path2_x, path2_y, linewidth='1', color='y')
                p2,= plt.plot(drone2_x, drone2_y, "#191970", marker='*')

            if i<len(way_list[2]):
                path3_x = [way_list[2][j][0] for j in range(0,i)]
                path3_y = [way_list[2][j][1] for j in range(0,i)]
                drone3_x = way_list[2][i][0]
                drone3_y =way_list[2][i][1]
                plt.plot(path3_x, path3_y, linewidth='1', color='#FFA500')
                p3,=plt.plot(drone3_x, drone3_y, "#191970", marker='*')

            if i<len(way_list[3]):
                path4_x = [way_list[3][j][0] for j in range(0,i)]
                path4_y = [way_list[3][j][1] for j in range(0,i)]
                drone4_x = way_list[3][i][0]
                drone4_y = way_list[3][i][1]
                plt.plot(path4_x, path4_y, linewidth='1', color='#F08080')
                p4,=plt.plot(drone4_x, drone4_y, "#191970", marker='*')

            if i<len(way_list[4]):
                path5_x = [way_list[4][j][0] for j in range(0,i)]
                path5_y = [way_list[4][j][1] for j in range(0,i)]
                drone5_x = way_list[4][i][0]
                drone5_y = way_list[4][i][1]
                plt.plot(path5_x, path5_y, linewidth='1', color='#F08080')
                p5,=plt.plot(drone5_x, drone5_y, "#191970", marker='*')

            if i<len(way_list[5]):
                path6_x = [way_list[5][j][0] for j in range(0,i)]
                path6_y = [way_list[5][j][1] for j in range(0,i)]
                drone6_x = way_list[5][i][0]
                drone6_y = way_list[5][i][1]
                plt.plot(path6_x, path6_y, linewidth='1', color='#F08080')
                p6,=plt.plot(drone6_x, drone6_y, "#191970", marker='*')

            if i<len(way_list[6]):
                path7_x = [way_list[6][j][0] for j in range(0,i)]
                path7_y = [way_list[6][j][1] for j in range(0,i)]
                drone7_x = way_list[6][i][0]
                drone7_y = way_list[6][i][1]
                plt.plot(path7_x, path7_y, linewidth='1', color='#F08080')
                p7,=plt.plot(drone7_x, drone7_y, "#191970", marker='*')

            if i<len(way_list[7]):
                path8_x = [way_list[7][j][0] for j in range(0,i)]
                path8_y = [way_list[7][j][1] for j in range(0,i)]
                drone8_x = way_list[7][i][0]
                drone8_y = way_list[7][i][1]
                plt.plot(path8_x, path8_y, linewidth='1', color='#F08080')
                p8,=plt.plot(drone8_x, drone8_y, "#191970", marker='*')


            i = i+1


            plt.pause(0.1)
            if i <= len(way_list[0]):
                p1.remove()
            if i <= len(way_list[1]):
                p2.remove()
            if i <= len(way_list[2]):
                p3.remove()
            if i <= len(way_list[3]):
                p4.remove()
            if i <= len(way_list[4]):
                p5.remove()
            if i <= len(way_list[5]):
                p6.remove()
            if i <= len(way_list[6]):
                p7.remove()
            if i <= len(way_list[7]):
                p8.remove()

            if i == max(length):
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
