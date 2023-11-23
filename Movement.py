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
        self.rightWheel.set_power(-25)
        self.leftWheel.set_power(-20)

    def correctRight(self):
        self.rightWheel.set_power(-20)
        self.leftWheel.set_power(-25)

    def partialMoveForward(self) -> bool:
        if self.orientation == "UP" or self.orientation == "DOWN":
            targetColor = "RED"
        else:
            targetColor = "BLUE"
        
        self.rightPower = -25
        self.leftPower = -25
        self.rightWheel.set_power(self.rightPower)
        self.leftWheel.set_power(self.leftPower)

        rightColor = self.classify_color(self.rightColorSensor.get_rgb())
        leftColor = self.classify_color(self.leftColorSensor.get_rgb())
    
        #move forward, until green is reached 
        #while moving poll for right/left bad reads
        while (leftColor != 'GREEN' and rightColor != 'GREEN'):
            
            #if leftColor != 'BOARD':
            if leftColor == targetColor:
                self.correctLeft()
            #elif rightColor != 'BOARD':
            if rightColor == targetColor:
                self.correctRight()
            
            time.sleep(.05)
            
            self.rightPower = -25
            self.leftPower = -25
            self.rightWheel.set_power(self.rightPower)
            self.leftWheel.set_power(self.leftPower)
            
            rightColor = self.classify_color(self.rightColorSensor.get_rgb())
            leftColor = self.classify_color(self.leftColorSensor.get_rgb())
        
        self.rightWheel.set_power(0)
        self.leftWheel.set_power(0)

        return True
    
    def fullMoveForward(self) -> bool:
        if self.orientation == "UP" or self.orientation == "DOWN":
            targetColor = "RED"
        else:
            targetColor = "BLUE"
        
        self.rightPower = -25
        self.leftPower = -25
        self.rightWheel.set_power(self.rightPower)
        self.leftWheel.set_power(self.leftPower)

        rightColor = self.classify_color(self.rightColorSensor.get_rgb())
        leftColor = self.classify_color(self.leftColorSensor.get_rgb())
    
        #move forward, until green is reached 
        #while moving poll for right/left bad reads
        while (leftColor != 'GREEN' and rightColor != 'GREEN'):
            
            #if leftColor != 'BOARD':
            while leftColor == targetColor:
                self.correctLeft()
                time.sleep(.05)
                leftColor = self.classify_color(self.leftColorSensor.get_rgb())
            #elif rightColor != 'BOARD':
            while rightColor == targetColor:
                self.correctRight()
                time.sleep(.05)
                rightColor = self.classify_color(self.rightColorSensor.get_rgb())
            
            self.rightPower = -25
            self.leftPower = -25
            self.rightWheel.set_power(self.rightPower)
            self.leftWheel.set_power(self.leftPower)
            
            rightColor = self.classify_color(self.rightColorSensor.get_rgb())
            leftColor = self.classify_color(self.leftColorSensor.get_rgb())
            time.sleep(.1)
        
        timeEnd = time.time() + 1.3
        
        while time.time() < timeEnd:
            #if leftColor != 'BOARD' and leftColor != 'GREEN': #correct rightward
            if leftColor == targetColor: #and rightColor != targetColor:
                self.correctLeft()
                leftColor = self.classify_color(self.leftColorSensor.get_rgb())
            #elif rightColor != 'BOARD' and rightColor != 'GREEN': #correct leftward
            elif rightColor == targetColor: #and leftColor != targetColor:
                self.correctRight()
                rightColor = self.classify_color(self.rightColorSensor.get_rgb())
            
            time.sleep(.05)
            
            self.rightPower = -25
            self.leftPower = -25
            self.rightWheel.set_power(self.rightPower)
            self.leftWheel.set_power(self.leftPower)
                  
            rightColor = self.classify_color(self.rightColorSensor.get_rgb())
            leftColor = self.classify_color(self.leftColorSensor.get_rgb())
           
        self.rightWheel.set_power(0)
        self.leftWheel.set_power(0)
        
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
        
        return True

    def backUp(self) -> bool:
        #basically turn right twice
        #rotate until the original color is read again
        if self.orientation == "UP" or self.orientation == "DOWN":
            targetColor = "RED"
        else:
            targetColor = "BLUE"
        
        rightColor = self.classify_color(self.rightColorSensor.get_rgb())
        leftColor = self.classify_color(self.leftColorSensor.get_rgb())
            
        timeEnd = time.time() + 1.75
        
        while time.time() < timeEnd:
            #if leftColor != 'BOARD' and leftColor != 'GREEN': #correct rightward
            if leftColor == targetColor: #and rightColor != targetColor:
                self.correctLeft()
                leftColor = self.classify_color(self.leftColorSensor.get_rgb())
            #elif rightColor != 'BOARD' and rightColor != 'GREEN': #correct leftward
            elif rightColor == targetColor: #and leftColor != targetColor:
                self.correctRight()
                rightColor = self.classify_color(self.rightColorSensor.get_rgb())
            
            time.sleep(.05)
            
            self.rightPower = 25
            self.leftPower = 25
            self.rightWheel.set_power(self.rightPower)
            self.leftWheel.set_power(self.leftPower)
                  
            rightColor = self.classify_color(self.rightColorSensor.get_rgb())
            leftColor = self.classify_color(self.leftColorSensor.get_rgb())
           
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
        
        return True


