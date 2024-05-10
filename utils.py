from Process import Process

def validate_input(value):
    try:
        return int(value) >= 0
    except ValueError:
        return False

def calculate_metrics(processes: list[Process]) -> dict:
    avg_time = {'waiting' : 0.0,
                'turnaround' : 0.0,
                }
    for process in processes:
        avg_time['waiting'] += process.waiting_time
        avg_time['turnaround'] += process.turnaround_time

    num_processes = len(processes)
    avg_time['waiting'] /= num_processes
    avg_time['turnaround'] /= num_processes

    return avg_time

def display_results(scheduling_order):
    metrics = calculate_metrics(scheduling_order)

    print("\nProcess\t Waiting Time\t Turnaround Time")
    for process in scheduling_order:
        print(f"{process.pid}\t {process.waiting_time}\t\t {process.turnaround_time}\t")
    
    print("\nAverage Waiting Time: ", round(metrics['waiting'], 3))
    print("Average Turnaround Time: ", round(metrics['turnaround'], 3))
