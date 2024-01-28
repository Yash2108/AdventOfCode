with open('./Day 2/input.txt', 'r+') as infile:
    input_lines=[line.strip() for line in infile.readlines()]

input_lines=[line.split(':') for line in input_lines]
input_lines=[[line[0].split()[1], line[1].split(';')] for line in input_lines]

threshold={
    'red': 12,
    'green': 13,
    'blue': 14
}

total=0
for line in input_lines:
    games=line[1]
    games=[g.strip() for g in games]
    game_id=line[0]
    flag=True
    for game in games:
        game=game.split(',')
        game=[g.strip() for g in game]
        for cube in game:
            cube=cube.split()
            if int(cube[0])>threshold[cube[1]]:
                flag=False
    if flag:
        total+=int(game_id)

print(total)