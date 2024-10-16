mgafruits = []
fruitstorage = int(input("Gaano Karami Fruit ang Gusto mo: "))

for i in range(fruitstorage):
    x = input("Pili ka Fruit: A for Apple, D for DragonFruit, O for Orange, G for Grapes: ").upper()
    
    if x == "A":
        mgafruits.append("Apple")
    elif x == "D":
        mgafruits.append("DragonFruit")
    elif x == "O":
        mgafruits.append("Orange")
    elif x == "G":
        mgafruits.append("Grapes")
    else:
        print("Invalid input, please select again.")
        i -= 1  # Repeat the same index for invalid input
    
    print(f"Fruit {i+1} of {fruitstorage}: {mgafruits[-1]}")

print("All selected fruits:", mgafruits)

# Now, asking if the user wants to "eat" the fruits one by one
while fruitstorage > 0:
    eat = input("Kakain mo na ba ang fruit? (Press E to eat): ").upper()
    if eat == "E" and mgafruits:
        eaten_fruit = mgafruits.pop()
        print(f"You ate: {eaten_fruit}")
        fruitstorage -= 1
    else:
        print("Invalid input or no more fruits to eat.")

print("All fruits have been eaten.")
