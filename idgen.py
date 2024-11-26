import os
import json
import requests
import urllib.parse
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

cwd = os.getcwd()
ID_DIR = f"{cwd}/idcards/"


def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def get_pfp(adm_no):
    url = f"https://bvme.amserp.in/banner/{adm_no}.jpg"

    result = requests.get(url)
    if b"404 Not Found" not in result.content:
        res_img = Image.open(BytesIO(result.content))
        res_img = res_img.resize((375, 375))
        add_corners(res_img, 25)

        return res_img

def generate_id(st_data):
    j_data = json.dumps(st_data)
    enc_data = urllib.parse.quote(j_data)

    url = f"https://api.qrserver.com/v1/create-qr-code/?data={enc_data}&size=300x300"
    result = requests.get(url)

    qr_code_img = Image.open(BytesIO(result.content))
    pfp_img = get_pfp(st_data["st_adm"])


    title_font = ImageFont.truetype("/home/niranjan/Documents/projects/idgenerator/fonts/Rubik-Bold.ttf", 84)
    huge_font = ImageFont.truetype("/home/niranjan/Documents/projects/idgenerator/fonts/Rubik-ExtraBold.ttf", 150)
    subtext_font = ImageFont.truetype("/home/niranjan/Documents/projects/idgenerator/fonts/Rubik-Medium.ttf", 56)

    img = Image.new("RGB", (1920, 1080), 'white')

    name = ImageDraw.Draw(img)
    name.text((600, 180), st_data["st_name"], fill=(0, 0, 0), font=title_font)

    canteenpass = ImageDraw.Draw(img)
    canteenpass.text((180, 680), "CANTEEN PASS", fill=(0, 0, 0), font=huge_font)

    i_adm_no = ImageDraw.Draw(img)
    i_adm_no.text((600, 310), f"Adm. No: {st_data['st_adm']}", fill=(0, 0, 0), font=subtext_font)

    i_class = ImageDraw.Draw(img)
    i_class.text((600, 370), f"Class: {st_data['st_class']}", fill=(0, 0, 0), font=subtext_font)

    qrcode = Image.Image.paste(img, qr_code_img, (1520, 680))
    pfp = Image.Image.paste(img, pfp_img, (150, 150))


    add_corners(img, 50)
    
    img.save(f"{ID_DIR}{st_data['st_adm']}.png")

    print(f"Saved ID Card for {st_data['st_adm']} at {ID_DIR}{st_data['st_adm']}.png")
