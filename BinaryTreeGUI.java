import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

// Node class for Binary Tree
class Node {
    int key;
    Node left, right;

    public Node(int item) {
        key = item;
        left = right = null;
    }
}

// Binary Tree class
class BinaryTree {
    Node root;

    public BinaryTree() {
        root = null;
    }

    // Insert method to add nodes to the tree
    public void insert(int key) {
        root = insertRec(root, key);
    }

    // A recursive function to insert a new key in the Binary Tree
    Node insertRec(Node root, int key) {
        if (root == null) {
            root = new Node(key);
            return root;
        }

        if (key < root.key) {
            root.left = insertRec(root.left, key);
        } else if (key > root.key) {
            root.right = insertRec(root.right, key);
        }

        return root;
    }

    // In-order traversal to display the tree (Left, Root, Right)
    public void inorder(Node root) {
        if (root != null) {
            inorder(root.left);
            System.out.print(root.key + " ");
            inorder(root.right);
        }
    }
}

// Custom JPanel class to draw the binary tree
class TreePanel extends JPanel {
    private final BinaryTree tree;

    public TreePanel(BinaryTree tree) {
        this.tree = tree;
        setPreferredSize(new Dimension(800, 600));
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (tree.root != null) {
            drawTree(g, tree.root, getWidth() / 2, 50, getWidth() / 4);
        }
    }

    // Draw the tree nodes and branches
    private void drawTree(Graphics g, Node root, int x, int y, int xOffset) {
        if (root == null) return;

        g.setColor(Color.BLUE);
        g.fillOval(x - 15, y - 15, 30, 30);
        g.setColor(Color.WHITE);
        g.drawString(Integer.toString(root.key), x - 7, y + 4);

        if (root.left != null) {
            g.drawLine(x - 10, y + 10, x - xOffset + 10, y + 50 - 10);
            drawTree(g, root.left, x - xOffset, y + 50, xOffset / 2);
        }
        if (root.right != null) {
            g.drawLine(x + 10, y + 10, x + xOffset - 10, y + 50 - 10);
            drawTree(g, root.right, x + xOffset, y + 50, xOffset / 2);
        }
    }
}

// Main class for Binary Tree GUI
public class BinaryTreeGUI {
    private BinaryTree tree = new BinaryTree();

    public BinaryTreeGUI() {
        JFrame frame = new JFrame("Binary Tree Visualizer");
        TreePanel treePanel = new TreePanel(tree);

        JTextField inputField = new JTextField(10);
        JButton insertButton = new JButton("Insert");
        JLabel instructionLabel = new JLabel("Enter number to insert into tree:");

        insertButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    int key = Integer.parseInt(inputField.getText());
                    tree.insert(key);
                    treePanel.repaint();
                    inputField.setText(""); // Clear the input field after insertion
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Please enter a valid number.");
                }
            }
        });

        JPanel controlPanel = new JPanel();
        controlPanel.add(instructionLabel);
        controlPanel.add(inputField);
        controlPanel.add(insertButton);

        frame.add(treePanel, BorderLayout.CENTER);
        frame.add(controlPanel, BorderLayout.SOUTH);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new BinaryTreeGUI();
            }
        });
    }
}
