from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


mc.postToChat("Comece a clicar!!!")

# Wait 60 seconds
time.sleep(60)

# Get the list of block hits
blockHits = mc.events.pollBlockHits()

# Display the length of the block hits list to chat
for hit in blockHits:
    x, y, z = hit.pos.x, hit.pos.y, hit.pos.z

blockHitsLength = hit

mc.postToChat("Your score is " + str(blockHitsLength))


