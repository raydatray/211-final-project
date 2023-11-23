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
    
