from PIL import Image,ImageFont,ImageDraw
import json
from proceses import backgroundcolor,convert_jpg_to_semi_transparent_png,backgroundcreate,set_image_alpha


#バックグラウンドの画像を読み込む
background = Image.open(r"./output/Bennett.png").convert("RGBA")

#ボックスの画像を読み込む
box_img = Image.open(r"item\boxv2.png").convert("RGBA")

#キャラ画像を読み込む
chara_img = Image.open(r"data\chara_img\banner_Bennett.png").convert("RGBA")

genshin_color = open(r"data\color.json", 'r')
genshin_color = json.load(genshin_color)

box_img = set_image_alpha(box_img,alpha=0.2)
#リサイズする
new_size = (500, 500)
box_img = box_img.resize(new_size)


draw = ImageDraw.Draw(box_img)

font = ImageFont.truetype(f'./font/ja-jp.ttf', 40)
draw.text((40, 50), "攻撃力", '#ffffff', font=font)


#リサイズする
new_size = (int(800*2), int(400*2))
chara_img = chara_img.resize(new_size)


background.alpha_composite(chara_img,dest=(-400,-100))
background.alpha_composite(box_img,dest=(50,550))    



background.show()



