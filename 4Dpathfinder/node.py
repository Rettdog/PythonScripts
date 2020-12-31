
class node:
    """
    Node class holds the position at a certain point in the array and
    assigns it a value based on how many moves from the starting point it is
    which allows us to get a full list of nodes with their distances
    and then can backtrack through to find path.
    Mostly a storage for values but has methods for getting neighboring positions and
    creating them as nodes to add to the queue
    """
    def __init__(self,x,y,z,w,counter):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.counter = counter
        """
        Makes sure that position doesn't have a one or has been searched previously
        """
    def checkLegalMove(self,x,y,z,w,arr,searched):
        if arr[x][y][z][w] != 0:
            return False
        if searched[x][y][z][w] != 0:
            return False
        return True
    """
    Finds neighboring nodes/positions
    Boundary Checking and blockade checking(1s)
    Searched is set to one at a position when added to queue in order to prevent loops
    """
    def getNeighbors(self,arr,searched):
        out = []
        if self.x != 0:
            if self.checkLegalMove(self.x-1,self.y,self.z,self.w,arr,searched):
                out.append([self.x-1,self.y,self.z,self.w])
                searched[self.x-1][self.y][self.z][self.w] = 1
        if self.x != len(arr)-1:
            if self.checkLegalMove(self.x+1,self.y,self.z,self.w,arr,searched):
                out.append([self.x+1,self.y,self.z,self.w])
                searched[self.x+1][self.y][self.z][self.w] = 1
        if self.y != 0:
            if self.checkLegalMove(self.x,self.y-1,self.z,self.w,arr,searched):
                out.append([self.x,self.y-1,self.z,self.w])
                searched[self.x][self.y-1][self.z][self.w] = 1
        if self.y != len(arr[0])-1:
            if self.checkLegalMove(self.x,self.y+1,self.z,self.w,arr,searched):
                out.append([self.x,self.y+1,self.z,self.w])
                searched[self.x][self.y+1][self.z][self.w] = 1
        if self.z != 0:
            if self.checkLegalMove(self.x,self.y,self.z-1,self.w,arr,searched):
                out.append([self.x,self.y,self.z-1,self.w])
                searched[self.x][self.y][self.z-1][self.w] = 1
        if self.z != len(arr[0][0])-1:
            if self.checkLegalMove(self.x,self.y,self.z+1,self.w,arr,searched):
                out.append([self.x,self.y,self.z+1,self.w])
                searched[self.x][self.y][self.z+1][self.w] = 1
        if self.w != 0:
            if self.checkLegalMove(self.x,self.y,self.z,self.w-1,arr,searched):
                out.append([self.x,self.y,self.z,self.w-1])
                searched[self.x][self.y][self.z][self.w-1] = 1
        if self.w != len(arr[0][0][0])-1:
            if self.checkLegalMove(self.x,self.y,self.z,self.w+1,arr,searched):
                out.append([self.x,self.y,self.z,self.w+1])
                searched[self.x][self.y][self.z][self.w+1] = 1
        return out
    """
    Called in queue loop in 4Dpathfinder.py
    Finds the neighbors of the node and returns a list of them
    """

    def update(self,arr,searched,end):
        # if [self.x,self.y,self.z,self.w] == end:
        out = []
        for i in self.getNeighbors(arr,searched):
            out.append(node(i[0],i[1],i[2],i[3],self.counter+1))
        # print("update")
        return out
