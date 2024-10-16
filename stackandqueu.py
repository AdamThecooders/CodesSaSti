from collections import deque

# Initialize stack and queue
item_stack = []
item_queue = deque()

# Ask user how many items they want to add to the stack
item_count = int(input("How many items do you want to add to the stack? "))

# Adding items to the stack
for i in range(1, item_count + 1):
    item_name = input(f"Enter item {i} of {item_count}: ")
    item_stack.append(item_name)  # Push item onto the stack

print(f"Items in the stack: {item_stack}")

# Moving items from the stack to the queue
while item_stack:
    input_command = input("Press E to move the top item from the stack to the queue: ").upper()

    if input_command == "E":
        # Pop item from stack and add to queue
        item = item_stack.pop()
        item_queue.append(item)

        print(f"Moved '{item}' from stack to queue.")
        print(f"Current Stack: {item_stack}")
        print(f"Current Queue: {list(item_queue)}")
    else:
        print("Wrong input! Please press 'E' to move an item.")

print("All items have been moved from the stack to the queue.")
print(f"Final Queue: {list(item_queue)}")
