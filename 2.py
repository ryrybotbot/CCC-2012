data = input()
dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
out = 0
for x in range(0,len(data),2):
    if (x+3<len(data)):
        if(dict.get(data[x+3])>dict.get(data[x+1])):
            out -=int(data[x])*dict.get(data[x+1])
        else:
            out +=int(data[x])*dict.get(data[x+1])
    else:
        out +=int(data[x])*dict.get(data[x+1])
print(out)
