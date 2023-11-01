
#TODO: input validation
mapSize = int(input("Enter the size of the square map to traverse: "))

map = [[0 for _ in range(mapSize)] for _ in range(mapSize)] #Construct the map as a m x m matrix of 0s

#Init list of coordinates of buildings (guaranteed to be 3)
targets = []

#DONE: this WORKS
def translateCoordinates(x, y, size):
    newX = size - y - 1
    newY = x
    return (newX,newY)

#TODO: input validation
for target in range(3):
    coordinate = input("Enter the coordinate of a target: " + str(target + 1) + " as a two comma separated numbers ex. 3,4: ")
    xCoordinate, yCoordinate = coordinate.split(",")
    translatedCoords = translateCoordinates(int(xCoordinate), int(yCoordinate), mapSize)

    map[translatedCoords[0]][translatedCoords[1]] = 1
    targets.append(translatedCoords)
    print(map)
    print(targets)


"""
TSP with dynamic programming

Given set of vertices {1,2,3,...,n}, consider the vertex 1 as the start and end point
    For us this is the BOTTOM LEFT corner (mapsize - 1, 0)

For every other vertex X, find the minimum cost path with 1 as the starting point and every OTHER vertex appearing exactly once



"""

#Calculate the manhattan distance (Cardinal directions only) between 2 points
def manhattanDistance(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2

    return abs(x1 - x2) + abs(y1 - y2)      

def TSP(targets):
    n = len(targets)
    unvisited = set(targets)



def nearestNeighborTSP(targets):
    n = len(targets)
    unvisited = set(targets)

    circuit = [targets[0]]

    while len(circuit) <= n:
        lastTarget = circuit[-1]
        nearestTarget = min(unvisited, key= lambda target: manhattanDistance(lastTarget, target))
        circuit.append(nearestTarget)   
        unvisited.remove(nearestTarget)

    return circuit



targets.insert(0, (3,3))

print(targets)

tour = nearestNeighborTSP(targets)

for target in tour:
    print(target)
