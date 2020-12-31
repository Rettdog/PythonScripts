import numpy as np
import random
from node import node



"""Sample array: should take 5 steps"""
arr = [[[[1, 1, 1],
       [1, 1, 1],
       [1, 1, 1]],
      [[1, 1, 1],
       [1, 1, 1],
       [1, 1, 1]],
      [[1, 0, 1],
       [0, 0, 1],
       [1, 1, 1]]],

     [[[1, 0, 1],
       [0, 1, 1],
       [1, 0, 1]],
      [[1, 0, 1],
       [1, 1, 1],
       [1, 0, 1]],
      [[1, 0, 1],
       [0, 0, 1],
       [1, 0, 1]]],

     [[[1, 0, 1],
       [1, 0, 1],
       [1, 0, 1]],
      [[1, 1, 1],
       [1, 1, 1],
       [1, 1, 1]],
      [[1, 1, 1],
       [1, 1, 1],
       [1, 1, 1]]]]
start = [1,2,1,0]
end = [2,0,2,1]
x=start[0]
y=start[1]
z=start[2]
w=start[3]
n = 3

"""
This code creates a random 4 dimensional array, or a hyper-cube of values
with side length n, filled 75% with 0s and 25% with 1s. Then it uses BFS to calculate one of the shortest possible
paths in order to get from a randomly determined start and end points, only traveling on zeros.
"""

"""
generates the 4D array with 25% of the spaces being ones, the rest being zeros
comment below section if you want to use demo array
"""
def generateArray(n):
    nums = np.zeros((n,n,n,n))
    for i in range(int(n*n*n*n/4)):
        rand = [random.randint(0,n-1),random.randint(0,n-1),random.randint(0,n-1),random.randint(0,n-1)]
        if nums[rand[0],rand[1],rand[2],rand[3]] == 0:
            nums[rand[0],rand[1],rand[2],rand[3]] = 1

    return nums
    
arr = generateArray(n)

"""Generates random starting and ending points"""
while True:
    rand = [random.randint(0,n-1),random.randint(0,n-1),random.randint(0,n-1),random.randint(0,n-1)]
    if arr[rand[0]][rand[1]][rand[2]][rand[3]] == 0:
        start = [rand[0],rand[1],rand[2],rand[3]]
        break
while True:
    rand = [random.randint(0,n-1),random.randint(0,n-1),random.randint(0,n-1),random.randint(0,n-1)]
    if arr[rand[0]][rand[1]][rand[2]][rand[3]] == 0 and [rand[0],rand[1],rand[2],rand[3]] != start:
        end = [rand[0],rand[1],rand[2],rand[3]]
        break
searched = np.zeros((n,n,n,n))
print(arr)

"""Begins with the starting point and calls update on a created node (see node.py class)
and gets a list of the neighboring nodes that are viable moves that haven't been made yet"""
searched[x][y][z][w] = 1
queue = []
queue.append(node(x,y,z,w,0))
total = []
while True:
    nde = queue.pop(0)
    total.append(nde)

    input = nde.update(arr,searched,end)
    queue.extend(input)

    if len(queue) == 0:
        break
    # print("Popping")
    # print(nde.x,nde.y,nde.z,nde.w)
    # print("Adding:")
    # for i in input:
    #     print(i.x,i.y,i.z,i.w)
    # print("full list:")
    # for n in queue:
    #     print(str(n.x),str(n.y),str(n.z),str(n.w),str(n.counter))
    # print("going")
# print("done")

def getNeighbors(arr,x,y,z,w):
    out = []
    if x != 0:
            out.append([x-1,y,z,w])
    if x != len(arr)-1:
            out.append([x+1,y,z,w])
    if y != 0:
            out.append([x,y-1,z,w])
    if y != len(arr[0])-1:
            out.append([x,y+1,z,w])
    if z != 0:
            out.append([x,y,z-1,w])
    if z != len(arr[0][0])-1:
            out.append([x,y,z+1,w])
    if w != 0:
            out.append([x,y,z,w-1])
    if w != len(arr[0][0][0])-1:
            out.append([x,y,z,w+1])
    return out


"""Recursive method that travels backwards as the counter(moves from starting point) of the nodes decreases, creates path as it goes"""
def findPath(points,number,path):
    for i in points:
        if i.counter == number and [i.x,i.y,i.z,i.w] in getNeighbors(arr,path[0][0],path[0][1],path[0][2],path[0][3]):
            path.insert(0,[i.x,i.y,i.z,i.w])
            break
    if number <= 0:
        return path
    else:
        return findPath(points,number-1,path)

"""finds the end point to start findPath"""
found = False
for i in total:
    if [i.x,i.y,i.z,i.w] == end:
        final = findPath(total,i.counter-1,[end])
        # final.append(end)
        print("It took "+str(len(final)-1)+" steps to get from "+str(final[0])+" to "+str(final[-1]))
        print(final)
        found = True
        break
if not found:
    print("No solution found")
