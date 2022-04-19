class WirelessNetworks:


    BRAND_NAME = 'Cisco'              #static variable

    ADHOC_Mode = 'ON'                 #static variable
    
   
    
    def greetMessage(self):                  #method to print welcome message
        print("Welcome to the company's IoT-Based Health System \nThese are sensors of " , self.BRAND_NAME  , " brand, and the Ad Hoc Mode is " , self.ADHOC_Mode , "\n")

    def __init__(self):                     #constuctor method of WirelessNetwork class
        self.id = '' 
        self.neighbours = 0
        self.oxygenLevel = 0
        self.distance = ()
        self.temperature = 0.0

    def setID(self, Id):                  #mutator method to set i.d
        self.id = Id

    def getID(self):                      #accesor method to get the i.d
       return self.id

    def setTemperature(self, temp):       #mutator method to set temperature
        self.temperature = temp   


    def setOxygenLevel(self, o2Level):    #mutator method to set oxygen level
        self.oxygenLevel = o2Level

    

    def setNeighbours(self, neighbours):   #mutator method to set number of neighbours
        self.neighbours = neighbours