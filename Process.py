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


def get_processes():
    processes = []
    arrival_time = 0
    burst_time = 1
    with open('input.txt', 'r') as file:
        for line in file:
            if (burst_time != 0):
                arrival_time = int(line.strip())
                burst_time = 0
            else:
                burst_time = int(line.strip())
                processes.append(Process(arrival_time, burst_time))
    return processes
