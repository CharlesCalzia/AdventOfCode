from general.utils import read
input = read()

def solve(series):
    inp = series.split(' | ')[0].split(' ')
    out = series.split(' | ')[1].split(' ')

    c = 0
    for i in out:
        if len(i)==3:
            c+=1
        elif len(i)==4:
            c+=1
        elif len(i)==2:
            c+=1
        elif len(i)==7:
            c+=1
    return c
total = 0
for i in input.split('\n'):
    x = solve(i)
    total+=x
print(total)
