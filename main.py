input_tiles = [2, 1, 1, 0, 2, 1, 2]

# memory mechanism
tiles = []
for i in range(7):
    tiles.append(input_tiles[i])
    for j in range(i+1):
        if j != i:
            print(tiles[j], end=',')
        else:
            print(tiles[j])
