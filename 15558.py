import queue

Nk = input().split()
N = int(Nk[0])
k = int(Nk[1])
leftrow = list(input())
rightrow = list(input())

solvable = 0
start_node = ('left', 0, -1)
# [0] : left or right
# [1] : current index
# [2] : invalid

stack = list()
visited = list()
stack.append(start_node)

while stack:
    print(stack)
    node = stack.pop()
    if node not in visited:
        visited.append(node)
        left_or_right = node[0]
        curr_index = node[1]
        invalid_index = node[2]

        if curr_index + k >= N:
            solvable = 1
            break

        if left_or_right == 'left':
            if leftrow[curr_index + 1] == '1':
                stack.append(('left', curr_index + 1, invalid_index + 1))
            if rightrow[curr_index + k] == '1':
                stack.append(('right', curr_index + k, invalid_index + 1))
            if invalid_index + 1 < curr_index and leftrow[curr_index - 1] == '1':
                stack.append(('left', curr_index - 1, invalid_index + 1))
        
        if left_or_right == 'right':
            if rightrow[curr_index + 1] == '1':
                stack.append(('right', curr_index + 1, invalid_index + 1))
            if leftrow[curr_index + k] == '1':
                stack.append(('left', curr_index + k, invalid_index + 1))
            if invalid_index + 1 < curr_index and rightrow[curr_index - 1] == '1':
                stack.append(('right', curr_index - 1, invalid_index + 1))

print(solvable)
