
from wireless_network import *
class Application:
   def __init__(self):                                           #constructor method of application class
      self.totalNoOfSensors = 0
      self.listOfSensors = []    
      self.sensorDictionary = {}


      welcome = WirelessNetworks()                              #creating an object for WirelessNetwork class
      welcome.greetMessage()                                    #calling the method to print the first statement


      self.createSensors()                                      #calling the method to print the statements
   
   def createSensors(self):                                     #method that creates the sensors
      while True:                                               #while for number of sensors
         try:
            numOfSensors = int(input("Enter the number of sensors: "))
            break
         except:
            print("This is an invalid entry for the number of sensors")
      self.setTotalSensors(numOfSensors)

      self.seperation()                                        #calls separation function

      for sensorNode in range(1, self.totalNoOfSensors + 1):   #loop for data of all the sensors
         sensorNode = WirelessNetworks()

         id = (input('Enter the Sensor ID: '))                 #loop for input of sensor id
         while any(char.isdigit() for char in id):             
            print("This is an invalid entry for sensor Id!")
            id = input('Enter the sensor ID: ')
         sensorNode.setID(id)
         
         while True:                                         #loop for input of number of neigbours
            try:
               noOfNeighbours = int(input("Enter the number of neighbours: "))
               break
            except:
               print("This is an invalid entry for the number of neighbours")
         sensorNode.setNeighbours(noOfNeighbours)

         for wn in range(1, sensorNode.neighbours + 1):               #loop for details of neighbour sensors
            wn = WirelessNetworks()

            wnId = input("Enter the neighbour for Sensor " + sensorNode.id + ": ")

            
            while any(char.isalpha()== False for char in wnId):                        #loop for neighbour sensor name
               print("This is an invalid entry for the neighbour's name and/or distance!")
               wnId = input("Enter the neighbour for sensor " + sensorNode.id + ": ")
            wn.setID(wnId)
         

            self.convrtToDictionary(sensorNode, wn)                           #calling the function to convert to dictionary

         while True:                                                          #loop for entering the oxygen level
            try:
               o2Level = int(input("Enter the Oxygen level in %: "))
               break
            except:
               print("This is an invalid entry for the oxygen level!")
         sensorNode.setOxygenLevel(o2Level)

         while True:                                                         #loop for entering the temperature mesurements
            try:
               temp = float(input("Enter the temperature measurement: "))
               break
            except:
               print("This is an invalid entry for the temperature!")
         sensorNode.setTemperature(temp)

         self.listOfSensors.append(sensorNode)
         self.seperation()

      self.findPath()
         

            
   def convrtToDictionary(self, sensorNode, wn):                              #method to convert to dictionary
      distance = (wn.id, int(input("Enter the distance to " + sensorNode.id + ": ")))
      if sensorNode.id not in self.sensorDictionary:
         self.sensorDictionary[sensorNode.id] = [distance]
      else:
         self.sensorDictionary[sensorNode.id].append(distance)


   def findPath(self):                                                       #method to find path
      source = input("Enter the source sensor: ")
      path = [source]
      destination = input("Enter the destination sensor: ")
      try:
         self.findPathRecurssion(source, destination, path)
         print("Path= ",path)
      except RecursionError:
         print('The destination is not found')  

         
   def findPathRecurssion(self, source, destination, path):               #method for help in finding path with recurssion
      if source == destination:
         return(True)
      currentMaximum = self.sensorDictionary[source][0]
      for id, distance in self.sensorDictionary[source]:
         if distance > currentMaximum[1]:
            currentMaximum = (id, distance)
      path.append(currentMaximum[0])
      return(self.findPathRecurssion(currentMaximum[0], destination, path))



   def setTotalSensors(self, sensorCount):                            #mutator method for setting the total number of sensors
      self.totalNoOfSensors = sensorCount

   def seperation(self):                                              #method to print the seperations
      print('__*__*__*__*__*__*__*__*__*__*__*__')


obj = Application()
