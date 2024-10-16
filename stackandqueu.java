
import java.util.Scanner;
import java.util.Queue;
import java.util.Stack;
import java.util.LinkedList;

public class stackandqueu {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        // Stack to hold items (e.g., things)
        Stack<String> itemStack = new Stack<>();
        
        // Queue to hold items after they are removed from the stack
        Queue<String> itemQueue = new LinkedList<>();

        System.out.print("How many items do you want to add to the stack? ");
        int itemCount = sc.nextInt();
        sc.nextLine();  // Consume the newline left-over from nextInt

        // Adding items to the stack
        for (int i = 1; i <= itemCount; i++) {
            System.out.print("Enter item " + i + " of " + itemCount + ": ");
            String itemName = sc.nextLine();
            itemStack.push(itemName);  // Add to stack
        }

        System.out.println("Items in the stack: " + itemStack);

        // Moving items from the stack to the queue
        while (!itemStack.isEmpty()) {
            System.out.println("Press E to move the top item from the stack to the queue.");
            String input = sc.next().toUpperCase();

            if (input.equals("E")) {
                // Pop item from stack and add to queue
                String item = itemStack.pop();
                itemQueue.add(item);

                System.out.println("Moved \"" + item + "\" from stack to queue.");
                System.out.println("Current Stack: " + itemStack);
                System.out.println("Current Queue: " + itemQueue);
            } else {
                System.out.println("Wrong input! Please press 'E' to move an item.");
            }
        }

        System.out.println("All items have been moved from the stack to the queue.");
        System.out.println("Final Queue: " + itemQueue);
    
    }
}
