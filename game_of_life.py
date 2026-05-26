fr = open("glider-gun.txt")
height = int(fr.readline().strip())
width = int(fr.readline().strip())
dish1 = []
dish2 = []

def create_dishes():
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
    if y-1 >= 0 and x-1 >= 0 and dish[y-1][x-1] == 1: neighbours += 1
    if y-1 >= 0 and             dish[y-1][x]   == 1: neighbours += 1
    if y-1 >= 0 and x+1 < width and dish[y-1][x+1] == 1: neighbours += 1
    if             x-1 >= 0 and dish[y][x-1]   == 1: neighbours += 1
    if             x+1 < width and dish[y][x+1]   == 1: neighbours += 1
    if y+1 < height and x-1 >= 0 and dish[y+1][x-1] == 1: neighbours += 1
    if y+1 < height and             dish[y+1][x]   == 1: neighbours += 1
    if y+1 < height and x+1 < width and dish[y+1][x+1] == 1: neighbours += 1
    return neighbours

def copy_dishes(source, destination):
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            neighbours = get_neighbours(source, x, y)
            if source[y][x] == 1:
                if neighbours < 2:
                    destination[y][x] = 0   # Pravidlo 1: underpopulation
                elif neighbours <= 3:
                    destination[y][x] = 1   # Pravidlo 2: lives on
                else:
                    destination[y][x] = 0   # Pravidlo 3: overpopulation
            else:
                if neighbours == 3:
                    destination[y][x] = 1   # Pravidlo 4: reproduction
                else:
                    destination[y][x] = 0


create_dishes()
print(dish1)
print(get_neighbours(dish1, 0, 0))
