baseX = int(input("baseX: "))
baseY = int(input("baseY: "))
num = int(input("Number in BaseX: "))

#chr(97) = 'a'
#ord("a")-97+11 = 11

def ten2twelve(a):
    b = int(a)//12; c = (int(a)-b*12)
    if b > 9: b = ten2twelve(b)
    if b == 0: b = ""
    if c > 9:
        if c == 10: return str(b)+"X"
        else: return str(b)+"E"
    return str(b)+str(c)

def ten2baseX(a,x):
    b = int(a)//x; c = (int(a)-b*x)
    if b > 9: b = ten2twelve(b)
    if b == 0: b = ""
    if c > 9:
        if c == 10: return str(b)+"X"
        else: return str(b)+"E"
    return str(b)+str(c)

def add(a,b,base):
    for i in range(int(b)):
        #check if a will overflow (ord("value")), then add one to end value
        if
        a += 1

def addArrInBase(nums,base):
    for i in
