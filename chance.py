import numpy as np
import random

odds = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def arrSum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

def getOdds():
    count = 0
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                for l in range(1,7):
                    count+=1
                    # print(str(i)+str(j)+str(k)+str(l))
                    nums = [i,j,k,l]
                    nums.sort()
                    nums.pop(0)
                    sum = 0
                    for m in nums:
                        sum += m
                    odds[sum] += 1

    for i in range(len(odds)):
        # out[i] = str(i)+": "+str(round(out[i]/(count)*100,2))+"%"
        odds[i] = odds[i]/(count)*100
    odds.pop(0)
    odds.pop(0)
    odds.pop(0)

def getCharacter():
    rolls = []
    for i in range(6):
        rolls.extend(random.choices(range(3,19),odds))
    rolls.sort()
    return rolls

def generateRollList():
    out = []
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                for l in range(1,7):
                    nums = [i,j,k,l]
                    nums.sort()
                    nums.pop(0)
                    out.append(arrSum(nums))
    return out

def getAverage(list):
    return arrSum(list)/len(list)

def generateCharSums():
    out = [0] * 120
    sums = []
    list = generateRollList()
    for i in list:
        for j in list:
            for k in list:
                for l in list:
                    for m in list:
                        for n in list:
                            sum = i+j+k+l+m+n
                            out[sum] += 1
                            sums.append(sum)
                            print(sum)
    for i in range(len(out)):
        out[i] = str(i)+": "+str(out[i])
        print(out)
    average = arrSum(sums)/len(sums)
    print(average)

def getExamples():
    chars = []
    sums = []
    counter = 0
    # for j in range(10000):
    while (True):
        counter +=1
        rolls = []
        for i in range(6):
            rolls.extend(random.choices(range(3,19),out))
        # rolls.sort()
        if rolls == [18,18,18,18,18,18]:
            break;
        # print(rolls)
        # rolls.insert(0,arrSum(rolls))
        # chars.append(rolls)
    print("it took "+counter+" times to get [18,18,18,18,18,18]")
    # for i in chars:

        # i.pop(0)
    chars.sort()
    sums.sort()
    print(chars[-10:-1])
# print(out)

#getOdds()
print(6*getAverage(generateRollList()))
# generateCharSums()
# generateCharSums()
# print(getAverage(generateRollList())*5)
