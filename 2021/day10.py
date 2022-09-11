from general.utils import read
input = read().split('\n')

def inverse(pos):
    if pos=='<': return '>'
    elif pos=='(': return ')'
    elif pos=='[': return ']'
    elif pos=='{': return '}'
    elif pos=='>': return '<'
    elif pos==')': return '('
    elif pos==']': return '['
    elif pos=='}': return '{'
    else: return pos

points = 0
for inp in input:
    current = inp
    startPointer = 0
    endPointer = len(inp)
    while True:
        if inverse(inp[startPointer])==inp[endPointer]:
            del current[startPointer]
            del current[endPointer]
        endPointer -=1


        first = input[inp][0]
        last = input[inp][-1]
        if first!=last:
            print(last, points)
            if last==')': points+=3
            elif last==']': points+=57
            elif last=='}': points+=1197
            elif last=='>': points+=25137
        else:
            input[inp]=input[inp][1:-1]
    print(points)