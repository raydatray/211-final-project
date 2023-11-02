from collections import deque

class Pathing:


    def __init__(self):
        #TODO: input validation for mapSize and coordinates
        self.mapSize = int(input("Enter the size of the square map: "))
        self.map = [[0 for _ in range(self.mapSize) for _ in range(self.mapSize)]]
        self.targets = []
        self.path = deque()

        for target in range(3):
            coordinate = input("Enter the coordinate of a target: " + str(target + 1) + " as a two comma separated numbers ex. 3,4: ")
            xCoordinate, yCoordinate = coordinate.split(",")
            translatedCoords = self.translateCoordinates(int(xCoordinate), int(yCoordinate), self.mapSize)

            self.map[translatedCoords[0]][translatedCoords[1]] = 1
            self.targets.append(translatedCoords)




    def translateCoordinates(self, x, y, size):
        """
        Converts a 3,3 indexed 2d array (90 degree ) coordinate to a 0,0 indexed 2d array coordinate



        """
        newX = size - y - 1
        newY = x
        return (newX, newY)



    def generatePath(self, targets, origin):
        """
        Generates the most optimal path given a list of targets and origin
        Targets are ordered in decreasing manhattan distance from the origin
        Movements are translated into instructions that are placed into a deque
        """
        sortedTargets = sorted(targets, key = lambda target: manhattanDistance(target, origin), reverse = True) 
        impassableCoords = set()

        while len(sortedTargets) > 0:
            visited = set()
            bfs()

        def manhattanDistance(point1, point2):
            '''Returns the manhattan distance of two points (cardinal direction movements only)'''
            x1, y1 = point1
            x2, y2 = point2

            return abs(x1 - x2) + abs(y1 - y2)

        def bfs(r, c, target):

            def isValid(r, c):
                if (
                    r not in range(self.mapSize)
                    or c not in range(self.mapSize)
                    or (r,c) in visited
                    or (r,c) in impassableCoords
                ):
                    return False
                else:
                    return True
                
            def reconstructPath(parents, target):
                
                
            directions = [[0,1], [0,-1], [1,0], [-1,0]] #right, left, up, down
            q = deque()
            q.append((r,c))

            visited.add((r,c))

            while q:
                x, y = q.popleft()

                for dx, dy in directions:




            

        





    
