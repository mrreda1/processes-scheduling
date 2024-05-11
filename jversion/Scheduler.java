import java.util.ArrayList;

public class Scheduler {
    public static ArrayList<Process> schedule(ArrayList<Process> processes) {
        // Sort processes based on arrival time
        processes.sort((p1, p2) -> Integer.compare(p1.getArrivalTime(), p2.getArrivalTime()));

        // Initialize variables
        int currentTime = 0;
        int totalProcesses = processes.size();
        int completedProcesses = 0;
        ArrayList<Process> schedulingOrder = new ArrayList<>();

        while (completedProcesses < totalProcesses) {
            // Filter arrived processes
            ArrayList<Process> availableProcesses = new ArrayList<>();
            for (Process p : processes) {
                if (p.getArrivalTime() <= currentTime) {
                    availableProcesses.add(p);
                }
            }

            if (availableProcesses.isEmpty()) {
                currentTime++;
                continue;
            }

            // Select the process with the shortest burst time
            Process shortestProcess = availableProcesses.stream()
                    .min((p1, p2) -> Integer.compare(p1.getBurstTime(), p2.getBurstTime())).get();

            processes.remove(shortestProcess);

            shortestProcess.setWaitingTime(currentTime - shortestProcess.getArrivalTime());
            shortestProcess.setTurnaroundTime(shortestProcess.getWaitingTime() + shortestProcess.getBurstTime());

            currentTime += shortestProcess.getBurstTime();

            completedProcesses++;
            schedulingOrder.add(shortestProcess);
        }

        return schedulingOrder;
    }
}

