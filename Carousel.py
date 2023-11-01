class Carousel:
    anglePerBlock = 900 #TEMPORARY VALUE

    #TODO: either init motors here as class variables, or accept them as inputs through the init 
    #test comment....

    def __init__(self):
        self.blocks = ["A","B","C","D","E","F"]
        self.pointer = 0
        self.currentBlock = "A"
        self.unavailableBlocks = set()

    def rotateToBlockByName(self, selectedBlock):
        if selectedBlock in self.unavailableBlocks:
            return "Selected block has already been dropped"
        

        while self.currentBlock != selectedBlock:
            #TODO: rotate the motor by anglePerBlock


            self.pointer = (self.pointer + 1) % 6 #increment the pointer
            self.currentBlock = self.blocks[self.pointer] #update the current block

        return 
        
    def rotateToBlockByIndex(self, selectedIndex):
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
        #TODO: Drop the block by calling the motor methods




        #Update the array and rotate the carousel
        self.unavailableBlocks.add(self.currentBlock)
        self.blocks[self.pointer] = None #Void the current index of the array 
        self.rotateToBlockByIndex((self.pointer +  1 % 6)) #Rotate to next index
        




    