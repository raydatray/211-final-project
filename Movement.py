import time

class Movement:
    colorClusters = {
    'BLUE': (0.308, 0.329, 0.362),
    'RED': (0.805, 0.123, 0.072),
    'GREEN': (0.223, 0.588, 0.189),
    'BOARD': (0.530, 0.339, 0.131)
    }

    def __init__(self, rightColorSensor, leftColorSensor, rightWheel, leftWheel):
        self.rightColorSensor = rightColorSensor
        self.leftColorSensor = leftColorSensor
        self.rightWheel = rightWheel
        self.leftWheel = leftWheel
        #INIT MOTOR POWERS (TEST)
        self.rightPower = 0
        self.leftPower = 0
        self.orientation = "UP"

    def classify_color(self, values: list[int]) -> str:
        r, g, b = values
        # Normalize the input RGB values
        total = r + g + b
        if total == 0:
            return 'UNKNOWN'  # To avoid division by zero error.
        norm_r = r / total
        norm_g = g / total
        norm_b = b / total

        # Initialize minimum distance to a high value
        min_distance = float('inf')
        classified_color = 'UNKNOWN'

        # Calculate the distance to each color cluster and find the nearest
        for color, cluster in self.colorClusters.items():
            cluster_norm_r, cluster_norm_g, cluster_norm_b = cluster
            distance = (
                        (norm_r - cluster_norm_r)**2 +
                        (norm_g - cluster_norm_g)**2 +
                        (norm_b - cluster_norm_b)**2
                        ) ** 0.5
            if distance < min_distance:
                min_distance = distance
                classified_color = color

        return classified_color

    def correctLeft(self):
        self.rightPower += 0.5
        self.rightWheel.set_power(self.rightPower)
        self.leftPower -= 0.5
        self.leftWheel.set_power(self.leftPower)

    def correctRight(self):
        self.rightPower -= 0.5
        self.rightWheel.set_power(self.rightPower)
        self.leftPower += 0.5
        self.leftWheel.set_power(self.leftPower)

    def moveForward(self) -> bool:
        
        self.rightPower = -29.5
        self.leftPower = -30
        
        self.rightWheel.set_power(self.rightPower)
        self.leftWheel.set_power(self.leftPower)

        rightColor = self.classify_color(self.rightColorSensor.get_rgb())
        leftColor = self.classify_color(self.leftColorSensor.get_rgb())
    
        #move forward, until green is reached 
        #while moving poll for right/left bad reads
        while (leftColor != 'GREEN' and rightColor != 'GREEN'):
            
            if leftColor != 'BOARD' and rightColor == "BOARD": #correct rightward
                self.correctRight()
            if rightColor != 'BOARD' and leftColor == "BOARD": #correct leftward
                self.correctLeft()
                
            #reread the color after .5 seconds
            time.sleep(.05)

            rightColor = self.classify_color(self.rightColorSensor.get_rgb())
            leftColor = self.classify_color(self.leftColorSensor.get_rgb())
            
        self.rightWheel.set_power(0)
        self.leftWheel.set_power(0)
        print("MOVED FORWARD")

        return True
    
    def finishMoveForward(self) -> bool:
        timeEnd = time.time() + 1.5
        
        rightColor = self.classify_color(self.rightColorSensor.get_rgb())
        leftColor = self.classify_color(self.leftColorSensor.get_rgb())
        
        while time.time() < timeEnd:
            self.rightPower = -30
            self.leftPower = -30
            
            self.rightWheel.set_power(self.rightPower)
            self.leftWheel.set_power(self.leftPower)
            
            if leftColor != 'BOARD' and leftColor != 'GREEN': #correct rightward
                self.correctRight()
            if rightColor != 'BOARD' and leftColor != 'GREEN': #correct leftward
                self.correctLeft()
                
            rightColor = self.classify_color(self.rightColorSensor.get_rgb())
            leftColor = self.classify_color(self.leftColorSensor.get_rgb())
            
        self.rightWheel.set_power(0)
        self.leftWheel.set_power(0)
        
        print("FINISHED MOVING FORWARD")
        return True
            

    def turnRight(self) -> bool:
        #turn the left motor forward and the right motor backwards
        #if the orientation is up or down, rotate until blue is read
        #if the orientation is right or left, rotate until red is read
        rightColor = self.classify_color(self.rightColorSensor.get_rgb())
    
        if self.orientation == "UP" or self.orientation == "DOWN":
            targetColor = "BLUE"
        else:
            targetColor = "RED"

        self.rightWheel.set_power(20)
        self.leftWheel.set_power(-20)

        while (rightColor != targetColor):
            time.sleep(.1)
            rightColor = self.classify_color(self.rightColorSensor.get_rgb())
            
        while (rightColor != "BOARD"):
            time.sleep(.1)
            rightColor = self.classify_color(self.rightColorSensor.get_rgb())
        
        self.rightWheel.set_power(0)
        self.leftWheel.set_power(0)
        
        # Change orientation
        if self.orientation == "UP":
            self.orientation = "RIGHT"
        elif self.orientation == "RIGHT":
            self.orientation = "DOWN"
        elif self.orientation == "DOWN":
            self.orientation = "LEFT"
        else:
            self.orientation = "UP"
        
        print("TURNED RIGHT")
        return True

    def turnLeft(self) -> bool:
        #turn the right motor forward and the left motor backwards
        #if the orientation is up or down, rotate until blue is read
        #if the orientation is right or left, rotate until red is read
        leftColor = self.classify_color(self.leftColorSensor.get_rgb())
    
        if self.orientation == "UP" or self.orientation == "DOWN":
            targetColor = "BLUE"
        else:
            targetColor = "RED"

        self.rightWheel.set_power(-20)
        self.leftWheel.set_power(20)

        while (leftColor != targetColor):
            time.sleep(.1)
            leftColor = self.classify_color(self.leftColorSensor.get_rgb())
            
        while (leftColor != "BOARD"):
            time.sleep(.1)
            leftColor = self.classify_color(self.leftColorSensor.get_rgb())

        self.rightWheel.set_power(0)
        self.leftWheel.set_power(0)
        
        # Change orientation
        if self.orientation == "UP":
            self.orientation = "LEFT"
        elif self.orientation == "LEFT":
            self.orientation = "DOWN"
        elif self.orientation == "DOWN":
            self.orientation = "RIGHT"
        else:
            self.orientation = "UP"
        
        print("TURNED LEFT")
        return True

    def turnAround(self) -> bool:
        #basically turn right twice
        #rotate until the original color is read again

        rightColor = self.classify_color(self.rightColorSensor.get_rgb())

        if self.orientation == "UP" or self.orientation == "DOWN":
            targetColor = "RED"
        else:
            targetColor = "BLUE"

        self.rightWheel.set_power(30)
        self.leftWheel.set_power(-30)
            
        while (rightColor != targetColor):
            time.sleep(.1)
            rightColor = self.classify_color(self.rightColorSensor.get_rgb())
        
        while (rightColor != "BOARD"):
            time.sleep(.1)
            rightColor = self.classify_color(self.rightColorSensor.get_rgb())

        self.rightWheel.set_power(0)
        self.leftWheel.set_power(0)
        
        # Change orientation
        if self.orientation == "UP":
            self.orientation = "DOWN"
        elif self.orientation == "LEFT":
            self.orientation = "RIGHT"
        elif self.orientation == "DOWN":
            self.orientation = "UP"
        else:
            self.orientation = "LEFT"
        
        print("TURNED AROUND")
        return True


