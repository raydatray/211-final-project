from collections import deque

class Pathing:
    def __init__(self):
        #TODO: input validation for mapSize and coordinates
        #self.mapSize = int(input("Enter the size of the square map: "))
        self.mapSize = 4
        #self.board = [[0 for _ in range(self.mapSize)] for _ in range(self.mapSize)]
        self.start = (3,0)
        self.targets = []
        self.suppressants = {}
        self.path = deque()
        """
        for target in range(3):
            coordinate = input("Enter the coordinate of a target: " + str(target + 1) + " as a two comma separated numbers ex. 3,4: ")
            xCoordinate, yCoordinate = coordinate.split(",")
            translatedCoords = self.translateCoordinates(int(xCoordinate), int(yCoordinate), self.mapSize)

            self.board[translatedCoords[0]][translatedCoords[1]] = 1
            self.targets.append(translatedCoords)
        """


        #ADD INPUT VALIDAITON1!!
        inputPrompt = input("Please input the 3 fires and their type in the following order: x,y,fireType: ")

        inputList = inputPrompt.split(',')

        coordinates = [self.translateCoordinates(int(inputList[i]), int(inputList[i+1]), self.mapSize) for i in range(0, len(inputList), 3)]
        fireTypes = inputList[2::3]

        self.targets = coordinates
        self.suppressants = {coordinates[i]:fireTypes for i, fireTypes in enumerate(fireTypes)}
        print()
        
        #print(self.suppressants)
        #print(coordinates)
            


    def translateCoordinates(self, x: int, y: int, size: int) -> tuple:
        """
        Converts a 3,3 indexed 2d array (90 degree) coordinate to a 0,0 indexed 2d array coordinate
        """
        newX = size - y - 1
        newY = x
        return (newX, newY)

    def generatePath(self):
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
                    return reconstructPath(parents, target)

                for dx, dy in directions:
                    newR, newC = r + dx, c + dy

                    if isValid(newR, newC): 
                        q.append((newR, newC))
                        visited.add((newR, newC))
                        parents[(newR, newC)] = (r, c)
    
        origin = self.start
        #print(sortedTargets)
        impassableCoords = set(self.targets)
        path = []

        sortedTargets = sorted(self.targets, key = lambda target: manhattanDistance(target, origin))
        sortedTargets.insert(0, self.start) #Add the origin to the end of the queue 
       

        while sortedTargets:
            target = sortedTargets.pop()
            impassableCoords.discard(target)
            #print(target)
            subPath = bfs(target, origin)    
            origin = subPath[-2] #BACKTRACK ONE NODE
            path = path + subPath
            impassableCoords.add(target)

        return path

    def generateInstructions(self, path: list[tuple]) -> str:

        def generateRotations(currentOrientation: str, instruction: str) -> list[str]:
            #Case 1: instruction matches current orientation:
                # Do not insert a rotation and MOVE
            #Case 2: instruction does match the current orientation:
                # 

            orientationPairings = {
                "UP": {"RIGHT": "RIGHT", "DOWN": "BACK", "LEFT": "LEFT"},
                "RIGHT": {"UP": "LEFT", "DOWN": "RIGHT", "LEFT": "BACK"},
                "DOWN": {"UP": "BACK", "RIGHT": "LEFT", "LEFT": "RIGHT"},
                "LEFT": {"UP": "RIGHT", "RIGHT": "BACK", "DOWN": "LEFT"}
            }

            return orientationPairings.get(currentOrientation, {}).get(instruction, None)
            
        """
        THIS IS A LESS THAN OPTIMAL FUNCTION\n
        Translates a list of coordinates into a list of cardinal directions to be traversed\n
        Drop instructions are also included in this set of instructions (When targets are reached)
        """
        orientation = "UP" #init orientation, upwards (facing 0,0)
        instructions = []

        for start, end in zip(path[0::], path[1::]):
            sR, sC = start
            eR, eC = end
            dR, dC = eR - sR, eC - sC

            direction = None

            if start in self.targets:
                instructions.append("DROP")
                instructions.append(self.suppressants.get(start, None))

            if dR == 1:
                direction = "DOWN"
            elif dR == -1:
                direction = "UP"
            elif dC == 1:
                direction = "RIGHT"
            elif dC == -1:
                direction = "LEFT"

            if orientation != direction:
                lastGenerated = generateRotations(orientation, direction)
                instructions.append(lastGenerated)
            else:
                instructions.append("MOVE")
                continue

            if lastGenerated != "BACK":
                instructions.append("MOVE")
                orientation = direction
                
        return instructions


            
     
        




            

        





    
