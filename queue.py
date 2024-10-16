from collections import deque

queue = deque([])
snacks= deque([])

num = int(input("Enter the number of movie you want: "))
for i in range (num):
    wow = input(f"Movie "+ str(i+1) +" of "+str(num) +": ")
    queue.append(wow)
    

for i in range (num):
   snack= input(f"Enter Snacks "+ str(i+1) +" of "+str(num)+ ": ")
   snacks.append(snack)
   

print("this is your movies"+str(queue))
print("this is your snacks"+str(snacks))

while True:
    if not snacks:
        print ("You have no pagkain left")
        break
    eat = (input("Kakain mo na ba ang snalcs (Press E)").upper())
    if eat == "E":
        eat == snacks.pop()
        print(f"You have eaten {snack}")
        print(f"foods remaining {snacks}")
        
    else:
        print("Invalid Input")

print("Thank you sa pag punta sa movie theather")