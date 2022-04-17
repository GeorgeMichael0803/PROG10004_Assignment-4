class WirelessNetworks:


    BRAND_NAME = 'Cisco'

    ADHOC_Mode = 'ON'
   
   
    
    def greetMessage(self):
        print("Welcome to the company's IoT-Based Health System\nThese are sensors of " + self.BRAND_NAME  + " brand, and the Ad Hoc Mode is " + self.ADHOC_Mode + "\n")

    def __init__(self):
        self.id = ''
        self.oxygenLevel = 0
        self.temperature = 0.0
        self.neighbours = 0
        self.distance = ()

    def setID(self, Id):
        self.id = Id

    def getID(self):
       return self.id


    def setOxygenLevel(self, o2Level):
        self.oxygenLevel = o2Level

    def setTemperature(self, temp):
        self.temperature = temp

    def setNeighbours(self, neighbours):
        self.neighbours = neighbours