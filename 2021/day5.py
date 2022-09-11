from general.utils import read

input = read()
lines = input.split('\n')

biggestX = 0
biggestY = 0
for line in lines:
    linedata = line.split(' -> ')
    x1, y1 = linedata[0].split(',')
    x2, y2 = linedata[1].split(',')
    
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    if x1 > biggestX: biggestX = x1
    if x2 > biggestX: biggestX = x2
    if y1 > biggestY: biggestY = y1
    if y2 > biggestY: biggestY = y2

basic = [[0 for j in range(biggestX+1)] for i in range(biggestY+1)]

for line in lines:
    linedata = line.split(' -> ')
    x1, y1 = linedata[0].split(',')
    x2, y2 = linedata[1].split(',')
    
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

    if x1==x2:
        if y1<y2:
            for ycor in range(y1, y2+1):
                basic[ycor][x1] +=1
        else:
            for ycor in range(y2, y1+1):
                basic[ycor][x1] +=1
            
    elif y1==y2:
        if x1<x2:
            for xcor in range(x1, x2+1):
                basic[y1][xcor] +=1
        else:
            for xcor in range(x2, x1+1):
                basic[y1][xcor] +=1
    elif abs(x1-x2) == abs(y1-y2):
        if x1<x2 and y1<y2:
            xdelta = x1
            for ycor in range(y1, y2+1):
                basic[ycor][xdelta] +=1
                xdelta +=1
        elif x1<x2 and y1>y2:
            xdelta = x2
            for ycor in range(y2, y1+1):
                basic[ycor][xdelta] +=1
                xdelta -=1
        elif x1>x2 and y1<y2:
            xdelta = x1
            for ycor in range(y1, y2+1):
                basic[ycor][xdelta] +=1
                xdelta -=1
        elif x1>x2 and y1>y2:
            xdelta = x2
            for ycor in range(y2, y1+1):
                basic[ycor][xdelta] +=1
                xdelta +=1



c=0
for i in basic:
    for j in i:
        if j>=2:
            c+=1
print(c)