import random 

class Process:
   numberOfProcesses:int=0
   processId:int=1
   assignedRandomeName=["n1","n2","n3","n5","n5","n6","n7","n8","n9","n10"]
   alresdyAssignedNames:set=set({})



   def __init__(self,processName:str="skip",arrivlaTime:int=0,brustTime:int=0,priority:int=0)->None:
       self.name=Process.handleNotAssignedProcessName(processName)
       self.id=Process.processId
       self.arrivalTime=arrivlaTime
       self.brustTime=brustTime
       self.priority=priority
       self.waitingTime=0
       self.turnAroundTime=0
       self.completionTime=0
       Process.processId+=1
       Process.numberOfProcesses+=1

   def __str__(self) -> str:
        return f"The Process name is {self.name}: Process number: {self.id} has an Arrival time: {self.arrivalTime}"  
   
   @staticmethod
   def handleNotAssignedProcessName(name)->str:
       if name=="skip":
           name=random.choice(Process.assignedRandomeName)
           while  name  in Process.alresdyAssignedNames:
              name=random.choice(Process.assignedRandomeName) 
           else : 
               Process.alresdyAssignedNames.add(name)
               return name
       else: 
           return name
 
process1 = Process(processName=input("enter name \n"),arrivlaTime=0,brustTime=3,priority=1)
print(process1)
##!  create test objects here saber
              
#  {
#               process1 = Process(processName="p1",arrivlaTime=0,brustTime=3,priority=1),
#               process2 = Process(processName="p2",arrivlaTime=3,brustTime=4,priority=2) , 
#               process3 = Process(processName="p3",arrivlaTime=4,brustTime=5,priority=3),
#               process4 = Process(processName="p4",arrivlaTime=7,brustTime=6,priority=4),
#               process5 = Process(processName="p5",arrivlaTime=8,brustTime=7,priority=5) , 
#               process6 = Process(processName="p6",arrivlaTime=9,brustTime=8,priority=6),
#               process7 = Process(processName="p7",arrivlaTime=10,brustTime=9,priority=7),
#               process8 = Process(processName="p8",arrivlaTime=11,brustTime=10,priority=8),  
#               process9 = Process(processName="p9",arrivlaTime=13,brustTime=11,priority=9)
              
#        }
       
       

          
