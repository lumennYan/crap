from astar import AStar
import drone
import multiprocessing
import plotting, env


from behave import condition, action, FAILURE
from behave import repeat, forever, succeeder, failer
from behave import SUCCESS, FAILURE, RUNNING, BehaveException, \
                   action, condition

def set_everything():
    start1 = (10, 7)
    goal = (70,70)
    start2 = (8,5)
    start3 = (8,9)
    start = [start1,start2,start3]
    drone1 = drone.Drone(start1,0)
    drone2 = drone.Drone(start2,1)
    drone3 = drone.Drone(start3,2)
    global uav_series
    uav_series = [drone1,drone2,drone3]
    drone1.neighbors = get_neighbors(drone1.index)
    drone2.neighbors = get_neighbors(drone2.index)
    drone3.neighbors = get_neighbors(drone3.index)

    astar1 = AStar(start1, goal, "euclidean")
    astar2 = AStar(start2, goal, "euclidean")
    astar3 = AStar(start3, goal, "euclidean")


    path1, visited = astar1.searching()
    path2, visited2= astar2.searching()
    path3, visited3= astar3.searching()
    print(path1)
    print(path2)
    print(path3)
    global uav_paths
    uav_paths = [path1,path2,path3]
    drone1.neighbors_path = get_otherpaths(drone1.index)
    drone2.neighbors_path = get_otherpaths(drone2.index)
    drone3.neighbors_path = get_otherpaths(drone3.index)
    print("done")

    with multiprocessing.Pool(processes=3) as pool:
        way1 = pool.apply_async(drone1.tracking, args=(path1, ))
        way1_list = way1.get()
        way2 = pool.apply_async(drone2.tracking, args=(path2, ))
        way2_list = way2.get()
        way3 = pool.apply_async(drone3.tracking, args=(path3, ))
        way3_list = way3.get()

    print(way1_list)
    print(way2_list)
    print(way3_list)
    plot = plotting.Plotting(start, goal)
    plot.animation(way1_list,way2_list,way3_list,"testing")

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
