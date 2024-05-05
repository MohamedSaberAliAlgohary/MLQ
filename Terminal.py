import Process
import GanttChart
import TerminalBodyOne as HandelerOne
import ToolViewer as tools
import scheduileTool  
import MLQ as mlq

##?----------------------------------------------------------------------------------------------
print("Welcome to processes scheduling")
print(f">")
firstInputFromUser=input("> Enter -h  (or) --help for show all options\n>")

if firstInputFromUser =="-h" or firstInputFromUser=="--help" :
     HandelerOne.TerminalIfBody()  
else:print("Invalid input ,enter valid input  ") 

checker= input("Done ?\nok or no\n>")
if checker=="ok":
    print("Enjoy with our code")
else:print("We will redpond to  your error soon\n")


tool=input("Dispaly all tools ?\n>ok or no\n")
if tool =="ok":
   tools.ToolViewer()  
   
anyTool=input("Enter number of code you need (1) or (2)\n> ")

if anyTool=="1":
    Data=scheduileTool.ScheduileToolHandler().Implementation()
    GanttChart.GanttChart(processes=Data).print_gantt_chart_table()
    mlqObj=mlq.MLQ(allData=Data)
    mlqObj.MLQScheduling()
    
#print(allData[0])
elif anyTool=="2":
    print("Coming soon")
    print("No connection to the internet")
else:
    print("Error Happened !!!!!")


