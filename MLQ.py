
from collections import deque
from statistics import mean #?--------> Get the mean value of the waiting time
import Process
#?----------------------------------------------------------------------------------------------------------------------------------------------------------------
class MLQ:
    def __init__(self,allData) -> None:
        self.ListOfAllProcesses=allData

#? Function to implement MLQ CPU scheduling
    def MLQScheduling(self):
      high_queue = deque()    #? Queue for high priority processes (Round Robin)
      medium_queue = deque()  #? Queue for medium priority processes (Shortest Remaining First)
      low_queue = deque()     #? Queue for low priority processes (Shortest Job Next)
      current_time = 0        #? Start time of all the processes
      EventViewer =[]         #? The database logic to keep track of the actions

    
      for process in self.ListOfAllProcesses: #? -------> Iterate through all the processes and add them to their respective queues
        if process.priority == 0:
            high_queue.append(process)
        elif process.priority == 1:
            medium_queue.append(process)
        elif process.priority == 2:                                              
            low_queue.append(process)
            
            
    
      while high_queue or medium_queue or low_queue:   #?------------> Process execution loop
                 ##!------------------------->   high queue
        if high_queue:       ##? check if the queue is not empty 
            process = high_queue.popleft()  #? get the first element in the queue ==> fifo algorithm
            EventViewer.append(f"At time = {current_time}\n{process.name} Entered the high queue")
            EventViewer.append(f"{process.name} left the high queue")
            EventViewer.append(f"{process.name} Entered kernel")
            if process.brustTime >= 8:
                process.brustTime -= 8
                EventViewer.append(f"{process.name} left the kernel")
                EventViewer.append(f"{process.name} entered the medium queue")
                medium_queue.append(process)
                process.waitingTime += current_time - process.arrivalTime
                current_time+=8
                process.arrivalTime=current_time
                
            else:
                value= process.brustTime
                process.brustTime -= process.brustTime
                EventViewer.append(f"{process.name} left the kernel")
                EventViewer.append(f"{process.name} finished execution")
                process.waitingTime += current_time - process.arrivalTime
                current_time+=value
            
                ##! ------------------------>    medium queue
        elif medium_queue:     ##? check if the queue is not empty 
            process = medium_queue.popleft() ##? get the first element in the queue ==> fifo algorithm
            EventViewer.append(f"At t = {current_time}\n{process.name} Entered the medium queue")
            EventViewer.append(f"{process.name} left the medium queue")
            EventViewer.append(f"{process.name} entered kernel")
            
            if process.brustTime >= 16:
                process.brustTime -= 16
                EventViewer.append(f"{process.name} left the kernel")
                EventViewer.append(f"{process.name} entered the low queue")
                low_queue.append(process)
                process.waitingTime += current_time - process.arrivalTime
                current_time+=16
                process.arrivalTime=current_time
            else:
                value= process.brustTime
                process.brustTime -= process.brustTime
                EventViewer.append(f"{process.name} left the kernel")
                EventViewer.append(f"{process.name} finished execution")
                process.waitingTime += current_time - process.arrivalTime
                current_time+=value
                process.arrivalTime=current_time
                
                
                
                 ##!--------------------------->    low queue
        elif low_queue:      ##? check if the queue is not empty 
            process = low_queue.popleft() ##? get the first element in the queue ==> fifo algorithm
            EventViewer.append(f"At t = {current_time}\n{process.name} Entered the low queue")
            EventViewer.append(f"{process.name} left the low queue")
            EventViewer.append(f"{process.name} entered kernel")
            value=process.brustTime
            process.brustTime -=process.brustTime #! 
            EventViewer.append(f"{process.name} left the kernel")
            process.waitingTime += current_time - process.arrivalTime
            current_time+=value
            EventViewer.append(f"{process.name} finished execution at time ={current_time}")
            



    #? Calculate average waiting time
        waiting_times = [process.waitingTime for process in self.ListOfAllProcesses]
        #? list comerhintion to loop on the list
        average_waiting_time = mean(waiting_times)

    #? Print the eventViewer and waiting times
        for event in EventViewer:
          print(event)
        print("Waiting Times:")
        for process in self.ListOfAllProcesses:
          print(f"{process.name}: {process.waitingTime}")
        print(f"Average Waiting Time: {average_waiting_time}")


#?------------------------------------------------------------------------------------------------------
#! New  knowledge about data structure in python 
#! Here are the differences between high_queue.popleft(), high_queue.pop(), and high_queue.pop(0):

#! high_queue.popleft():
#? Removes and returns the leftmost element (i.e., the first element) from the deque.
#? This operation is O(1) because it only involves updating the internal pointers of the deque.
#? If the deque is empty, it raises an IndexError.



#! high_queue.pop():
#? Removes and returns the rightmost element (i.e., the last element) from the deque.
#? This operation is O(1) because it only involves updating the internal pointers of the deque.
#? If the deque is empty, it raises an IndexError.
#! high_queue.pop(0):
#? Removes and returns the leftmost element (i.e., the first element) from the deque.
#? This operation is O(n) because it involves shifting all the elements in the deque to the left, where n is the length of the deque.
#? If the deque is empty, it raises an IndexError.


#! In summary:

#? popleft() and pop(0) both remove the first element from the deque, but popleft() is more efficient (O(1) vs O(n)).
#? pop() removes the last element from the deque.
#? When to use each:
#? Use popleft() when you need to process elements in the order they were added to the deque (FIFO, First-In-First-Out).
#? Use pop() when you need to process elements in the reverse order they were added to the deque (LIFO, Last-In-First-Out).
#? Avoid using pop(0) unless you have a specific reason to do so, as it is less efficient than popleft()