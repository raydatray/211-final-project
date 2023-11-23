from Carousel import *
from Pathing import *
from Movement import *
from utils.brick import *

class Robot:
    def __init__ (self):
        self.rightColorSensor = EV3ColorSensor(1)
        self.leftColorSensor = EV3ColorSensor(4)

        self.rightMotor = Motor("C")
        self.leftMotor = Motor("B")

        self.carouselMotor = Motor("A")
        self.tarpdoorMotor = Motor("D")

        wait_ready_sensors(True)
        print("Sensors and motors initialized")

    def initSubsystems(self):
        self.pathing = Pathing()
        self.carousel = Carousel(self.carouselMotor, self.tarpdoorMotor)
        self.movement = Movement(self.rightColorSensor, self.leftColorSensor, self.rightMotor, self.leftMotor)
        print("Subsystems initialized")
    
    def runRobot(self):
        foundPath = self.pathing.generatePath()
        translatedPath = self.pathing.generateInstructions(foundPath)
        
        
        for i in range(0, len(translatedPath)):
            print(i, len(translatedPath), translatedPath[i])
            if translatedPath[i] == "RIGHT":
                self.movement.turnRight()
                
            if translatedPath[i] == "LEFT":
                self.movement.turnLeft()

            if translatedPath[i] == "BACK":
                self.movement.backUp()

            if translatedPath[i] == "MOVE":
                if i != (len(translatedPath) - 1):
                    print("reachedx")
                    if translatedPath[i+1] != "DROP":
                        self.movement.fullMoveForward()
                    else:
                        self.movement.partialMoveForward()
                else:
                    self.movement.fullMoveForward() #extremely ghetto fix might not work
            
            if translatedPath[i] == "DROP":
                if i != (len(translatedPath) - 1):
                    print("reachedy")
                    self.carousel.rotateToBlockByName(translatedPath[i+1])
                    self.carousel.dropCurrentBlock()
            time.sleep(.25)

        """
        for instruction, nextInstruction in zip(translatedPath[0::], translatedPath[1::]):
            if instruction == "RIGHT":
                self.movement.turnRight()
                
            if instruction == "LEFT":
                self.movement.turnLeft()

            if instruction == "BACK":
                self.movement.backUp()

            if instruction == "MOVE":
                if nextInstruction != "DROP":
                    self.movement.fullMoveForward()
                else:
                    self.movement.partialMoveForward()
            
            if instruction == "DROP":
                self.carousel.rotateToBlockByName(nextInstruction)
                self.carousel.dropCurrentBlock()
            print(instruction, nextInstruction)
            """
        
        
    
