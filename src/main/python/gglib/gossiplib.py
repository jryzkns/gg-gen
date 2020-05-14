from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import random

from .productioncontext import ProductionContext
import os

def generate(pctx, base_img_path, preamble_font_path, response_font_path):

    random.seed()
    
    img = Image.open(base_img_path)

    draw = ImageDraw.Draw(img)

    draw_preamble(  draw, 
                    300, 
                    pctx.preamble, 
                    ImageFont.truetype(preamble_font_path, 24))

    draw_gossip_girl(   draw, 
                        600, 
                        pctx.response, 
                        response_font_path, 86)

    if not pctx.out_fn.endswith(".png"):
        pctx.out_fn += ".png"

    img.save(pctx.out_fn)

def draw_bounding_box(drawobj, locx, locy, w, h, scalex = 1.2, scaley = 1.1):

    half_w, half_h = w >> 1, h >> 1
    centroidx, centroidy = locx + half_w, locy + half_h
    drawobj.rectangle(( centroidx - scalex * half_w,
                        centroidy - scaley * half_h,
                        centroidx + scalex * half_w,
                        centroidy + scaley * half_h,),
                        fill="white")

def center_draw_w(imgw,textw):

    return (imgw - textw) >> 1

def draw_preamble(drawobj,locy,text,font):

    locx = center_draw_w(drawobj.im.size[0], font.getsize(text)[0])
    draw_bounding_box(drawobj,locx,locy,*font.getsize(text))
    drawobj.text(   (locx,locy),
                    text,
                    fill=(0,0,0,255),
                    font=font)

def preprocess_text(text):

    outbuffer = ""
    for ch in text.lower():
        if ch == " ":
            outbuffer += " "*3
        else:
            outbuffer += ch

    return text

def draw_gossip_girl(drawobj, locy, text, fontpath, fontsize):

    default_font = ImageFont.truetype(fontpath,fontsize)
    text = preprocess_text(text)
    locx = center_draw_w(drawobj.im.size[0], default_font.getsize(text+"     ")[0])

    x_offset = 0
    for ch in text:
        
        if ch != " ":
            ch_w, ch_h = default_font.getsize(ch)
            draw_bounding_box(drawobj, locx + x_offset, locy, ch_w, ch_h)

        ch_font_size = int(fontsize * random.triangular(0.9,1.1,1))

        drawobj.text(   (locx + x_offset + 1, locy + 1), 
                        ch, 
                        font=ImageFont.truetype(fontpath,ch_font_size), 
                        fill=(0,0,0,255))
        drawobj.text(   (locx + x_offset, locy),
                        ch,
                        font=ImageFont.truetype(fontpath,ch_font_size),
                        fill=(222,216,138,255))

        x_offset += ch_w