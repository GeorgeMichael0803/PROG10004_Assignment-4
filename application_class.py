
from wireless_network import *
class Application:
   def __init__(self):
      self.totalNoOfSensors = 0
      self.listOfSensors = []    
      self.sensorDictionary = {}


      welcome = WirelessNetworks()
      welcome.greetMessage()


      self.createSensors()
   
   def createSensors(self):
      while True:
         try:
            numOfSensors = int(input("Enter the number of sensors: "))
            break
         except:
            print("This is an invalid entry for the number of sensors")
      self.setTotalSensors(numOfSensors)

      self.seperation()

      for sensorNode in range(1, self.totalNoOfSensors + 1):
         sensorNode = WirelessNetworks()

         id = (input('Enter the Sensor ID: '))
         while any(char.isdigit() for char in id):
            print("This is an invalid entry for sensor Id!")
            id = input('Enter the sensor ID: ')
         sensorNode.setID(id)
         
         while True:
            try:
               numOfNeighbours = int(input("Enter the number of neighbours: "))
               break
            except:
               print("This is an invalid entry for the number of neighbours")
         sensorNode.setNeighbours(numOfNeighbours)

         for neighbour in range(1, sensorNode.neighbours + 1):
            neighbour = WirelessNetworks()

            neighbourId = input("Enter the neighbour for Sensor " + sensorNode.id + ": ")

            
            while any(char.isalpha()== False for char in neighbourId):
               print("This is an invalid entry for the neighbour's name and/or distance!")
               neighbourId = input("Enter the neighbour for sensor " + sensorNode.id + ": ")
            neighbour.setID(neighbourId)
         

            self.convrtToDictionary(sensorNode, neighbour)

         while True:
            try:
               o2Level = int(input("Enter the Oxygen level in %: "))
               break
            except:
               print("This is an invalid entry for the oxygen level!")
         sensorNode.setOxygenLevel(o2Level)

         while True:
            try:
               temp = float(input("Enter the temperature measurement: "))
               break
            except:
               print("This is an invalid entry for the temperature!")
         sensorNode.setTemperature(temp)

         self.listOfSensors.append(sensorNode)
         self.seperation()

      self.findPath()
         

            
   def convrtToDictionary(self, sensorNode, neighbour):
      distance = (neighbour.id, int(input("Enter the distance to " + sensorNode.id + ": ")))
      if sensorNode.id not in self.sensorDictionary:
         self.sensorDictionary[sensorNode.id] = [distance]
      else:
         self.sensorDictionary[sensorNode.id].append(distance)


   def findPath(self):
      source = input("Enter the source sensor: ")
      path = [source]
      destination = input("Enter the destination sensor: ")
      try:
         self.findPathHelper(source, destination, path)
         print("Path= ",path)
      except RecursionError:
         print('The destination is not found')  

      '''if self.findPathHelper(source, destination, path):     #maybe try except would work  ,RecursionError
         print("Path= ",path)
      else:
         print("The destination is not found")'''
         
   def findPathHelper(self, source, destination, path):
      if source == destination:
         return(True)
      currentMax = self.sensorDictionary[source][0]
      for id, distance in self.sensorDictionary[source]:
         if distance > currentMax[1]:
            currentMax = (id, distance)
      path.append(currentMax[0])
      return(self.findPathHelper(currentMax[0], destination, path))



   def setTotalSensors(self, sensorCount):
      self.totalNoOfSensors = sensorCount

   def seperation(self):
      print('__*__*__*__*__*__*__*__*__*__*__*__')


obj = Application()
