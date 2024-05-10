from Process import Process

def schedule(processes: list[Process]) -> list[Process]:
    # Sort processes based on arrival time
    processes.sort(key=lambda x: x.arrival_time)
    
    # Initialize variables
    current_time = 0
    total_processes = len(processes)
    completed_processes = 0
    scheduling_order = []

    while completed_processes < total_processes:
        # Filter arrived proccess
        available_processes = [p for p in processes if p.arrival_time <= current_time and p.burst_time > 0]

        if not available_processes:
            current_time += 1
            continue

        # Select the process with the shortest burst time
        shortest_process = min(available_processes, key=lambda x: x.burst_time)

        processes.remove(shortest_process)

        shortest_process.waiting_time = current_time - shortest_process.arrival_time
        shortest_process.turnaround_time = shortest_process.waiting_time + shortest_process.burst_time

        current_time += shortest_process.burst_time

        completed_processes += 1
        scheduling_order.append(shortest_process)

    return scheduling_order
