from Process import get_processes
from sjf import schedule_sjf
from utils import calculate_metrics, display_results

processes = get_processes(3)
scheduling_order = schedule_sjf(processes)
metrics = calculate_metrics(scheduling_order)

display_results(scheduling_order, metrics)
# for process in scheduling_order:
#     print(process)
# print(f"Avarage waiting time: {metrics['waiting']}\n"
#       f"Avarage turnaround time: {metrics['turnaround']}")
