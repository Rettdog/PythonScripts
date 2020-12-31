import numpy as np

class Field:
    def __init__(self,worldSize=15,fieldSize=3):
        if worldSize >= 4:
            self.worldSize = worldSize
        else:
            raise Exception("worldSize must be greater than or equal to 4.")
        if fieldSize >= 3:
            self.fieldSize = fieldSize
        else:
            raise Exception("fieldSize must be greater than or equal to 3.")
        if fieldSize > worldSize//2:
            raise Exception("worldSize must be at least double fieldSize.")
        self.world = np.random.choice(self.worldSize**2,self.worldSize**2,replace=False)
        self.world = self.world + 1
        self.world.shape = self.worldSize,self.worldSize
        self.moves = 0
        self.stop = True
        self.complete = np.arange(1,(self.worldSize**2)+1)
        self.complete.shape = self.worldSize,self.worldSize
        self.x = self.worldSize//2 + self.worldSize%2 - 1
        self.y = self.worldSize//2 + self.worldSize%2 - 1
        self.xpos = self.x
        self.ypos = self.y
        self.moves = 0
        self.stop = False
        self.grabbed = np.array([],int)

    def grab(self):
        self.grabbed = np.array(self.field)
        self.grabbedCoords = self.y, self.x
        self.moves += 1

    def swap(self):
        try:
            if abs(self.y-self.grabbedCoords[0]) < self.fieldSize and abs(self.x-self.grabbedCoords[1]) < self.fieldSize:
                raise Exception("Grabbed field and swapped field cannot overlap.")
            else:
                cache = np.array(self.world[self.y-(self.fieldSize//2):self.y+(self.fieldSize//2+1),self.x-(self.fieldSize//2):self.x+(self.fieldSize//2+1)])
                self.world[self.y-(self.fieldSize//2):self.y+(self.fieldSize//2+1),self.x-(self.fieldSize//2):self.x+(self.fieldSize//2+1)] = self.grabbed
                self.world[self.grabbedCoords[0]-(self.fieldSize//2):self.grabbedCoords[0]+(self.fieldSize//2+1),self.grabbedCoords[1]-(self.fieldSize//2):self.grabbedCoords[1]+(self.fieldSize//2+1)] = cache
                self.field = self.world[self.y-(self.fieldSize//2):self.y+(self.fieldSize//2+1),self.x-(self.fieldSize//2):self.x+(self.fieldSize//2+1)]
                self.moves += 1
        except AttributeError:
            raise Exception("Swapping requires 2 positions, not 1.")
        except Exception as e:
            print(e)

    def check(self):
        if np.all(self.world == self.complete):
            print("All numbers have been organized!")
            print("Moves:",self.moves)

    @property
    def xpos(self):
        return self.x

    @xpos.setter
    def xpos(self,val):
        if abs(val-self.x) <= self.fieldSize and (val >= self.fieldSize//2 and val < np.size(self.world, 1)-self.fieldSize//2):
            self.x = val
            self.field = self.world[self.y-(self.fieldSize//2):self.y+(self.fieldSize//2+1),self.x-(self.fieldSize//2):self.x+(self.fieldSize//2+1)]
            self.moves += 1
            if not self.stop:
                self.check()
        else:
            raise Exception("Illegal move.")

    @property
    def ypos(self):
        return self.y

    @ypos.setter
    def ypos(self,val):
        if abs(val-self.y) <= self.fieldSize and (val >= self.fieldSize//2 and val < np.size(self.world, 0)-self.fieldSize//2):
            self.y = val
            self.field = self.world[self.y-(self.fieldSize//2):self.y+(self.fieldSize//2+1),self.x-(self.fieldSize//2):self.x+(self.fieldSize//2+1)]
            self.moves += 1
            if not self.stop:
                self.check()
        else:
            raise Exception("Illegal move.")
