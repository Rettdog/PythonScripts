import numpy as np

arr = [[[[0,0],[0,0]],[[0,0],[0,0]]],[[[0,0],[0,0]],[[0,0],[0,0]]]]
searched = [[[[0,0],[0,0]],[[0,0],[0,0]]],[[[0,0],[0,0]],[[0,0],[0,0]]]]
start = [0,0,0,0]
x=start[0]
y=start[1]
z=start[2]
w=start[3]
end = [1,1,1,0]

def getNeighbors(x,y,z,w):
    if x != 0:
    if x != len(arr)

def move(dimension,direction):
    if dimension==0:
        if searched[x+direction,y,z,w] == 0:
            x+=direction
            searched[x,y,z,w] = 1
            return True
    elif dimension==1:
        if searched[x,y+direction,z,w] == 0:
            y+=direction
            searched[x,y,z,w] = 1
            return True
    elif dimension==2:
        if searched[x,y,z+direction,w] == 0:
            z+=direction
            searched[x,y,z,w] = 1
            return True
    elif dimension==3:
        if searched[x,y,z,w+direction] == 0:
            w+=direction
            searched[x,y,z,w] = 1
            return True

    return False
