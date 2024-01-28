with open("./Day 1/input.txt", 'r+') as infile:
    input_lines=infile.readlines()
    input_lines=[line.strip() for line in input_lines]

final_val=0
for line in input_lines:
    nums=[]
    for char in line:
        if char.isnumeric():
            nums.append(char)
    final_val+=int(nums[0]+nums[-1])
print(final_val)

