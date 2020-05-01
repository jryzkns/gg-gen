import os

os.system("pip install Pillow")

from gossiplib import *
from data import *

img = Image.open("base.jpg")

draw = ImageDraw.Draw(img)
draw_preamble(  draw, 
                300, 
                preamble, 
                ImageFont.truetype("arial.ttf",24))

draw_gossip_girl(   draw, 
                    600, 
                    response, 
                    "Helvetica 33 Thin Extended.ttf",86)

img.save("out.png")