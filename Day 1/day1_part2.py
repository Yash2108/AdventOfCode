with open("./Day 1/input.txt", 'r+') as infile:
    input_lines=infile.readlines()
    input_lines=[line.strip() for line in input_lines]

num_map={
    'zero': '0', 
    'one': '1', 
    'two': '2', 
    'three': '3', 
    'four': '4', 
    'five': '5', 
    'six': '6', 
    'seven': '7', 
    'eight': '8', 
    'nine': '9',
}

final_val=0
final_nums=[]
for line in input_lines:
    idxs=[]
    for idx, char in enumerate(line):
        if char.isdigit():
            idxs.append([char, idx])
        else: 
            for num_text in num_map:
                if line[idx:].startswith(num_text):
                    idxs.append([num_map[num_text], idx])
    idxs=sorted(idxs, key=lambda k: k[1])
    final_val+= int(idxs[0][0]+idxs[-1][0])
    final_nums.append(int(idxs[0][0]+idxs[-1][0]))

print(final_val)