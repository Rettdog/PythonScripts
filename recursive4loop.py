arr = []
out = []

def recurse(depth, length, arr, out):
    for i in range(length):
        if i not in arr:
            outarr = list(arr)
            if depth != 0:
                outarr.append(i)
                recurse(depth-1,length,outarr,out)
            else:
                outarr.sort()
                if outarr not in out:
                    out.append(outarr)
                break
    return out

def getBlockCombos(depth, length, arr, out):
    for i in range(1,depth+1):
        recurse(i,length,arr,out)
    print(out)

getBlockCombos(6,25, arr, out)
