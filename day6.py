initial_state = '5,1,5,3,2,2,3,1,1,4,2,4,1,2,1,4,1,1,5,3,5,1,5,3,1,2,4,4,1,1,3,1,1,3,1,1,5,1,5,4,5,4,5,1,3,2,4,3,5,3,5,4,3,1,4,3,1,1,1,4,5,1,1,1,2,1,2,1,1,4,1,4,1,1,3,3,2,2,4,2,1,1,5,3,1,3,1,1,4,3,3,3,1,5,2,3,1,3,1,5,2,2,1,2,1,1,1,3,4,1,1,1,5,4,1,1,1,4,4,2,1,5,4,3,1,2,5,1,1,1,1,2,1,5,5,1,1,1,1,3,1,4,1,3,1,5,1,1,1,5,5,1,4,5,4,5,4,3,3,1,3,1,1,5,5,5,5,1,2,5,4,1,1,1,2,2,1,3,1,1,2,4,2,2,2,1,1,2,2,1,5,2,1,1,2,1,3,1,3,2,2,4,3,1,2,4,5,2,1,4,5,4,2,1,1,1,5,4,1,1,4,1,4,3,1,2,5,2,4,1,1,5,1,5,4,1,1,4,1,1,5,5,1,5,4,2,5,2,5,4,1,1,4,1,2,4,1,2,2,2,1,1,1,5,5,1,2,5,1,3,4,1,1,1,1,5,3,4,1,1,2,1,1,3,5,5,2,3,5,1,1,1,5,4,3,4,2,2,1,3'
state = [int(i) for i in initial_state.split(',')]

def sim(state):
    new = []
    new_lanternfish = 0
    for i in state:
        if i!=0:
            new.append(i-1)
        else:
            new.append(6)
            new_lanternfish += 1
    for i in range(new_lanternfish): new.append(8)
    return new

def sim_len(state, nSims):
    for i in state:
        x = ((nSims-i)//7)+1



"""for i in range(256):
    state = sim(state)
print(len(state))"""
time_limit = 256
fishes = state
breeding_cycle = [0]*7
for fish in fishes:
    breeding_cycle[fish%7] += 1

baby_rotate = [0]*9
for i in range(time_limit):
    breeding_cycle[i%7] +=baby_rotate[0]
    baby_rotate[0] = breeding_cycle[i%7]
    baby_rotate.append(baby_rotate[0])
    baby_rotate.pop(0)
print(sum(breeding_cycle) + sum(baby_rotate))