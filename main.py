from screenshot import Screenshot

# memory mechanism
tiles = []
for i in range(7):
    # get tile from screenshot
    tiles.append(Screenshot())
    for j in range(i+1):
        if j != i:
            print(tiles[j], end=',')
        else:
            print(tiles[j])
