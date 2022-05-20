from astar import AStar
import drone
import multiprocessing
import plotting, env
import time


goal = (280,280)
def set_everything():
    start = []
    start.append((10,7))
    start.append((8,4))
    start.append((8,10))
    start.append((6,7))
    start.append((2,7))
    start.append((8,12))
    start.append((10,12))
    start.append((6,12))
    #start.append((2,12))
    #start.append((2,4))
    #start.append((10,4))
    #start.append((6,4))
    global uav_series
    uav_series = []
    for i in range(8):
        uav_series.append(drone.Drone(start[i],i))
    astar = []
    visited = []
    global uav_paths
    uav_paths = []
    for i in range(8):
        uav_series[i].neighbors = get_neighbors(uav_series[i].index) 
        astar.append(AStar(start[i], goal, "euclidean"))
        path__,visited__ = astar[i].searching()
        uav_paths.append(path__)
        print(uav_paths[i])
        uav_series[i].neighbors_path = get_otherpaths(uav_series[i].index)

    print("done")

    manager = multiprocessing.Manager()
    share = manager.list()
    for i in range(8):
        share.append(start[i])
             
    start_time = time.time()
    print(start_time)
    way = []
    way_list = []
    with multiprocessing.Pool(processes=8) as pool:
        for i in range(8):
             way.append(pool.apply_async(uav_series[i].tracking, args=(uav_paths[i],share)))

        pool.close()
        pool.join()
    for i in range(8):
        way_list.append(way[i].get())

    end_time = time.time()
    print(end_time)
    print('running_time',end_time-start_time)
    for i in range(8):
        print(way_list[i])
    plot = plotting.Plotting(start, goal)
    plot.animation(way_list,"testing")

        #找朋友
def get_neighbors(index):
    neighbors = []
    for i in range(len(uav_series)):
        if i == index:
            pass
        else:
            neighbors.append(uav_series[i])
    return neighbors

        #找朋友的路
def get_otherpaths(index):
    paths = []
    for i in range(len(uav_paths)):
        if i == index:
            pass
        else:
            paths.append(uav_paths[i])
    return paths

