import random as r
import time as t
rolls = []
sum = 0
min = 10
max = 10
# for i in range(1000000):
#     rolls.append(r.randint(1,20))
#     while rolls[i]==1:
#        rolls[i] = r.randint(1,21)
    # if min>rolls[i]:
    #     min = rolls[i]
    # if max<rolls[i]:
    #     max = rolls[i]
    # sum +=rolls[i]
    # print(sum/len(rolls))
    # print("Min: ",min," Max: ",max)
percent = 0
for j in range(1,10000):
    sub = 1
    for k in range(j):
        sub*=1/20
    percent+=sub
    t.sleep(.4)
    print(percent)
