from gossiplib import *

img = Image.open("base.jpg")

preamble = "i haven't gotten my textbooks yet"
response = "pdf girl"

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