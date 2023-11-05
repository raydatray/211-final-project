from Pathing import *

#TEST CODE FOR PATHING
pathing = Pathing()
foundPath = pathing.generatePath(pathing.targets, (3,0))
print(foundPath)
translatedPath = pathing.generateInstructions(foundPath)
print(translatedPath)
