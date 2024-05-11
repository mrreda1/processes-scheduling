import java.util.Scanner;
import java.util.ArrayList;

class Process {
    private static int pidCounter = 1;
    private int pid;
    private int arrivalTime;
    private int burstTime;
    private int waitingTime;
    private int turnaroundTime;

    public Process(int arrivalTime, int burstTime) {
        this.pid = pidCounter++;
        this.arrivalTime = arrivalTime;
        this.burstTime = burstTime;
        this.waitingTime = 0;
        this.turnaroundTime = 0;
    }

    public int getPid() {
        return pid;
    }

    public int getArrivalTime() {
        return arrivalTime;
    }

    public int getBurstTime() {
        return burstTime;
    }

    public int getWaitingTime() {
        return waitingTime;
    }

    public int getTurnaroundTime() {
        return turnaroundTime;
    }

    public void setWaitingTime(int waitingTime) {
        this.waitingTime = waitingTime;
    }

    public void setTurnaroundTime(int turnaroundTime) {
        this.turnaroundTime = turnaroundTime;
    }
    public static ArrayList<Process> getProcesses(int numProcesses) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Process> processes = new ArrayList<>();
        for (int i = 0; i < numProcesses; i++) {
            int pid = i + 1;
            System.out.print("Enter arrival time for Process " + pid + ": ");
            int arrivalTime = scanner.nextInt();
            System.out.print("Enter burst time for Process " + pid + ": ");
            int burstTime = scanner.nextInt();
            processes.add(new Process(arrivalTime, burstTime));
        }
        scanner.close();
        return processes;
    }

    @Override
    public String toString() {
        return String.format("<Process pid=%d arrivalTime=%d burstTime=%d waitingTime=%d turnaroundTime=%d>",
                pid, arrivalTime, burstTime, waitingTime, turnaroundTime);
    }
}
