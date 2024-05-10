import os
import matplotlib.pyplot as plt
from Process import Process
import numpy as np


def printChart(scheduling_order: list[Process]):
    num_of_processes = len(scheduling_order)
    last = scheduling_order[num_of_processes - 1]
    plt.figure(figsize=(last.burst_time+last.waiting_time+last.arrival_time+1, num_of_processes + 1))

    i = 1
    for p in scheduling_order:
        plt.barh(y=i, width=p.burst_time, left=p.waiting_time + p.arrival_time, label=f'Process {p.pid}')
        i += 1

    plt.xlabel('Time')
    plt.ylabel('Processes')
    plt.title('Gantt Chart (SJF Non-Preemptive)')
    plt.xticks(np.arange(0, last.burst_time+last.waiting_time+last.arrival_time+1, step=1))
    plt.yticks([])
    plt.legend(loc='lower right')
    plt.grid(axis='x')
    plt.savefig('plot.png')
    os.system("viewnior plot.png &")
