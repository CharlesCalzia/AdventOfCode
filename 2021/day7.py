from general.utils import read
from statistics import mean


input = read()
line = input.strip()

def fuel(x):
    return sum(list(range(0,x+1)))

crabs = [int(i) for i in line.split(',')]

minMean = max(crabs)*100000
ans = ''
minFuel = 0
for i in range(min(crabs), max(crabs) + 1):
    crabTransform = [fuel(abs(i-j)) for j in crabs]
    meanCrab = mean(crabTransform)
    if meanCrab < minMean:
        minMean = meanCrab
        minFuel = sum(crabTransform)



print(minFuel)