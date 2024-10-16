import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;

public class treenode extends JFrame {
    JTree tree;
    JLabel label;

    public treenode() {
        // Create root and child nodes
        DefaultMutableTreeNode root = new DefaultMutableTreeNode("B");
        DefaultMutableTreeNode n1 = new DefaultMutableTreeNode("E");
        DefaultMutableTreeNode n2 = new DefaultMutableTreeNode("R");
        DefaultMutableTreeNode n3 = new DefaultMutableTreeNode("O");

        // Add child nodes to the root
        root.add(n1);
        root.add(n2);
        root.add(n3);

        // Adding children to n1, n2, and n3
        DefaultMutableTreeNode n1Child = new DefaultMutableTreeNode("C");
        n1.add(n1Child);  

        DefaultMutableTreeNode n2Child = new DefaultMutableTreeNode("S");
        n2.add(n2Child);  

        DefaultMutableTreeNode n3Child = new DefaultMutableTreeNode("A");
        n3.add(n3Child);  

        // Create the tree
        tree = new JTree(root);
        add(tree);

        // Get the child count for each node
        int childCount = root.getChildCount();
        int childrenCountn1 = n1.getChildCount();
        int childrenCountn2 = n2.getChildCount();
        int childrenCountn3 = n3.getChildCount();

        // Corrected the HTML string to refer to the correct node names
        label = new JLabel("<html>The root node has " + childCount + " children.<br>" +
                           "n1 (E) has " + childrenCountn1 + " children.<br>" +
                           "n2 (R) has " + childrenCountn2 + " children.<br>" +
                           "n3 (O) has " + childrenCountn3 + " children.</html>");

        // Add the label to the frame
        add(label, "North");

        // Set up the JFrame window
        this.setTitle("JTree Example");
        this.setSize(300, 300);
        this.setVisible(true);
    }

    public static void main(String[] args) {
        new treenode();
    }
}
