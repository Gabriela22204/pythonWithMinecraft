toDoFile = open("toDoList.txt", "w")

toDoList = ""

toDoItem = input("Enter a to-do list item: ")

while toDoItem != "exit":
    toDoList = toDoList + toDoItem + "\n"
    toDoItem = input("Enter a to-do list item: ")
# Write the to-do list to the file

toDoFile.write(toDoList)
# Close the file
toDoFile.close()
