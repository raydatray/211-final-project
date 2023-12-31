import time


class Carousel:
    anglePerBlock = 185 #finalized value

    def __init__(self, carouselMotor, trapdoorMotor):
        self.blocks = ["D","E","F","A","B","C"]
        self.pointer = 0
        self.currentBlock = "GREEN"
        self.unavailableBlocks = set()
        self.carouselMotor = carouselMotor
        self.trapdoorMotor = trapdoorMotor
        print("Carousel intialized")

    def rotateToBlockByName(self, selectedBlock):
        if selectedBlock in self.unavailableBlocks:
            return "Selected block has already been dropped"
        
        while self.currentBlock != selectedBlock:
            self.carouselMotor.set_limits(50, 165)
            self.carouselMotor.set_position_relative(self.anglePerBlock)
            time.sleep(2)

            self.pointer = (self.pointer + 1) % 6 #increment the pointer
            self.currentBlock = self.blocks[self.pointer] #update the current block
        
        self.carouselMotor.float_motor()
        return 
    
    #DEPRECATED, you should use rotateToBlockByName
    def rotateToBlockByIndex(self, selectedIndex):
        """
        if self.blocks[selectedIndex] == None:
            return "The block at the selected index has already been dropped"
        
        degreesToRotate = (selectedIndex - self.pointer) * self.anglePerBlock


        self.pointer = selectedIndex
        self.currentBlock = self.blocks[self.pointer]
        """
        return 

    def getCurrentBlock(self):
        return self.currentBlock
    
    def setCurrentBlock(self, currentBlock):
        self.currentBlock = currentBlock
        return self.currentBlock

    def getCurrentIndex(self):
        return self.pointer

    def setCurrentIndex(self, currentIndex):
        self.pointer = currentIndex
        return self.pointer

    def dropCurrentBlock(self):
        self.trapdoorMotor.set_limits(90,180)
        self.trapdoorMotor.reset_encoder() 

        self.trapdoorMotor.set_position_relative(-150)
        time.sleep(2)

        self.trapdoorMotor.set_position_relative(220)
        time.sleep(2)

        self.trapdoorMotor.set_power(0)
        self.unavailableBlocks.add(self.currentBlock)
        return




    