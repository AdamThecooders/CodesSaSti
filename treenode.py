import tkinter as tk
from tkinter import ttk

class TreeNodeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("TreeNode Example")
        self.geometry("300x300")

        # Create a treeview widget
        self.tree = ttk.Treeview(self)
        self.tree.pack(expand=True, fill=tk.BOTH)

        # Add root node
        root = self.tree.insert("", "end", "B", open=True)

        # Add child nodes to the root
        n1 = self.tree.insert(root, "end", "E", open=True)
        n2 = self.tree.insert(root, "end", "R", open=True)
        n3 = self.tree.insert(root, "end", "O", open=True)

        # Add children to n1, n2, and n3
        self.tree.insert(n1, "end", "C")
        self.tree.insert(n2, "end", "S")
        self.tree.insert(n3, "end", "A")

        # Get the child count for each node
        childCount = len(self.tree.get_children(root))
        childrenCountn1 = len(self.tree.get_children(n1))
        childrenCountn2 = len(self.tree.get_children(n2))
        childrenCountn3 = len(self.tree.get_children(n3))

        # Display the child counts in a label
        label_text = f"The root node has {childCount} children.\n" \
                     f"n1 (E) has {childrenCountn1} children.\n" \
                     f"n2 (R) has {childrenCountn2} children.\n" \
                     f"n3 (O) has {childrenCountn3} children."
        
        label = tk.Label(self, text=label_text)
        label.pack(side=tk.TOP, padx=10, pady=10)

if __name__ == "__main__":
    app = TreeNodeApp()
    app.mainloop()
