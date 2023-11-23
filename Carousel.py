import time

class Carousel:
    anglePerBlock = 185 #finalized value

    #TODO: either init motors here as class variables, or accept them as inputs through the init 
    #test comment....

    def __init__(self, carouselMotor, trapdoorMotor):
        self.blocks = ["D","B","C","A","E","F"]
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
        
    def rotateToBlockByIndex(self, selectedIndex):
        #only make if necessary
        if self.blocks[selectedIndex] == None:
            return "The block at the selected index has already been dropped"
        
        degreesToRotate = (selectedIndex - self.pointer) * self.anglePerBlock

        #TODO: rotate the motor by degreesToRotate

        self.pointer = selectedIndex
        self.currentBlock = self.blocks[self.pointer]
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
        self.trapdoorMotor.reset_encoder() #questionable usage may delete
        self.trapdoorMotor.set_position.relative(-150)
        time.sleep(2)
        self.trapdoorMotor.set_position_relative(220)
        time.sleep(2)
        self.trapdoorMotor.set_power(0)

        #Update the array and rotate the carousel
        self.unavailableBlocks.add(self.currentBlock)
        self.blocks[self.pointer] = None #Void the current index of the array 
        self.rotateToBlockByIndex((self.pointer +  1 % 6)) #Rotate to next index
        
        return




    