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
        self.orientation = "UP"

    def classify_color(self, r, g, b):
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
            distance = ((norm_r - cluster_norm_r)2 +
                        (norm_g - cluster_norm_g)2 +
                        (norm_b - cluster_norm_b)2)0.5
            if distance < min_distance:
                min_distance = distance
                classified_color = color

        return classified_color

    def moveForward(self) -> bool:
        
        #modify the speed to change the direction
        def correctLeft():


        def correctRight():



        #move forward, until green is reached 
        #while moving poll for right/left bad reads

        while 

            if 


    def turnRight(self) -> bool:

        #turn the left motor forward and the right motor backwards
        #if the orientation is up or down, rotate until blue is read
        #if the orientation is right or left, rotate until red is read

        return True

    def turnLeft(self) -> bool:
        #turn the right motor forward and the left motor backwards
        #if the orientation is up or down, rotate until blue is read
        #if the orientation is right or left, rotate until red is read

    def turnAround(self) -> bool:
        #basically turn right twice
        #rotate until the original color is read again
