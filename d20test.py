
bonus = int(input("Enter Bonus: "))
DC = int(input("Enter DC: "))
advantageSum = 0;
advArr = []
disadvantageSum = 0;
disArr = []
normalSum = 0;
normArr = []
for i in range(1+bonus,21+bonus):
    normalSum+=i
    normArr.append(i)
    for j in range(1+bonus,21+bonus):
        if i<=j:
            disadvantageSum+=i
            disArr.append(i)
            advantageSum+=j
            advArr.append(j)
        else:
            advantageSum+=i
            advArr.append(i)
            disadvantageSum+=j
            disArr.append(j)
print("")
print("Normal Average: ", normalSum/20)
print("Average with Advantage: ",advantageSum/400)
print("Average with Disadvantage: ",disadvantageSum/400)
print("")

successes = 0;
for num in normArr:
    if num>=DC:
        successes+=1
percent = successes/len(normArr)

print("Normal Success Rate: ", round(percent*100,1),"%")

successes = 0;
for num in advArr:
    if num>=DC:
        successes+=1
percent = successes/len(advArr)

print("Advantage Success Rate: ", round(percent*100,2),"%")

successes = 0;
for num in disArr:
    if num>=DC:
        successes+=1
percent = successes/len(disArr)

print("Disadvantage Success Rate: ", round(percent*100,2),"%")

print("")

crits = 0;
for num in normArr:
    if num-bonus==20:
        crits+=1
percent = crits/len(normArr)

print("Normal Crit Chance: ", round(percent*100,1),"%")

crits = 0;
for num in advArr:
    if num-bonus==20:
        crits+=1
percent = crits/len(advArr)

print("Advantage Crit Chance: ", round(percent*100,2),"%")

crits = 0;
for num in disArr:
    if num-bonus==20:
        crits+=1
percent = crits/len(disArr)

print("Disadvantage Crit Chance: ", round(percent*100,2),"%")
