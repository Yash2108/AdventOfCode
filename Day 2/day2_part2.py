with open('./Day 2/input.txt', 'r+') as infile:
    input_lines=[line.strip() for line in infile.readlines()]

input_lines=[line.split(':') for line in input_lines]
input_lines=[[game.strip() for game in line[1].split(';')] for line in input_lines]

total=0

for line in input_lines:
    min_cubes={
        'green':0,
        'red':0,
        'blue':0
    }

    for game in line:
        game=game.split(', ')
        for cube in game:
            cube=cube.split(' ')
            if min_cubes[cube[1]]<int(cube[0]):
                min_cubes[cube[1]]=int(cube[0])
    min_cubes=list(min_cubes.values())
    total+=(min_cubes[0]*min_cubes[1]*min_cubes[2])
print(total)