
import MLQ as mlq
class GanttChart:
   ##! This class is created for draw the gant chart of our table we have
    def __init__(self, processes: list) -> None:
        self.processes = processes

    def print_gantt_chart_table(self) -> None:
        print("Gantt Chart table details:")
        print("| Process Name | Arrival Time | Burst Time | Priority |")
        print(f"| PName\t| PAT\t| PBT\t| PP\t |")
        for process in self.processes:
             print(f"| {process.name}\t| {process.arrivalTime}\t| {process.brustTime}\t| {process.priority}\t |")
        