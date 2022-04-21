from utils import read

input = read()

input = [int(x) for x in input]

c = 0
for i in range(1, len(input)):
    if input[i]>input[i-1]:
        c+=1
print(c)

c=0
for i in range(1, len(input)-2):
    if input[i-1]+input[i]+input[i+1]<input[i]+input[i+1]+input[i+2]:
        c+=1
print(c)