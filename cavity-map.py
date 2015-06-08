def cavity_map(matrix):
    save_list = []
    eval_nums = []

    for i in range(len(matrix)):
            if i != 0 and i != len(matrix)-1:
                    for q in range(len(matrix[i])):
                            if q != 0 and q != len(matrix[i])-1:
                                    eval_nums.append((i,q))
                                   
    for indexer in range(len(eval_nums)):
        a,b = eval_nums[indexer][0], eval_nums[indexer][1]
        if all(q < matrix[a][b] for q in [matrix[a-1][b], matrix[a+1][b], matrix[a][b-1], matrix[a][b+1]]):
            save_list.append((a,b))
            
    for item in save_list:
        matrix[item[0]][item[1]] = 'X'

    for row in range(len(matrix)):
        print ''.join(map(str,matrix[row]))

test_cases = int(raw_input().strip())

M = []
for i in range(test_cases):
    input_row = [int(i) for i in raw_input().strip()]
    M.append(input_row)

cavity_map(M)
