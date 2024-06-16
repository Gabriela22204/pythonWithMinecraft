from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

blocks = []
diamondOre = 56
blockHits = mc.events.pollBlockHits()

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        hitX, hitY, hitZ = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(hitX, hitY, hitZ)
        blocks.append(block)

        if block == diamondOre:
            mc.postToChat("You found some diamond ore!")
        time.sleep(0.2)