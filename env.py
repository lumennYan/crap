import numpy as np

class Env:
    def __init__(self):
        self.x_range = 75  # size of background
        self.y_range = 75
        self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def obs_map(self):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """

        x = self.x_range
        y = self.y_range
        obs = set()

        #generate walls around the map
        for i in range(x):
            obs.add((i, 0))
        for i in range(x):
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
        for i in range(y):
            obs.add((x - 1, i))

        for i in range(25, 35):
            for j in range(25,35):
                obs.add((i, j))
        for i in range(42, 55):
            for j in range(28,41):
                obs.add((i, j))
        for i in range(51, 56):
            for j in range(56,65):
                obs.add((i, j))
        return obs