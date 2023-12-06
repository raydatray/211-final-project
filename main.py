#from Pathing import *
from Robot import *
"""
#TEST CODE FOR PATHING
pathing = Pathing()
foundPath = pathing.generatePath()
print(foundPath)
translatedPath = pathing.generateInstructions(foundPath)
print(translatedPath)

1,2,A,2,2,D,3,0,C
"""
while True:
    robot = Robot()
    robot.initSubsystems()
    robot.runRobot()
    reset_brick()
