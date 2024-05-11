import java.util.ArrayList;

public class MetricsCalculator {

    public static boolean validateInput(String value) {
        try {
            return Integer.parseInt(value) >= 0;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public static double[] calculateMetrics(ArrayList<Process> processes) {
        double[] avgTime = new double[2]; // Index 0: waiting time, Index 1: turnaround time
        for (Process process : processes) {
            avgTime[0] += process.getWaitingTime();
            avgTime[1] += process.getTurnaroundTime();
        }

        int numProcesses = processes.size();
        avgTime[0] /= numProcesses;
        avgTime[1] /= numProcesses;

        return avgTime;
    }

    public static void displayResults(ArrayList<Process> schedulingOrder) {
        double[] metrics = calculateMetrics(schedulingOrder);

        System.out.println("\nProcess\t Waiting Time\t Turnaround Time");
        for (Process process : schedulingOrder) {
            System.out.println(process.getPid() + "\t " + process.getWaitingTime() + "\t\t "
                    + process.getTurnaroundTime());
        }

        System.out.println("\nAverage Waiting Time: " + Math.round(metrics[0] * 1000.0) / 1000.0);
        System.out.println("Average Turnaround Time: " + Math.round(metrics[1] * 1000.0) / 1000.0);
    }
}
