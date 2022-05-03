import math
from behave import condition, action, FAILURE
from behave import repeat, forever, succeeder, failer
from behave import SUCCESS, FAILURE, RUNNING, BehaveException, \
                   action, condition

#行为树用的节点
@condition
def toofar(obj):
    x = obj.position_x
    y = obj.position_y
    others = obj.share
    R = obj.R
    length = len(others)
    for i in range(length):
        d = math.hypot(x - others[i][0], y - others[i][1])
        if d > R:
            obj.lost = i
            print("too far")
            return True
        print("not too far")
        return False

@condition
def notnear(obj):
    x = obj.position_x
    y = obj.position_y
    r = obj.R
    otherpath = obj.lost_paths
    for i in range(x-r,x+r):
            for j in range(y-r,y+r):
                if (i,j) in otherpath:
                    print('near path')
                    return False
                print('not near path')
                return True

@condition
def close(obj):
    x = obj.position_x
    y = obj.position_y
    other = obj.share[obj.lost]
    goal = obj.goal
    own_dis = math.hypot(x - goal[0],y-goal[1])
    oth_dis = math.hypot(other[0] - goal[0],other[1]-goal[1])
    if own_dis > oth_dis:
        print('far from goal')
        return False
    print('close to goal')
    return True

@action
def go(obj):
    obj.acc_total = obj.acc_tracking + obj.acc_swarm

@action
def slow(obj):
    obj.acc_total = -0.5 + obj.acc_swarm