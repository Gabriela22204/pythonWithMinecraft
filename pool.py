from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z

width = 10 # largura da piscina
height = 5 # altura
length = 6 # comprimento
blockType = 4
air = 0

mc.setBlocks(x, y, z, x + width, y - 2, z + length, blockType)
mc.setBlocks(x+1,y,z+1, (x+width)-1, y-1,(z+length)-1, 8)
# a água deve começar entorno da piscina(y) e para não transbordar: (y-1) 

mc.setBlocks(x+1,y+1,z+1, (x+width)-1, (y+height),(z+length)-1, 0)
#para quebrar bloco acima da piscina usamos o ar
