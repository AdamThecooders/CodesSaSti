import java.util.Scanner;
import java.util.Stack;

public class fruitbasket {
    public static void main(String[] args) {
          Scanner Scan = new Scanner(System.in);
          Stack  mgafruits = new Stack();
           System.out.println("Gaano Karami Fruit ang Gusto mo: ");
           int fruitstorage = Scan.nextInt();
              
        for(int i = 1; i <= fruitstorage; i++)
        {System.out.println("Pili ka Fruit: A for Apple , D for DragonFruit, O for Orange , G for Grapes");  
       
        String fruitchoice = Scan.next().toUpperCase(); 
        switch (fruitchoice){
           case "A":
               mgafruits.push("Apple");
               System.out.print("Fruit "+i+"of"+fruitstorage);
               break;
           case "D":
               mgafruits.push("DragonFruit");
               System.out.print("Fruit "+i+" of "+fruitstorage);
               break;  
           case "O":
               mgafruits.push("Orange");
               System.out.print("Fruit "+i+" of "+fruitstorage);
               break;     
           case "G":
               mgafruits.push("Grapes");
               System.out.print("Fruit "+i+" of "+fruitstorage);
                break;
           default:
               System.out.print("Invalid input");
               i--;
        }
               System.out.println(mgafruits);
              }
        int x = fruitstorage-1;
        
          while (x<= fruitstorage&& x>=0){
                  System.out.println("Kakain mo na ba ang fruit (Press E)");
          String eat = Scan.next();
           System.out.println("Meron ka nalang "+x+"left");
           x--;
    }
 System.out.println("you have no fruit");
    }
     
}
