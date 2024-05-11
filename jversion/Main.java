import java.util.Scanner;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("How many processes? ");
        int numProcesses = scanner.nextInt();

        ArrayList<Process> processes = Process.getProcesses(numProcesses);

        ArrayList<Process> schedulingOrder = Scheduler.schedule(processes);

        MetricsCalculator.displayResults(schedulingOrder);

        scanner.close();
    }
}
