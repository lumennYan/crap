
from behave import condition, action, FAILURE
from behave import repeat, forever, succeeder, failer
from behave import SUCCESS, FAILURE, RUNNING, BehaveException, \
                   action, condition


@condition
def toofar(x,y,others,R):
    length = len(others)
    for i in range(length):
        d = math.hypot(x - others[i].position_x, y - others[i].position_y)
        if d > R:
            print("too far")
            return True
        print("not too far")
        return False

@condition
def notnear(x,y,otherpath,r):
    for i in range(x-r,x+r):
            for j in range(y-r,self.y+r):
                if (i,j) in otherpath:
                    return False
                return True

@condition
def close(x,y,other,goal):
    own_dis = math.hypot(x - goal[0],y-goal[1])
    oth_dis = math.hypot(other.position_x - goal[0],other.position_y-goal[1])
    if own_dis > oth_dis:
        return False
    return True

@action
def go(acc_total,acc_tracking,acc_swarm):
    acc_total = acc_tracking + acc_swarm

@action
def slow(acc_total,acc_swarm):
    acc_total = -5 + acc_swarm