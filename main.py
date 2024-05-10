from Process import get_processes
from scheduling import schedule
from utils import calculate_metrics, display_results

num_of_processes = input("How many processes? ")
try:
    num_of_processes = int(num_of_processes)
except Exception as e:
    raise e

processes = get_processes(num_of_processes)
scheduling_order = schedule(processes)
metrics = calculate_metrics(scheduling_order)

display_results(scheduling_order, metrics)
