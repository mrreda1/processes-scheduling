class Process:
    pid_counter = 1
    
    def __init__(self, arrival_time, burst_time):
        self.pid = Process.pid_counter
        Process.pid_counter += 1
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
    def __repr__(self):
        return f'<Process pid={self.pid} arrival_time={self.arrival_time}\
 burst_time={self.burst_time} waiting_time={self.waiting_time}\
 turnaround_time={self.turnaround_time}>'


def get_processes(num_processes):
    processes = []
    for i in range(num_processes):
        pid = i + 1
        arrival_time = int(input(f"Enter arrival time for Process {pid}: "))
        burst_time = int(input(f"Enter burst time for Process {pid}: "))
        processes.append(Process(arrival_time, burst_time))
    return processes
