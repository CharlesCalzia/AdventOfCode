from utils import read
input = read(6)

groups = input.split('\n\n')

## Part 1

sum_counts = 0

for group in groups:
    group_answers = list(set(list(group.replace('\n',''))))
    sum_counts += len(group_answers)

print(sum_counts)

# Part 2

sum_counts = 0
for group in groups:
    group_answers = [set(list(person)) for person in group.split('\n')]
    group_all_agree = set.intersection(*group_answers)
    sum_counts += len(group_all_agree)

print(sum_counts)