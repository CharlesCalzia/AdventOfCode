from general.utils import read

input = read()
grids = input.split('\n\n')
boards = []

for grid in grids:
    board = []
    for row in grid.split('\n'):
        board.append([int(i) for i in row.strip().replace('  ',' ').split(' ')])
    boards.append(board)

nums_called = '94,21,58,16,4,1,44,6,17,48,20,92,55,36,40,63,62,2,47,7,46,72,85,24,66,49,34,56,98,41,84,23,86,64,28,90,39,97,73,81,12,69,35,26,75,8,32,77,52,50,5,96,14,31,70,60,29,71,9,68,19,65,99,57,54,61,33,91,27,78,43,95,42,3,88,51,53,30,89,87,93,74,18,15,80,38,82,79,0,22,13,67,59,11,83,76,10,37,25,45'
#nums_called='7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1'
nums = [int(i) for i in nums_called.split(',')]
pointer = 4
picked = nums[:4]
complete = False
while True:
    try: picked.append(nums[pointer])
    except:
        print(boards)
        print(len(boards))
        break
    done = False
    rems = []
    for b in range(len(boards)):
        board = boards[b]
        for row in range(len(board)):
            if board[row][0] in picked and board[row][1] in picked and board[row][2] in picked and board[row][3] in picked and board[row][4] in picked:
                if len(boards)==1: 
                    final = nums[pointer]
                    complete = True
                    break
                if board not in rems: rems.append(board)
                
                print('row')
                done = True
            if board[0][row] in picked and board[1][row] in picked and board[2][row] in picked and board[3][row] in picked and board[4][row] in picked:
                #print(board)
                if len(boards)==1: 
                    final =nums[pointer]
                    complete = True
                    break
                if board not in rems: rems.append(board)
                
                print('col')
                done = True
                
    for i in rems: 
        
        boards.remove(i)
    if complete: break
    pointer += 1
                        


    #for board in boards:
    #    for row in board:
    #        if row==nums[pointer-4:pointer]:
sumUnmarked = 0
board = boards[0]
print(board)
for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] not in picked:
            sumUnmarked += board[row][col]
            

print(final*sumUnmarked)          
