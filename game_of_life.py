fr = open("glider-gun.txt")
height = int(fr.readline().strip())
width = int(fr.readline().strip())
dish1 = []
dish2 = []

def create_dishes(height,width):
    global dish1, dish2
    for i in range(height):
        dish2.append([0] * width)
        dish1.append([0] * width)
    y = 0
    for riadok in fr:
        x = 0
        for znak in riadok.strip():
            if znak != "-":
                dish1[y][x] = 1
            x +=1
        y += 1

def get_neighbours(dish, x, y):
    neighbours = 0
    if dish[y-1][x-1] == 1: neighbours += 1
    if dish[y-1][x]   == 1: neighbours += 1
    if dish[y-1][x+1] == 1: neighbours += 1
    if dish[y][x-1]   == 1: neighbours += 1
    if dish[y][x+1]   == 1: neighbours += 1
    if dish[y+1][x-1] == 1: neighbours += 1
    if dish[y+1][x]   == 1: neighbours += 1
    if dish[y+1][x+1] == 1: neighbours += 1
    return neighbours
print(get_neighbours(dish1, 0, 0))

def copy_dishes(source,destination):










create_dishes(height, width)
print(dish1)
