
challengeToHalf = [10,25,50,100]
challengeTo24 = [200,450,700,1100,1800,2300,2900,3900,5000,5900,7200,8400,10000,11500,13000,15000,18000,20000,22000,25000,33000,41000,50000,62000]
challengeFull = challengeToHalf + challengeTo24
xp = [25,50,75,125,250,300,350,450,550,600,800,1000,1100,1250,1400,1600,2000,2100,2400,2800]
xptotal = 0


if input("Use previous settings? y/n\n") == "y":
    settings = open("encounterSettings.txt","r")
    plnum = int(settings.readline())
    print("Player Levels:", end = " ")
    for i in range(plnum-1):
        lvl = int(settings.readline())
        print(str(lvl), end = ", ")
        xptotal += xp[lvl-1]
    lvl = int(settings.readline())
    print(str(lvl))
    xptotal += xp[lvl-1]
    settings.close()
    ready = False
    while not ready:
        difficult = input("trivial, easy, medium, or hard, or deadly: ")
        if difficult in ["trivial", "easy","medium","hard","deadly"]:
            ready = True
    multiplier = 0
    if difficult == "trivial":
        multiplier = 1
    if difficult == "easy":
        multiplier = 2
    if difficult == "medium":
        multiplier = 3
    if difficult == "hard":
        multiplier = 4
    if difficult == "deadly":
        multiplier = 5
    xptotal *= multiplier

else:
    amount = int(input("Number of Players: "))
    settings = open("encounterSettings.txt","w")
    settings.write(str(amount)+"\n")
    for i in range(amount):
        num = int(input("".join(["Player ",str(i+1)," Level: "])))
        temp = xp[num]
        xptotal+=temp
        settings.write(str(num)+"\n")


    ready = False
    while not ready:
        difficult = input("trivial, easy, medium, or hard, or deadly: ")
        if difficult in ["trivial", "easy","medium","hard","deadly"]:
            ready = True
    multiplier = 0
    if difficult == "trivial":
        multiplier = 1
    if difficult == "easy":
        multiplier = 2
    if difficult == "medium":
        multiplier = 3
    if difficult == "hard":
        multiplier = 4
    if difficult == "deadly":
        multiplier = 5
    xptotal *= multiplier
    settings.close()
print("XP: ",xptotal)

def getMultiplier(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1.5
    elif num <= 6:
        return 2
    elif num <= 10:
        return 2.5
    elif num <= 14:
        return 3
    else:
        return 4

lvl = 0
for monsterXp in challengeFull:
    numMonsters = 1
    currentXp = numMonsters*monsterXp
    final = numMonsters
    while currentXp <= xptotal:
        final = numMonsters
        numMonsters += 1
        currentXp = numMonsters*monsterXp*getMultiplier(numMonsters)

    if monsterXp > xptotal:
        break
    if lvl == .125:
        print("CR 1/8:",final)
    elif lvl == .25:
        print("CR 1/4:",final)
    elif lvl == .5:
        print("CR 1/2:",final)
    else:
        print("CR ",int(lvl),":",final)
    if lvl == 0:
        lvl+=.125
    elif lvl < 2:
        lvl *= 2
    else:
        lvl+=1

mainLevel = input("Main Monster CR: ")
mainNum = int(input("Number of Main Monsters: "))
if mainLevel[0] not in ["0","1","2","3","4","5","6","7","8","9"]:
    exit(0)
if mainLevel=="0":
    mainLevel = challengeFull[0]
elif mainLevel=="1/8":
    mainLevel = challengeFull[1]
elif mainLevel=="1/4":
    mainLevel = challengeFull[2]
elif mainLevel=="1/2":
    mainLevel = challengeFull[3]
else:
    mainLevel = challengeFull[3+int(mainLevel)]


numFound = 0
lvl = 0
for monsterXp in challengeFull:
    numMonsters = 1+mainNum
    currentXp = (monsterXp+mainLevel*mainNum)*getMultiplier(numMonsters)
    final = numMonsters
    while currentXp <= xptotal:
        final = numMonsters - mainNum
        numMonsters += 1
        currentXp = ((numMonsters-1)*monsterXp+mainLevel*mainNum)*getMultiplier(numMonsters)
    if (monsterXp + mainLevel*mainNum)*getMultiplier(mainNum+mainNum) > xptotal:
        if monsterXp == 10:
            numFound+=1
        break
    if lvl == .125:
        print("CR 1/8: ",final)
    elif lvl == .25:
        print("CR 1/4: ",final)
    elif lvl == .5:
        print("CR 1/2: ",final)
    else:
        print("CR ",int(lvl),": ",final)
    if lvl == 0:
        lvl+=.125
    elif lvl < 2:
        lvl *= 2
    else:
        lvl+=1
if numFound>0:
    print("No other monsters found")
