from utils import read

input = read()

x = 0
y = 0
aim = 0
for inp in input:
    inpSplit = inp.split(' ')
    direction = inpSplit[0]
    magnitude = int(inpSplit[1])
    if direction=="forward": 
        x+=magnitude
        y+=(aim*magnitude)
    elif direction=="up": aim-=magnitude
    elif direction=="down": aim+=magnitude
print(abs(x*y))