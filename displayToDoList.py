from mcpi.minecraft import Minecraft
mc = Minecraft.create()

toDoList = open("toDoList.txt", "r")

for line in toDoList:
# Output "line" to the chat
    mc.postToChat(toDoList.readline())

toDoList.close()
