from general.utils import read

input = read()
len1 = len(input[0])

def setup(input):
    lists = [[] for i in range(len1)]
    for i in range(len1):
        for j in range(i, len(''.join(input)), len1):
            lists[i].append(''.join(input)[j])
    return lists
lists = setup(input)

def gam(lists):
    gamma = ''
    epsilon=''
    for i in lists:
        x = ''.join(i)
        if x.count('1')>=x.count('0'):
            gamma+='1'
            epsilon+='0'
        else:
            gamma+='0'
            epsilon+='1'
    #print(int('0b'+gamma,2)*int('0b'+epsilon,2))
    return gamma

def eps(lists):
    gamma = ''
    epsilon=''
    for i in lists:
        x = ''.join(i)
        if x.count('1')>=x.count('0'):
            gamma+='1'
            epsilon+='0'
        else:
            gamma+='0'
            epsilon+='1'
    #print(int('0b'+gamma,2)*int('0b'+epsilon,2))
    return epsilon



new_list1 = list(input)
#new_list2 = list(input)
for i in range(len1):
    lists = setup(''.join(new_list1))
    gamma = gam(lists)
    rems = []
    for j in new_list1:
        if gamma[i]=='1' and j[i]!='1':
            rems.append(j)
        elif gamma[i]=='0' and j[i]!='0':
            rems.append(j)
    for j in rems:
        new_list1.remove(j)
    if len(new_list1)==1:
        break
new_list2 = list(input)
for i in range(len1):
    lists = setup(''.join(new_list2))
    epsilon = eps(lists)
    rems = []
    for j in new_list2:
        if epsilon[i]=='1' and j[i]!='1':
            rems.append(j)
        elif epsilon[i]=='0' and j[i]!='0':
            rems.append(j)
    for j in rems:
        new_list2.remove(j)
    if len(new_list2)==1:
        break
print(int(new_list2[0],2)*int(new_list1[0],2))