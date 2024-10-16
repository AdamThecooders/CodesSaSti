import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class queue {
     public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Deque<String> movies = new LinkedList<>();
        Deque<String> snacks = new LinkedList<>();

        System.out.print("Enter the number of movie you want: ");
        int num = scanner.nextInt();
        scanner.nextLine();  // Consume newline

        // Input movies
        for (int i = 0; i < num; i++) {
            System.out.print("Movie " + (i + 1) + " of " + num + ": ");
            String movie = scanner.nextLine();
            movies.add(movie);
        }

        // Input snacks
        for (int i = 0; i < num; i++) {
            System.out.print("Enter Snacks " + (i + 1) + " of " + num + ": ");
            String snack = scanner.nextLine();
            snacks.add(snack);
        }

        System.out.println("this is your movies" + movies);
        System.out.println("this is your snacks" + snacks);

        // Eat snacks loop
        while (true) {
            if (snacks.isEmpty()) {
                System.out.println("You have no pagkain left");
                break;
            }

            System.out.print("Kakain mo na ba ang snalcs (Press E): ");
            String eat = scanner.nextLine().toUpperCase();

            if (eat.equals("E")) {
                String eatenSnack = snacks.pop();
                System.out.println("You have eaten " + eatenSnack);
                System.out.println("foods remaining " + snacks);
            } else {
                System.out.println("Invalid Input");
            }
        }

        System.out.println("Thank you sa pag punta sa movie theater.");
        scanner.close();
    }
}

