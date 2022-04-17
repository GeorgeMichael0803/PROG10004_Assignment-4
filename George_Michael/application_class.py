
from  wireless_network import WirelessNetworks

class Application:
   def __init__(self):
      self.listSensors = []
      self.totalSensors = 0
      self.sensorDict = {}


      network = WirelessNetworks()
      network.greetMessage()


      self.createSensors()
   
   def createSensors(self):
      while True:
         try:
            numOfSensors = int(input("Enter the number of sensors: "))
            break
         except:
            print("This is an invalid entry for the number of sensors")
      self.setTotalSensors(numOfSensors)
      print(str(self.totalSensors) + ' sensors total')

      self.drawLine()

      for sensor in range(1, self.totalSensors + 1):
         sensor = WirelessNetworks()

         id = (input('Enter the sensor ID: '))
         while any(char.isdigit() for char in id):
            print("This is an invalid entry for the neighbour's name and/or distance!")
            id = input('Enter the sensor ID: ')
         sensor.setID(id)
         
         while True:
            try:
               numOfNeighbours = int(input("Enter the number of neighbours: "))
               break
            except:
               print("This is an invalid entry for the number of neighbours")
         sensor.setNeighbours(numOfNeighbours)
         print(str(sensor.neighbours) + ' neighbour(s) total')

         for neighbour in range(1, sensor.neighbours + 1):
            neighbour = WirelessNetworks()

            neighbourId = input("Enter the neighbour for sensor " + sensor.id + ": ")
            while any(char.isdigit() for char in neighbourId ):
               print("This is an invalid entry for the neighbour's name and/or distance!")
               neighbourId = input("Enter the neighbour for sensor " + sensor.id + ": ")
            neighbour.setID(neighbourId)
         

            self.convrtToDict(sensor, neighbour)

         while True:
            try:
               o2Level = int(input("Enter the Oxygen level in %: "))
               break
            except:
               print("This is an invalid entry for the oxygen level!")
         sensor.setOxygenLevel(o2Level)

         while True:
            try:
               temp = float(input("Enter the temperature measurement: "))
               break
            except:
               print("This is an invalid entry for the temperature!")
         sensor.setTemperature(temp)

         self.listSensors.append(sensor)
         self.drawLine()

      self.findPath()
         

            
   def convrtToDict(self, sensor, neighbour):
      distance = (neighbour.id, int(input("Enter the distance (m) to " + sensor.id + ": ")))
      if sensor.id not in self.sensorDict:
         self.sensorDict[sensor.id] = [distance]
      else:
         self.sensorDict[sensor.id].append(distance)
      print(self.sensorDict)



   def findPath(self):
      source = input("Enter the source sensor: ")
      path = [source]
      dest = input("Enter the destination sensor: ")
      if self.findPathHelper(source, dest, path):
         print("Path= ",path)
      else:
         print("The destination is not found")
         
   def findPathHelper(self, source, dest, path):
      if source == dest:
         return(True)
      currentMax = self.sensorDict[source][0]
      for id, distance in self.sensorDict[source]:
         if distance > currentMax[1]:
            currentMax = (id, distance)
      path.append(currentMax[0])
      return(self.findPathHelper(currentMax[0], dest, path))



   def setTotalSensors(self, sensorCount):
      self.totalSensors = sensorCount

   def drawLine(self):
      print('_*__*__*__*__*__*__*__*__*__*__*_')


app = Application()