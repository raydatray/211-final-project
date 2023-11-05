from collections import deque

class Pathing:
    def __init__(self):
        #TODO: input validation for mapSize and coordinates
        self.mapSize = int(input("Enter the size of the square map: "))
        self.board = [[0 for _ in range(self.mapSize)] for _ in range(self.mapSize)]
        self.targets = []
        self.path = deque()

        for target in range(3):
            coordinate = input("Enter the coordinate of a target: " + str(target + 1) + " as a two comma separated numbers ex. 3,4: ")
            xCoordinate, yCoordinate = coordinate.split(",")
            translatedCoords = self.translateCoordinates(int(xCoordinate), int(yCoordinate), self.mapSize)

            self.board[translatedCoords[0]][translatedCoords[1]] = 1
            self.targets.append(translatedCoords)

    def translateCoordinates(self, x: int, y: int, size: int) -> tuple:
        """
        Converts a 3,3 indexed 2d array (90 degree) coordinate to a 0,0 indexed 2d array coordinate
        """
        newX = size - y - 1
        newY = x
        return (newX, newY)

    def generatePath(self, targets: list[tuple], origin: tuple):
        """
        Generates the most optimal path given a list of targets and origin\n
        Targets are ordered in decreasing manhattan distance from the origin\n
        Movements are translated into instructions that are placed into a deque
        """
        def manhattanDistance(point1: int, point2: int) -> int:
            '''Returns the manhattan distance of two points (cardinal direction movements only)'''
            x1, y1 = point1
            x2, y2 = point2

            return abs(x1 - x2) + abs(y1 - y2)

        def bfs(target: tuple, origin: tuple) -> list[tuple]: 

            def isValid(r: int, c: int) -> bool:
                if (
                    r not in range(self.mapSize)
                    or c not in range(self.mapSize)
                    or (r,c) in visited
                    or (r,c) in impassableCoords
                ):
                    return False
                else:
                    return True
                
            def reconstructPath(parents: dict, target: tuple) -> list[tuple]:
                """
                Reconstruct the path found by the BFS algorithm using a hashmap\n
                key:value -> node: parent node (1:1 mapping, each node has one parent node for a given bfs)\n
                Nodes are appended to the deque that consists of the path found 
                """
                path = []
                while target:
                    path.insert(0, target)
                    target = parents.get(target, None)
                
                return path

                
            directions = [[0,1], [0,-1], [1,0], [-1,0]] #right, left, up, down

            visited = set()
            visited.add(origin)

            parents = {}

            q = deque()
            q.append(origin)

            while q:
                r, c = q.popleft()

                if (r, c) == target:
                    impassableCoords.add((r, c))
                    return reconstructPath(parents, target)

                for dx, dy in directions:
                    newR, newC = r + dx, c + dy

                    if isValid(newR, newC): 
                        q.append((newR, newC))
                        visited.add((newR, newC))
                        parents[(newR, newC)] = (r, c)
    
        sortedTargets = sorted(targets, key = lambda target: manhattanDistance(target, origin))
        sortedTargets.insert(0, origin) #Add the origin to the end of the queue 
        impassableCoords = set()
        path = []

        while sortedTargets:
            target = sortedTargets.pop()
            subPath = bfs(target, origin)    
            origin = subPath[-2] #BACKTRACK ONE NODE
            path = path + subPath

        return path

    def generateInstructions(self, path: list[tuple]) -> list[str]:
        """
        THIS IS A LESS THAN OPTIMAL FUNCTION\n
        Translates a list of coordinates into a list of cardinal directions to be traversed\n
        Drop instructions are also included in this set of instructions (When targets are reached)
        """
        instructions = []

        for start, end in zip(path[0::], path[1::]):
            sR, sC = start
            eR, eC = end
            dR, dC = eR - sR, eC - sC

            if start in self.targets:
                instructions.append("DROP")

            if dR == 1:
                instructions.append("DOWN")
            elif dR == -1:
                instructions.append("UP")
            elif dC == 1:
                instructions.append("RIGHT")
            elif dC == -1:
                instructions.append("LEFT")
                
        return instructions


            
     
        




            

        





    
