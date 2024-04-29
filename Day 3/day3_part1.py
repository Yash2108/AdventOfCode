with open('./Day 3/input.txt', 'r+') as infile:
    input_lines=[[l for l in line.strip()] for line in infile.readlines()]

    
def check_l(array, idx1, idx2):
    if array[idx1][idx2-1] in '1234567890.':
        return False
    else: 
        return True
    
def check_r(array, idx1, idx2):
    if array[idx1][idx2+1] in '1234567890.':
        return False
    else: 
        return True
    
def check_t(array, idx1, idx2):
    if array[idx1-1][idx2] in '1234567890.':
        return False
    else: 
        return True
    
def check_b(array, idx1, idx2):
    if array[idx1+1][idx2] in '1234567890.':
        return False
    else: 
        return True
    
def check_tl(array, idx1, idx2):
    if array[idx1-1][idx2-1] in '1234567890.':
        return False
    else: 
        return True
    
def check_tr(array, idx1, idx2):
    if array[idx1-1][idx2+1] in '1234567890.':
        return False
    else: 
        return True
    
def check_bl(array, idx1, idx2):
    if array[idx1+1][idx2-1] in '1234567890.':
        return False
    else: 
        return True
    
def check_br(array, idx1, idx2):
    if array[idx1+1][idx2+1] in '1234567890.':
        return False
    else: 
        return True
    
total=0
max_i=len(input_lines)
max_j=len(input_lines[0])
for i in range(max_i):
    for j in range(max_j):
        if input_lines[i][j].isdigit():
            if i==0:
                if j==0:
                    if check_r(input_lines, i, j) or check_br(input_lines, i, j) or check_b(input_lines, i, j):
                        continue
                elif j==max_j-1:
                    if check_l(input_lines, i, j) or check_bl(input_lines, i, j) or check_b(input_lines, i, j):
                        continue
                else:
                    if check_bl(input_lines, i, j) or check_br(input_lines, i, j) or check_b(input_lines, i, j) or check_r(input_lines, i, j):
                        continue

            elif i==max_i-1:
                if j==0:
                    if check_r(input_lines, i, j) or check_tr(input_lines, i, j) or check_t(input_lines, i, j):
                        continue                    
                elif j==max_j-1:
                    if check_l(input_lines, i, j) or check_tl(input_lines, i, j) or check_t(input_lines, i, j):
                        continue
                else:
                    if check_l(input_lines, i, j) or check_tl(input_lines, i, j) or check_t(input_lines, i, j) or check_tr(input_lines, i, j) or check_r(input_lines, i, j):
                        continue
            else:
                if j==0:
                    if check_t(input_lines, i, j) or check_tr(input_lines, i, j) or check_r(input_lines, i, j) or check_br(input_lines, i, j) or check_b(input_lines, i, j):
                        continue
                elif j==max_j-1:
                    if check_t(input_lines, i, j) or check_tl(input_lines, i, j) or check_l(input_lines, i, j) or check_bl(input_lines, i, j) or check_b(input_lines, i, j):
                        continue
                else:
                    if check_t(input_lines, i, j) or check_tl(input_lines, i, j) or check_l(input_lines, i, j) or check_bl(input_lines, i, j) or check_b(input_lines, i, j) or check_br(input_lines, i, j) or check_r(input_lines, i, j) or check_tr(input_lines, i, j):
                        continue

            
            total+=int(input_lines[i][j])

print(total)