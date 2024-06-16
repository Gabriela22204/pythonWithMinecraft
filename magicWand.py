from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

mc.postToChat("Transforme blocos em meloes!!")

time.sleep(60)

hits = mc.events.pollBlockHits()
block = 103

for hit in hits:
    x, y, z = hit.pos.x, hit.pos.y, hit.pos.z

    # Set melon blocks at the coordinates
    mc.setBlock(x, y, z, block)

mc.postToChat("tadahhh")
