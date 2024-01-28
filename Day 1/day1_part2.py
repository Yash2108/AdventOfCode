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
    # '0':'0',
    # '1':'1',
    # '2':'2',
    # '3':'3',
    # '4':'4',
    # '5':'5',
    # '6':'6',
    # '7':'7',
    # '8':'8',
    # '9':'9'
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
        
    # for num_text in num_map:
    #     if num_text in line:
    #         idxs.append([num_text, line.rfind(num_text)])
    idxs=sorted(idxs, key=lambda k: k[1])
    # print(idxs)
    final_val+= int(idxs[0][0]+idxs[-1][0])
    final_nums.append(int(idxs[0][0]+idxs[-1][0]))

# with open('./Day 1/txt2.txt', 'r+') as outfile:
#     outfile.write(str(final_nums))
print(final_val)