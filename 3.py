data = [0]*1001
size = int(input())
for k in range(size):
    data[int(input())]+=1
mostf = []
num1 = 0
secf = []
num2 = 0
for k in range(len(data)):
    if (data[k]>num1):
        secf.clear()
        num2 = num1
        secf=mostf[:]
        mostf.clear()

        num1=data[k]
        mostf+=[k]
    elif (data[k]== num1):
        mostf+=[k]
    elif(data[k] > num2):
        secf.clear()
        num2=data[k]
        secf+=[k]
    elif(data[k]>0 and data[k]==num2):
        secf+=[k]
maxdiff = 0
for y in range(len(mostf)):
    for x in range(y+1,len(mostf)):
        if(maxdiff < max(mostf[y]-mostf[x],mostf[x]-mostf[y])):
            maxdiff = max(mostf[y]-mostf[x],mostf[x]-mostf[y])
if (maxdiff == 0):
    for y in range(len(mostf)):
        for x in range(len(secf)):
            if(maxdiff < max(mostf[y]-secf[x],secf[x]-mostf[y])):
                maxdiff = max(mostf[y]-secf[x],secf[x]-mostf[y])

print(maxdiff)
