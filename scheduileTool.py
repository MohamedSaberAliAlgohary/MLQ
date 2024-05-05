
import Process as processClass
import GanttChart as chart
class ScheduileToolHandler:
    counter=0
    def __init__(self,listOfData=[]) -> None:
        self.listOfAllProcesses=list(listOfData)
        
#?---------------------------------------------------------------------------------------  
 
    def Implementation(self):
      numberOfProcesses=input("Enter number of processes you have in your table :")
      while ScheduileToolHandler.counter<int(numberOfProcesses):
          self.listOfAllProcesses.append(processClass.Process(
              processName=(input("Enter process name: ")),
              arrivlaTime=int(input("Enter process arrival time: ")),
              brustTime=int(input("Enter process brust Time: ")),
              priority=int(input("Enter priority number: ")),
              
              ),)
          print(self.listOfAllProcesses[ ScheduileToolHandler.counter])
          #? Increase the counter for adjust the counter value  
          ScheduileToolHandler.counter+=1
          
         
          print("Process is added successfully")
          
          #? this bloc of code will be excuted when the while bloc done excuted ultemitly                                             )
      else:
          print("Data Entry operation is done ") 
          return self.listOfAllProcesses
       