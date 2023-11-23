from Pathing import *

#TEST CODE FOR PATHING
pathing = Pathing()
foundPath = pathing.generatePath()
print(foundPath)
translatedPath = pathing.generateInstructions(foundPath)
print(translatedPath)
