from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
pos = mc.player.getPos()


count = 0
while count < 180:
    mc.setBlock(pos.x, pos.y, pos.z, 8)
    count += 1
    time.sleep(1)
