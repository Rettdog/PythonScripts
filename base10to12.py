class base12Switcher:
    def _init_(self):
        ogStr = input("Base 10:")
        ogNum = int(ogStr)
        out = "0"
        for i in range(ogNum):
            index = -1
            while(True):
                next = self.getNext(out[index])
                out = list(out)
                out[len(out)+index] = next
                out = self.strFromArray(out)
                if next == "0" :
                    if -1*index == len(out):
                        out = "0"+out
                    index -=1
                else:
                    break
        print(out)

    def strFromArray(self,arr):
        out = ""
        for i in arr:
            out += i
        return out

    def getNext(self,str):
        if str == "0":
            return "1"
        elif str == "1":
            return "2"
        elif str == "2":
            return "3"
        elif str == "3":
            return "4"
        elif str == "4":
            return "5"
        elif str == "5":
            return "6"
        elif str == "6":
            return "7"
        elif str == "7":
            return "8"
        elif str == "8":
            return "9"
        elif str == "9":
            return "X"
        elif str == "X":
            return "E"
        elif str == "E":
            return "0"

thing = base12Switcher()
thing._init_()
